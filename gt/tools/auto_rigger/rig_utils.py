"""
Auto Rigger Utilities

Code Namespace:
    tools_rig_utils # import gt.tools.auto_rigger.rig_utils as tools_rig_utils
"""

import gt.tools.auto_rigger.rig_constants as tools_rig_const
import gt.tools.auto_rigger.rig_framework as tools_rig_frm
import gt.core.transform as core_trans
import gt.core.constraint as core_cnstr
import gt.core.rigging as core_rigging
import gt.core.hierarchy as core_hrchy
import gt.core.naming as core_naming
import gt.core.curve as core_curve
import gt.core.color as core_color
import gt.core.str as core_str
import gt.core.attr as core_attr
import gt.core.node as core_node
import gt.core.uuid as core_uuid
import maya.cmds as cmds
import logging
import json

# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# ------------------------------------------ Lookup functions ------------------------------------------
def find_proxy_from_uuid(uuid_string):
    """
    Return a proxy if the provided UUID is present in the attribute RiggerConstants.PROXY_ATTR_UUID
    Args:
        uuid_string (str): UUID to look for (if it matches, then the proxy is found)
    Returns:
        Node or None: If found, the proxy with the matching UUID, otherwise None
    """
    proxy = core_uuid.get_object_from_uuid_attr(
        uuid_string=uuid_string, attr_name=tools_rig_const.RiggerConstants.ATTR_PROXY_UUID, obj_type="transform"
    )
    if proxy:
        return core_node.Node(proxy)


def find_joint_from_uuid(uuid_string):
    """
    Return a joint if the provided UUID is present in the attribute RiggerConstants.JOINT_ATTR_UUID
    Args:
        uuid_string (str): UUID to look for (if it matches, then the joint is found)
    Returns:
        Node or None: If found, the joint with the matching UUID, otherwise None
    """
    joint = core_uuid.get_object_from_uuid_attr(
        uuid_string=uuid_string, attr_name=tools_rig_const.RiggerConstants.ATTR_JOINT_UUID, obj_type="joint"
    )
    if joint:
        return core_node.Node(joint)


def find_driver_from_uuid(uuid_string):
    """
    Return a transform if the provided UUID matches the value of the attribute
    tools_rig_const.RiggerConstants.DRIVER_ATTR_UUID
    Args:
        uuid_string (str): UUID to look for (if it matches, then the driver is found)
    Returns:
        Node or None: If found, the joint with the matching UUID, otherwise None
    """
    driver = core_uuid.get_object_from_uuid_attr(
        uuid_string=uuid_string, attr_name=tools_rig_const.RiggerConstants.ATTR_DRIVER_UUID, obj_type="transform"
    )
    if driver:
        return core_node.Node(driver)


def find_drivers_from_joint(source_joint, as_list=False, create_missing_generic=False, skip_block_drivers=False):
    """
    Finds drivers according to the data described in the joint attributes.
    It's expected that the joint has this data available as string attributes.
    Args:
        source_joint (str, Node): The path to a joint. It's expected that this joint contains the drivers attribute.
        as_list (bool, optional): If True, it will return a list of Node objects.
                                  If False, a dictionary where the key is the driver name and the value its path (Node)
        create_missing_generic (bool, optional): If the driver is of the type generic, but no driver transform
                                                is found in the scene, a new transform is created to be used as generic.
                                                If no drivers are detected, then a generic driver is created and
                                                plugged populated in the "source_joint".
        skip_block_drivers (bool, optional): If True, when a block driver is detected an empty result becomes the
                                             result instead of the actual drivers. Useful for when creating the logic
                                             that blocks creation of control drivers.
    Returns:
        dict or list: A dictionary where the key is the driver name and the value its path (Node)
                      If "as_list" is True, then a list of Nodes containing the path to the drivers is returned.
    """
    driver_uuids = get_driver_uuids_from_joint(source_joint=source_joint, as_list=False)
    # Block lookup for None drivers
    if tools_rig_const.RiggerDriverTypes.BLOCK in driver_uuids.keys() and skip_block_drivers:
        return [] if as_list else {}
    found_drivers = {}
    # Handle listed drivers
    for index, (driver, uuid) in enumerate(driver_uuids.items()):
        _found_driver = find_driver_from_uuid(uuid_string=uuid)
        # If generic driver is the first option, but transform is missing, generate one that follows the parent joint
        if driver == tools_rig_const.RiggerDriverTypes.GENERIC and create_missing_generic and not _found_driver:
            _found_driver = get_generic_driver(source_joint=source_joint)
        if _found_driver:
            found_drivers[driver] = _found_driver
    # Handle empty driver list
    if cmds.objExists(source_joint) and not driver_uuids and create_missing_generic:
        _found_driver = get_generic_driver(source_joint=source_joint, add_missing_driver=True)
        if _found_driver:
            found_drivers[tools_rig_const.RiggerDriverTypes.GENERIC] = _found_driver
    # Convert to list
    if as_list:
        return list(found_drivers.values())
    return found_drivers


def find_object_with_attr(attr_name, obj_type="transform", transform_lookup=True, lookup_list=None):
    """
    Return object if provided UUID is present in it
    Args:
        attr_name (str): Name of the attribute where the UUID is stored.
        obj_type (str, optional): Type of objects to look for (default is "transform") - Used for optimization
        transform_lookup (bool, optional): When not a transform, it checks the item parent instead of the item itself.
        lookup_list (list, optional): If provided, this list will be used instead of a full "ls" type query.
                                      This can be used to improve performance in case the element was already
                                      previously listed in another operation. List should use full paths.
                                      e.g. ["|itemOne", "|transform|itemTwo"]

    Returns:
        Node or None: If found, the object with a matching UUID, otherwise None
    """
    if isinstance(lookup_list, list):
        obj_list = lookup_list
    else:
        obj_list = cmds.ls(typ=obj_type, long=True) or []
    for obj in obj_list:
        if transform_lookup and obj_type != "transform":
            _parent = cmds.listRelatives(obj, parent=True, fullPath=True) or []
            if _parent:
                obj = _parent[0]
        if cmds.objExists(f"{obj}.{attr_name}"):
            return core_node.Node(obj)


def find_root_group_proxy():
    """
    Looks for the proxy root transform (group) by searching for objects containing the expected lookup attribute.
    Not to be confused with the root curve. This is the parent TRANSFORM.
    Returns:
        Node or None: The existing root group (top proxy parent), otherwise None.
    """
    return find_object_with_attr(tools_rig_const.RiggerConstants.REF_ATTR_ROOT_PROXY, obj_type="transform")


def find_root_group_rig():
    """
    Looks for the rig root transform (group) by searching for objects containing the expected lookup attribute.
    Not to be confused with the root control curve. This is the parent TRANSFORM.
    Returns:
        Node or None: The existing rig group (top rig parent), otherwise None.
    """
    return find_object_with_attr(tools_rig_const.RiggerConstants.REF_ATTR_ROOT_RIG, obj_type="transform")


def find_ctrl_global(use_transform=False):
    """
    Looks for the control root/global curve by searching for objects containing the expected lookup attribute.
    Args:
        use_transform (bool, optional): If active, it will use the type transform to look for the object.
                                        This can potentially make the operation less efficient, but will
                                        run a more complete search as it will include curves that had
                                        their shapes deleted.
    Returns:
        Node or None: The existing control root curve (a.k.a. main control), otherwise None.
    """
    obj_type = "nurbsCurve"
    if use_transform:
        obj_type = "transform"
    return find_object_with_attr(tools_rig_const.RiggerConstants.REF_ATTR_CTRL_GLOBAL, obj_type=obj_type)


def find_ctrl_global_offset(use_transform=False):
    """
    Looks for the direction curve by searching for objects containing the expected lookup attribute.
    Args:
        use_transform (bool, optional): If active, it will use the type transform to look for the object.
                                        This can potentially make the operation less efficient, but will
                                        run a more complete search as it will include curves that had
                                        their shapes deleted.
    Returns:
        Node or None: The existing direction curve, otherwise None.
    """
    obj_type = "nurbsCurve"
    if use_transform:
        obj_type = "transform"
    return find_object_with_attr(tools_rig_const.RiggerConstants.REF_ATTR_CTRL_GLOBAL_OFFSET, obj_type=obj_type)


def find_ctrl_global_proxy(use_transform=False):
    """
    Looks for the proxy global/root curve by searching for objects containing the expected attribute.
    Args:
        use_transform (bool, optional): If active, it will use the type transform to look for the object.
                                        This can potentially make the operation less efficient, but will
                                        run a more complete search as it will include curves that had
                                        their shapes deleted.
    Returns:
        Node or None: The existing proxy root curve, otherwise None.
    """
    obj_type = "nurbsCurve"
    if use_transform:
        obj_type = "transform"
    return find_object_with_attr(tools_rig_const.RiggerConstants.REF_ATTR_CTRL_GLOBAL_PROXY, obj_type=obj_type)


def find_skeleton_group():
    """
    Looks for the rig skeleton group (transform) by searching for objects containing the expected attribute.
    Returns:
        Node or None: The existing skeleton group, otherwise None.
    """
    return find_object_with_attr(tools_rig_const.RiggerConstants.REF_ATTR_SKELETON, obj_type="transform")


def find_setup_group():
    """
    Looks for the rig setup group (transform) by searching for objects containing the expected attribute.
    Returns:
        Node or None: The existing setup group, otherwise None.
    """
    return find_object_with_attr(tools_rig_const.RiggerConstants.REF_ATTR_SETUP, obj_type="transform")


def find_vis_lines_from_uuid(parent_uuid=None, child_uuid=None):
    """
    Looks for a visualization line containing the parent or the child uuid.
    Args:
        parent_uuid (str, optional): The UUID of the parent proxy.
        child_uuid (str, optional): The UUID of the child proxy.
    Returns:
        tuple: A tuple of detected lines containing the requested parent or child uuids. Empty tuple otherwise.
    """
    # Try the group first to save time.
    lines_grp = find_object_with_attr(attr_name=tools_rig_const.RiggerConstants.REF_ATTR_LINES)
    _lines = set()
    if lines_grp:
        _children = cmds.listRelatives(str(lines_grp), children=True, fullPath=True) or []
        for child in _children:
            if not cmds.objExists(f"{child}.{tools_rig_const.RiggerConstants.ATTR_LINE_PARENT_UUID}"):
                continue
            if parent_uuid:
                existing_uuid = cmds.getAttr(f"{child}.{tools_rig_const.RiggerConstants.ATTR_LINE_PARENT_UUID}")
                if existing_uuid == parent_uuid:
                    _lines.add(core_node.Node(child))
            if child_uuid:
                existing_uuid = cmds.getAttr(f"{child}.{tools_rig_const.RiggerConstants.ATTR_LINE_CHILD_UUID}")
                if existing_uuid == child_uuid:
                    _lines.add(core_node.Node(child))
    if _lines:
        return tuple(_lines)
    # If nothing was found, look through all transforms - Less optimized
    obj_list = cmds.ls(typ="nurbsCurve", long=True) or []
    valid_items = set()
    for obj in obj_list:
        _parent = cmds.listRelatives(obj, parent=True, fullPath=True) or []
        if _parent:
            obj = _parent[0]
        if cmds.objExists(f"{obj}.{tools_rig_const.RiggerConstants.ATTR_LINE_PARENT_UUID}"):
            valid_items.add(core_node.Node(obj))
    for item in valid_items:
        if parent_uuid:
            existing_uuid = cmds.getAttr(f"{item}.{tools_rig_const.RiggerConstants.ATTR_LINE_PARENT_UUID}")
            if existing_uuid == parent_uuid:
                _lines.add(core_node.Node(child))
        if child_uuid:
            existing_uuid = cmds.getAttr(f"{item}.{tools_rig_const.RiggerConstants.ATTR_LINE_CHILD_UUID}")
            if existing_uuid == child_uuid:
                _lines.add(core_node.Node(child))
    return tuple(_lines)


def find_or_create_joint_automation_group():
    """
    Use the "find_or_create_automation_group" function to get the joint automation group.
    This is a group where extra joints used for automation (not skinning) are stored.
    Returns:
        str: Path to the automation group (or subgroup)
    """
    return get_automation_group(name="jointAutomation", rgb_color=core_color.ColorConstants.RigOutliner.GRP_SKELETON)


def find_drivers_from_module(module_uuid, filter_driver_type=None, filter_driver_purpose=None):
    """
    Finds all drivers belonging to a module.
    Args:
        module_uuid (str, ModuleGeneric): The UUID to use when filtering all existing drivers.
        filter_driver_type (str, optional): If provided, only drivers of this type are returned.
        filter_driver_purpose (str, optional): If provided, only drivers of this purpose are returned.
    Returns:
        list: A list of Nodes, each one is a driver belonging to the module uuid provided as argument.
    """
    from gt.tools.auto_rigger.rig_framework import ModuleGeneric

    if module_uuid and isinstance(module_uuid, ModuleGeneric):
        module_uuid = module_uuid.get_uuid()
    module_drivers = []
    transforms = cmds.ls(typ="transform", long=True) or []
    for obj in transforms:
        attr_path = f"{obj}.{tools_rig_const.RiggerConstants.ATTR_DRIVER_UUID}"
        if cmds.objExists(attr_path):
            attr_value = core_attr.get_attr(attribute_path=attr_path)
            if not attr_value:
                continue  # Missing UUID driver data, skip it
            if filter_driver_type and isinstance(filter_driver_type, str):
                # Check if it has valid content
                if len(str(attr_value).split("-")) == 3 and str(attr_value).split("-")[1] != filter_driver_type:
                    continue  # Not of the desired type, skip it
            if filter_driver_purpose and isinstance(filter_driver_purpose, str):
                # Check if it has valid content
                if len(str(attr_value).split("-")) == 3 and str(attr_value).split("-")[2] != filter_driver_purpose:
                    continue  # Not of the desired purpose, skip it
            if attr_value.startswith(module_uuid):
                module_drivers.append(core_node.Node(obj))
    # Find Supporting Drivers
    for driver in module_drivers:
        if not cmds.objExists(f"{driver}.{tools_rig_const.RiggerConstants.ATTR_DRIVER_UUID}"):
            continue
        supporting_drivers = get_supporting_drivers(source_driver=driver)
        if supporting_drivers:
            module_drivers.extend(supporting_drivers)
    return module_drivers


# ------------------------------------------ Create functions ------------------------------------------
def create_proxy_visualization_lines(proxy_list, lines_parent=None):
    """
    Creates visualization lines according to the proxy UUID parent attribute.
    If a proxy meta parent is found, this is used instead.
    Args:
        proxy_list (list): A list of Proxy objects to be parented.
                           UUID and parent UUID fields are required for the operation.
                           Objects without it will be ignored.
        lines_parent (str, optional): If provided, it will automatically parent all generated elements to this object.
                                      Must exist and allow objects to be parented to it. e.g. "pSphere1"
    Returns:
        list: List of tuples. Every tuple carries a list of generated elements.
              e.g. [('second_to_first', 'second_cluster', 'first_cluster')]
    """
    _lines = []
    for proxy in proxy_list:
        built_proxy = find_proxy_from_uuid(proxy.get_uuid())
        parent_proxy = find_proxy_from_uuid(proxy.get_parent_uuid())

        # Check for Meta Parent - OVERWRITES parent!
        metadata = proxy.get_metadata()
        if metadata:
            line_parent = metadata.get(tools_rig_const.RiggerConstants.META_PROXY_LINE_PARENT, None)
            if line_parent:
                parent_proxy = find_proxy_from_uuid(line_parent)

        # Create Line
        if built_proxy and parent_proxy and cmds.objExists(built_proxy) and cmds.objExists(parent_proxy):
            try:
                line_objects = core_curve.create_connection_line(object_a=built_proxy, object_b=parent_proxy) or []
                if lines_parent and cmds.objExists(lines_parent):
                    core_hrchy.parent(source_objects=line_objects, target_parent=lines_parent) or []
                if line_objects:
                    line_crv = line_objects[0]
                    core_attr.add_attr(
                        obj_list=line_crv,
                        attributes=tools_rig_const.RiggerConstants.ATTR_LINE_CHILD_UUID,
                        attr_type="string",
                    )
                    core_attr.set_attr(
                        attribute_path=f"{line_crv}.{tools_rig_const.RiggerConstants.ATTR_LINE_CHILD_UUID}",
                        value=proxy.get_uuid(),
                    )
                    core_attr.add_attr(
                        obj_list=line_crv,
                        attributes=tools_rig_const.RiggerConstants.ATTR_LINE_PARENT_UUID,
                        attr_type="string",
                    )
                    core_attr.set_attr(
                        attribute_path=f"{line_crv}.{tools_rig_const.RiggerConstants.ATTR_LINE_PARENT_UUID}",
                        value=proxy.get_parent_uuid(),
                    )
                _lines.append(line_objects)
            except Exception as e:
                logger.debug(f"Failed to create visualization line. Issue: {str(e)}")
    return _lines


def create_ctrl_rig_global(name=f"global_{core_naming.NamingConstants.Suffix.CTRL}"):
    """
    Creates a circle/arrow curve to be used as the root/global of a control rig or a proxy guide
    Args:
        name (str, optional): Name of the curve transform
    Returns:
        Node, str: A Node containing the generated root curve
    """
    selection = cmds.ls(selection=True)
    ctrl_crv = core_curve.get_curve("_rig_root")
    ctrl_crv.set_name(name=name)
    ctrl_transform = ctrl_crv.build()
    core_attr.connect_attr(
        source_attr=f"{ctrl_transform}.sy", target_attr_list=[f"{ctrl_transform}.sx", f"{ctrl_transform}.sz"]
    )
    core_attr.set_attr_state(obj_list=ctrl_transform, attr_list=["sx", "sz"], hidden=True)
    core_color.set_color_viewport(obj_list=ctrl_transform, rgb_color=core_color.ColorConstants.RigProxy.CENTER)
    cmds.select(clear=True)
    if selection:
        try:
            cmds.select(selection=True)
        except Exception as e:
            logger.debug(f"Unable to restore initial selection. Issue: {str(e)}")
    return core_node.Node(ctrl_transform)


def create_root_group(is_proxy=False):
    """
    Creates a group to be used as the root of the current setup (rig or proxy)
    Args:
        is_proxy (bool, optional): If True, it will create the proxy group, instead of the main rig group
    Returns:
        Node: A Node describing the path to the created root group.
    """
    _name = tools_rig_const.RiggerConstants.GRP_RIG_NAME
    _attr = tools_rig_const.RiggerConstants.REF_ATTR_ROOT_RIG
    _color = core_color.ColorConstants.RigOutliner.GRP_ROOT_RIG
    if is_proxy:
        _name = tools_rig_const.RiggerConstants.GRP_PROXY_NAME
        _attr = tools_rig_const.RiggerConstants.REF_ATTR_ROOT_PROXY
        _color = core_color.ColorConstants.RigOutliner.GRP_ROOT_PROXY
    root_group = cmds.group(name=_name, empty=True, world=True)
    root_group = core_node.Node(root_group)
    core_attr.hide_lock_default_attrs(obj_list=root_group, translate=True, rotate=True, scale=True)
    core_attr.add_attr(obj_list=root_group, attr_type="string", is_keyable=False, attributes=_attr, verbose=True)
    core_color.set_color_outliner(root_group, rgb_color=_color)
    return root_group


def create_ctrl_proxy_global(prefix=core_naming.NamingConstants.Prefix.CENTER):
    """
    Creates a curve to be used as the root of a proxy skeleton
    Args:
        prefix (str, optional): Prefix to be added to the control.
                                Default is the center prefix according to core naming module.
    Returns:
        Node, str: A Node containing the generated root curve
    """
    root_transform = create_ctrl_rig_global(name=f"{prefix}_globalProxy")
    core_attr.hide_lock_default_attrs(obj_list=root_transform, translate=True, rotate=True)

    core_attr.add_separator_attr(
        target_object=root_transform,
        attr_name=f"proxy{core_str.upper_first_char(core_rigging.RiggingConstants.SEPARATOR_CONTROL)}",
    )
    core_attr.add_attr(
        obj_list=root_transform,
        attr_type="string",
        is_keyable=False,
        attributes=tools_rig_const.RiggerConstants.REF_ATTR_CTRL_GLOBAL_PROXY,
        verbose=True,
    )

    core_curve.set_curve_width(obj_list=root_transform, line_width=2)
    return core_node.Node(root_transform)


def create_ctrl_default(name, curve_file_name=None, outliner_color=core_color.ColorConstants.RigOutliner.CTRL):
    """
    Creates a curve to be used as control within the auto rigger context.
    Args:
        name (str): Control name.
        curve_file_name (str, optional): Curve file name (from inside "gt/core/data/curves") e.g. "circle"
        outliner_color (str, None, optional): Outliner color used for the created control. Set to None to skip it.
    Returns:
        Node or None: Node with the generated control, otherwise None
    """
    if not curve_file_name:
        curve_file_name = "_cube"
    crv_obj = core_curve.get_curve(file_name=curve_file_name)
    crv_obj.set_name(name)
    crv = crv_obj.build()
    if crv:
        if outliner_color:
            core_color.set_color_outliner(crv, rgb_color=core_color.ColorConstants.RigOutliner.CTRL)
        return core_node.Node(crv)


def create_ctrl_global(prefix=core_naming.NamingConstants.Prefix.CENTER):
    """
    Creates a curve to be used as the root of a control rig skeleton
    Args:
        prefix (str, optional): Prefix to be added to the control.
                                Default is the center prefix according to core naming module.
    Returns:
        Node, str: A Node containing the generated root curve
    """
    global_trans = create_ctrl_rig_global(name=f"{prefix}_global_{core_naming.NamingConstants.Suffix.CTRL}")
    core_attr.add_separator_attr(
        target_object=global_trans,
        attr_name=f"rig{core_str.upper_first_char(core_rigging.RiggingConstants.SEPARATOR_CONTROL)}",
    )
    core_attr.add_attr(
        obj_list=global_trans,
        attr_type="string",
        is_keyable=False,
        attributes=tools_rig_const.RiggerConstants.REF_ATTR_CTRL_GLOBAL,
        verbose=True,
    )
    core_curve.set_curve_width(obj_list=global_trans, line_width=3)
    core_color.set_color_outliner(global_trans, rgb_color=core_color.ColorConstants.RigOutliner.CTRL)
    core_color.set_color_viewport(obj_list=global_trans, rgb_color=core_color.ColorConstants.RigControl.ROOT)
    return core_node.Node(global_trans)


def create_ctrl_global_offset(prefix=core_naming.NamingConstants.Prefix.CENTER):
    """
    Creates a curve to be used as the offset of the root/global control of a rig skeleton
    Returns:
        Node, str: A Node containing the generated root curve
    """
    global_offset_trans = cmds.circle(
        name=f"{prefix}_globalOffset_{core_naming.NamingConstants.Suffix.CTRL}", normal=(0, 1, 0), ch=False, radius=44.5
    )[0]
    cmds.rebuildCurve(global_offset_trans, ch=False, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s=20, d=3, tol=0.01)
    core_attr.add_separator_attr(
        target_object=global_offset_trans,
        attr_name=f"rig{core_str.upper_first_char(core_rigging.RiggingConstants.SEPARATOR_CONTROL)}",
    )
    core_rigging.expose_rotation_order(global_offset_trans)
    core_attr.add_attr(
        obj_list=global_offset_trans,
        attr_type="string",
        is_keyable=False,
        attributes=tools_rig_const.RiggerConstants.REF_ATTR_CTRL_GLOBAL_OFFSET,
        verbose=True,
    )
    core_attr.hide_lock_default_attrs(global_offset_trans, scale=True, visibility=True)
    core_color.set_color_outliner(global_offset_trans, rgb_color=core_color.ColorConstants.RigOutliner.CTRL)
    core_color.set_color_viewport(obj_list=global_offset_trans, rgb_color=core_color.ColorConstants.RigControl.CENTER)
    return core_node.Node(global_offset_trans)


def create_utility_groups(geometry=False, skeleton=False, control=False, setup=False, line=False, target_parent=None):
    """
    Creates category groups for the rig.
    This group holds invisible rigging elements used in the automation of the project.
    Args:
        geometry (bool, optional): If True, the geometry group is created.
        skeleton (bool, optional): If True, the skeleton group is created.
        control (bool, optional): If True, the control group is created.
        setup (bool, optional): If True, the setup group is created.
        line (bool, optional): If True, the visualization line group gets created.
        target_parent (str, Node, optional): If provided, groups will be parented to this object after creation.
    Returns:
        dict: A dictionary with lookup attributes (tools_rig_const.RiggerConstants)
        as keys and "Node" objects as values.
              e.g. {tools_rig_const.RiggerConstants.REF_GEOMETRY_ATTR: core_node.Node("group_name")}
    """
    desired_groups = {}
    if geometry:
        _name = tools_rig_const.RiggerConstants.GRP_GEOMETRY_NAME
        _color = core_color.ColorConstants.RigOutliner.GRP_GEOMETRY
        desired_groups[tools_rig_const.RiggerConstants.REF_ATTR_GEOMETRY] = (_name, _color)
    if skeleton:
        _name = tools_rig_const.RiggerConstants.GRP_SKELETON_NAME
        _color = core_color.ColorConstants.RigOutliner.GRP_SKELETON
        desired_groups[tools_rig_const.RiggerConstants.REF_ATTR_SKELETON] = (_name, _color)
    if control:
        _name = tools_rig_const.RiggerConstants.GRP_CONTROL_NAME
        _color = core_color.ColorConstants.RigOutliner.GRP_CONTROL
        desired_groups[tools_rig_const.RiggerConstants.REF_ATTR_CONTROL] = (_name, _color)
    if setup:
        _name = tools_rig_const.RiggerConstants.GRP_SETUP_NAME
        _color = core_color.ColorConstants.RigOutliner.GRP_SETUP
        desired_groups[tools_rig_const.RiggerConstants.REF_ATTR_SETUP] = (_name, _color)
    if line:
        _name = tools_rig_const.RiggerConstants.GRP_LINE_NAME
        _color = None
        desired_groups[tools_rig_const.RiggerConstants.REF_ATTR_LINES] = (_name, _color)

    group_dict = {}
    for attr, (name, color) in desired_groups.items():
        group = cmds.group(name=name, empty=True, world=True)
        core_attr.add_attr(obj_list=group, attr_type="string", is_keyable=False, attributes=attr, verbose=True)
        _node = core_node.Node(group)
        group_dict[attr] = _node
        if color:
            core_color.set_color_outliner(str(_node), rgb_color=color)
        if target_parent:
            core_hrchy.parent(source_objects=_node, target_parent=str(target_parent))
    return group_dict


# ------------------------------------------ Misc functions ------------------------------------------
def parent_proxies(proxy_list):
    """
    Parent proxy elements (and their offset groups) according to their parent UUID
    Args:
        proxy_list (list): A list of Proxy objects to be parented.
                           UUID and parent UUID fields are required for the operation.
                           Objects without it will be ignored.
    """
    # Parent Joints
    for proxy in proxy_list:
        built_proxy = find_proxy_from_uuid(proxy.get_uuid())
        parent_proxy = find_proxy_from_uuid(proxy.get_parent_uuid())
        if built_proxy and parent_proxy and cmds.objExists(built_proxy) and cmds.objExists(parent_proxy):
            offset = cmds.listRelatives(built_proxy, parent=True, fullPath=True)
            if offset:
                core_hrchy.parent(source_objects=offset, target_parent=parent_proxy)


def get_proxy_offset(proxy_name):
    """
    Return the offset transform (parent) of the provided proxy object. If not found, it returns "None"
    Args:
        proxy_name (str): Name of the attribute where the UUID is stored.
    Returns:
        str, None: If found, the offset object (parent of the proxy), otherwise None
    """
    if not proxy_name or not cmds.objExists(proxy_name):
        logger.debug(f'Unable to find offset for "{str(proxy_name)}".')
        return
    offset_list = cmds.listRelatives(proxy_name, parent=True, typ="transform", fullPath=True) or []
    for offset in offset_list:
        return offset


def get_meta_purpose_from_dict(metadata_dict):
    """
    Gets the meta type of the proxy. A meta type helps identify the purpose of a proxy within a module.
    For example, a type "knee" proxy describes that it will be influenced by the "hip" and "ankle" in a leg.
    This can also be seen as "pointers" to the correct proxy when receiving data from a dictionary.
    Args:
        metadata_dict (dict, None): A dictionary describing a proxy metadata.
    Returns:
        string or None: The meta type string or None when not detected/found.
    """
    if metadata_dict:
        meta_type = metadata_dict.get(tools_rig_const.RiggerConstants.META_PROXY_PURPOSE)
        return meta_type


def get_automation_group(
    name=f"generalAutomation",
    subgroup=None,
    rgb_color=core_color.ColorConstants.RigOutliner.AUTOMATION,
):
    """
    Gets the path to an automation group (or subgroup) or create it in case it can't be found.
    Automation groups are found inside the "setup_grp" found using "find_setup_group"
    Args:
        name (str, optional): Name of the automation group (found inside the "setup_grp")
        subgroup (str, optional): If provided, this subgroup should exist inside the base automation group.
        rgb_color (tuple, optional): A tuple with three integers/floats describing a color (RGB).
    Returns:
        Node, str: Path to the automation group (or subgroup) - Node format has string as its base.
    Example:
        output_a = find_or_create_automation_group(name="generalAutomation_grp")
        print(output_a)  # |rig_grp|setup_grp|generalAutomation_grp
        output_b = find_or_create_automation_group(name="generalAutomation_grp", subgroup="baseConstraints_grp")
        print(output_b)  # |rig_grp|setup_grp|generalAutomation_grp|baseConstraints_grp
    """
    selection = cmds.ls(selection=True)
    setup_grp = find_setup_group()
    _grp_path = f"{setup_grp}|{str(name)}"
    # Find or create automation group (base)
    if name and cmds.objExists(_grp_path):
        _grp_path = core_node.Node(_grp_path)
    else:
        _grp_path = cmds.group(name=name, empty=True, world=True)
        _grp_path = core_node.Node(_grp_path)
        core_color.set_color_outliner(obj_list=_grp_path, rgb_color=rgb_color)
        core_hrchy.parent(source_objects=_grp_path, target_parent=setup_grp)
        if not setup_grp:
            logger.debug(f'Automation group "{str(name)}" could not be properly parented. ' f"Missing setup group.")
    # Find or create automation subgroup (child of the base)
    if subgroup and isinstance(subgroup, str):
        _grp_path_base = _grp_path  # Store base for re-parenting
        _grp_path = f"{_grp_path}|{str(subgroup)}"
        if name and cmds.objExists(_grp_path):
            _grp_path = _grp_path
        else:
            _grp_path = cmds.group(name=subgroup, empty=True, world=True)
            _grp_path = core_node.Node(_grp_path)
            core_hrchy.parent(source_objects=_grp_path, target_parent=_grp_path_base)
            if not setup_grp:
                logger.debug(f'Automation group "{str(name)}" could not be properly parented. ' f"Missing setup group.")
    cmds.select(clear=True)
    if selection:
        try:
            cmds.select(selection=True)
        except Exception as e:
            logger.debug(f"Unable to restore initial selection. Issue: {str(e)}")
    return _grp_path


def get_driven_joint(uuid_string, suffix=core_naming.NamingConstants.Suffix.DRIVEN, constraint_to_source=True):
    """
    Gets the path to a driven joint or create it in case it's missing.
    Driven joints are used to control automation joints or joint hierarchies.
    Args:
        uuid_string (str): UUID str stored in "tools_rig_const.RiggerConstants.JOINT_ATTR_DRIVEN_UUID" used to identify.
        suffix (str, optional): Suffix to add to the newly created driven joint. Default is "driven".
        constraint_to_source (bool, optional): Parent constraint the joint to its source during creation.
                                               Does nothing if driver already exists and is found.
    Returns:
        Node, str: Path to the FK Driver - Node format has string as its base.

    """
    driven_jnt = core_uuid.get_object_from_uuid_attr(
        uuid_string=uuid_string, attr_name=tools_rig_const.RiggerConstants.ATTR_JOINT_DRIVEN_UUID, obj_type="joint"
    )
    if not driven_jnt:
        source_jnt = find_joint_from_uuid(uuid_string)
        if not source_jnt:
            return
        driven_jnt = core_rigging.duplicate_joint_for_automation(joint=source_jnt, suffix=suffix)
        core_attr.delete_user_defined_attrs(obj_list=driven_jnt)
        core_attr.add_attr(
            obj_list=driven_jnt, attr_type="string", attributes=tools_rig_const.RiggerConstants.ATTR_JOINT_DRIVEN_UUID
        )
        core_attr.set_attr(
            attribute_path=f"{driven_jnt}.{tools_rig_const.RiggerConstants.ATTR_JOINT_DRIVEN_UUID}", value=uuid_string
        )
        if constraint_to_source:
            constraint = cmds.parentConstraint(source_jnt, driven_jnt)
            cmds.setAttr(f"{constraint[0]}.interpType", 0)  # Set to No Flip
    return driven_jnt


def get_drivers_list_from_joint(source_joint):
    """
    Gets the list of drivers that are stored in a joint drivers attribute.
    If missing the attribute, it will return an empty list.
    If the string data stored in the attribute is corrupted, it will return an empty list.
    """
    drivers = core_attr.get_attr(obj_name=source_joint, attr_name=tools_rig_const.RiggerConstants.ATTR_JOINT_DRIVERS)
    if drivers:
        try:
            drivers = eval(drivers)
            if not isinstance(drivers, list):
                logger.debug("Stored value was not a list.")
                drivers = None
        except Exception as e:
            logger.debug(f"Unable to read joint drivers data. Values will be overwritten. Issue: {e}")
            drivers = None
    if not drivers:
        return []
    return drivers


def add_driver_to_joint(target_joint, new_drivers):
    """
    Adds a new driver to the driver list of the target joint.
    The list is stored inside the drivers attribute of the joint.
    If the expected "joint drivers" attribute is not found, the operation is ignored.
    Args:
        target_joint (str, Node): The path to a joint. It's expected that this joint contains the drivers attribute.
        new_drivers (str, list): A new driver to be added to the drivers list. e.g. "fk". (Can be a list of drivers)
                                 This will only be added to the list and will not overwrite the existing items.
                                 The operation is ignored in case the item is already part of the list.
    """
    if isinstance(new_drivers, str):
        new_drivers = [new_drivers]
    drivers = get_drivers_list_from_joint(source_joint=target_joint)
    for new_driver in new_drivers:
        if new_driver not in drivers:
            drivers.append(new_driver)
    data = json.dumps(drivers)
    core_attr.set_attr(obj_list=target_joint, attr_list=tools_rig_const.RiggerConstants.ATTR_JOINT_DRIVERS, value=data)


def get_driver_uuids_from_joint(source_joint, as_list=False):
    """
    Gets a dictionary or list of drivers uuids from joint.
    It's expected that the joint has this data available as string attributes.
    Args:
        source_joint (str, Node): The path to a joint. It's expected that this joint contains the drivers attribute.
        as_list (bool, optional): If True, it will return a list of uuids. if False, the standard dictionary.
    Returns:
        dict or list: A dictionary where the key is the driver name and the value its uuid, or a list of uuids.
    """
    driver_uuids = {}
    if source_joint and cmds.objExists(source_joint):
        drivers = get_drivers_list_from_joint(source_joint=source_joint)
        module_uuid = core_attr.get_attr(
            obj_name=source_joint, attr_name=tools_rig_const.RiggerConstants.ATTR_MODULE_UUID
        )
        joint_purpose = core_attr.get_attr(
            obj_name=source_joint, attr_name=tools_rig_const.RiggerConstants.ATTR_JOINT_PURPOSE
        )
        for driver in drivers:
            _driver_uuid = f"{module_uuid}-{driver}"
            if joint_purpose:
                _driver_uuid = f"{_driver_uuid}-{joint_purpose}"
            driver_uuids[driver] = _driver_uuid
    if as_list:
        return list(driver_uuids.values())
    return driver_uuids


def get_generic_driver(source_joint, add_missing_driver=False):
    """
    Gets the generic driver if it exists, or creates one if it doesn't exist.
    Args:
        source_joint (str, Node): The path to a joint. It's expected that this joint contains the drivers attribute.
        add_missing_driver (bool, optional): If active, it will add a generic module before creating a generic
                                             transform/driver that follows the source joint.
    Returns:
        Node, str: the created or found generic driver.
    """
    driver_uuids = get_driver_uuids_from_joint(source_joint=source_joint, as_list=False)
    if tools_rig_const.RiggerDriverTypes.GENERIC in driver_uuids.keys():  # Is Generic Driver available?
        driver_uuid = driver_uuids.get(tools_rig_const.RiggerDriverTypes.GENERIC)
        driver = core_uuid.get_object_from_uuid_attr(
            uuid_string=driver_uuid, attr_name=tools_rig_const.RiggerConstants.ATTR_DRIVER_UUID, obj_type="transform"
        )
        if driver:
            return driver
        # Driver not found, create one
        purpose = core_attr.get_attr(
            obj_name=source_joint, attr_name=tools_rig_const.RiggerConstants.ATTR_JOINT_PURPOSE
        )
        module_uuid = core_attr.get_attr(
            obj_name=source_joint, attr_name=tools_rig_const.RiggerConstants.ATTR_MODULE_UUID
        )
        # Driven Group (For Parented Controls)
        driver = core_hrchy.create_group(
            name=f"{core_naming.get_short_name(source_joint)}_{core_naming.NamingConstants.Suffix.DRIVER}"
        )
        add_driver_uuid_attr(
            target_driver=driver,
            module_uuid=module_uuid,
            driver_type=tools_rig_const.RiggerDriverTypes.GENERIC,
            proxy_purpose=purpose,
        )
        core_cnstr.constraint_targets(source_driver=source_joint, target_driven=driver, maintain_offset=False)
        direction_ctrl = find_ctrl_global_offset()
        if direction_ctrl:
            core_hrchy.parent(source_objects=driver, target_parent=direction_ctrl)
        return driver
    else:
        if add_missing_driver:
            add_driver_to_joint(target_joint=source_joint, new_drivers=tools_rig_const.RiggerDriverTypes.GENERIC)
            return get_generic_driver(source_joint=source_joint, add_missing_driver=False)


def add_driver_uuid_attr(target_driver, module_uuid, driver_type=None, proxy_purpose=None):
    """
    Adds an attributes to be used as driver UUID to the target object. (Target object is the driver/control)
    The value of the attribute is created using the module uuid, the driver type and proxy purpose combined.
    Following this pattern: "<module_uuid>-<driver_type>-<proxy_purpose>" e.g. "abcdef123456-fk-shoulder"
    Args:
        target_driver (str, Node): Path to the object that will receive the driver attributes. e.g. Driver/Control
        module_uuid (str): UUID for the module. This is used to determine the driver UUID value.
        driver_type (str, optional): A string or tag use to identify the control type. e.g. "fk", "ik", "offset"
                                     If not provided, it's assumed to be a generic driver. "RiggerDriverTypes.GENERIC"
        proxy_purpose (str, Proxy, optional): This is the proxy purpose. It can be a string, or the Proxy object.
                                        e.g. "shoulder" or the shoulder proxy object. If a Proxy object is provided,
                                        then the function tries to extract the meta "purpose" value from it.
                                        If not present or not provided, this portion of the data becomes "unknown".
    Returns:
        str: target UUID value created by the operation.
             Pattern: "<module_uuid>-<driver_type>-<proxy_purpose>" e.g. "abcdef123456-fk-shoulder"
    """
    if not module_uuid or not isinstance(module_uuid, str):
        logger.warning(f"Unable to add UUID attribute. Module UUID is missing.")
        return
    uuid = f"{module_uuid}"
    # Add Driver Type
    if not driver_type:
        driver_type = "unknown"  # Unknown driver / Missing
    uuid = f"{uuid}-{driver_type}"
    # Add Purpose
    if proxy_purpose and isinstance(proxy_purpose, tools_rig_frm.Proxy):
        proxy_purpose = proxy_purpose.get_meta_purpose()
    if not proxy_purpose:
        proxy_purpose = "unknown"  # Unknown purpose / Missing
    uuid = f"{uuid}-{proxy_purpose}"
    # Add Attribute and Set Value
    if not target_driver or not cmds.objExists(target_driver):
        logger.warning(f"Unable to add UUID attribute. Target object is missing.")
        return
    uuid_attr = core_attr.add_attr(
        obj_list=target_driver,
        attr_type="string",
        is_keyable=False,
        attributes=tools_rig_const.RiggerConstants.ATTR_DRIVER_UUID,
        verbose=True,
    )[0]
    core_attr.set_attr(attribute_path=uuid_attr, value=str(uuid))
    return uuid


def connect_supporting_driver(source_parent_driver, target_child_driver):
    """
    Connects a driver that already has a driverUUID defined to a dependant auxiliary/supporting driver (child).
    This allows for a control to have multiple child drivers without requiring extra driver types for each one of them.

    Connection: <source_driver.driverUUID> -> <target_offset.driverChild>
    e.g. "cog_ctrl.driverUUID" -> "cog_offset_ctrl.driverChild"

    Args:
        source_parent_driver (str, Node): Driver (often controls) with already populated driverUUID attribute. (parent)
        target_child_driver (str, Node): Auxiliary control attr that receives data from "ATTR_DRIVER_PARENT". (child)
    Returns:
        list: List of created attributes. e.g. 'cog_offset_ctrl.driverChild'
    """
    if not source_parent_driver or not cmds.objExists(source_parent_driver):
        logger.debug(f"Unable to connect driver offset. Provided source driver is missing.")
        return
    if not target_child_driver or not cmds.objExists(target_child_driver):
        logger.debug(f"Unable to connect driver offset. Provided target is missing.")
        return
    is_uuid_present = cmds.objExists(f"{source_parent_driver}.{tools_rig_const.RiggerConstants.ATTR_DRIVER_UUID}")
    if not is_uuid_present:
        logger.debug(f'Unable to connect driver offset. Provided target does not have a "driverUUID" attribute.')
        return
    attr = core_attr.add_attr(
        obj_list=target_child_driver,
        attr_type="string",
        attributes=tools_rig_const.RiggerConstants.ATTR_DRIVER_CHILD,
    )
    core_attr.connect_attr(
        source_attr=f"{source_parent_driver}.{tools_rig_const.RiggerConstants.ATTR_DRIVER_UUID}",
        target_attr_list=f"{target_child_driver}.{tools_rig_const.RiggerConstants.ATTR_DRIVER_CHILD}",
    )
    if attr and isinstance(attr, list):
        return attr[0]


def get_supporting_drivers(source_driver):
    """
    Gets supporting drivers from the destination connection of the driverUUID of a source driver.

    Args:
        source_driver (str, Node): Driver (often controls) with already populated driverUUID attribute.
    Returns:
        list: A list of connection destination objects that are auxiliary/supporting drivers (child of the main driver)
    """
    if not source_driver or not cmds.objExists(source_driver):
        logger.debug(f"Unable to get driver offset. Provided source driver is missing.")
        return []
    source_attr_path = f"{source_driver}.{tools_rig_const.RiggerConstants.ATTR_DRIVER_UUID}"
    if not cmds.objExists(source_attr_path):
        logger.debug(f'Unable to get driver offset. Provided source driver does not have a "driverUUID" attribute.')
        return []
    supporting_drivers = []
    for destination in cmds.listConnections(source_attr_path, destination=True) or []:
        supporting_drivers.append(core_node.Node(destination))
    return supporting_drivers


def create_twist_joints(
    start_joint,
    end_joint,
    number_of_twist=2,
    copy_start=False,
    copy_end=False,
    aim_axis="X",
):
    """
    Creates the twist joints and connections in a joint chain.

    Args:
        start_joint (str): First Joint of the chain.
        end_joint (str): Last Joint of the chain.
        number_of_twist (index, float): Number of twist joints.
        copy_start (bool): Copy the first joint of the chain.
        copy_end (bool): Copy the last joint of the chain.
        aim_axis (str): Primary joint aim axis.

    Returns:
        list: A list of all the twist joints.

    """
    twist_joints = []
    chain_distance = cmds.getAttr(f"{end_joint}.translate{aim_axis}")
    twist_distance = chain_distance / (number_of_twist + 1)
    joint_name = start_joint.split("_JNT")[0]
    twist_index = 1
    if copy_start:
        start_twist = cmds.duplicate(start_joint, n=f"[{joint_name}Twist0{twist_index}_JNT", po=True)[0]
        twist_index += 1
        cmds.parent(start_twist, start_joint)
        twist_joints.append(start_twist)
    for number in range(number_of_twist):
        twist_joint = cmds.duplicate(start_joint, n=f"[{joint_name}Twist0{twist_index}_JNT", po=True)[0]
        cmds.parent(twist_joint, start_joint)
        cmds.setAttr(f"{twist_joint}.translate{aim_axis}", twist_distance * (number + 1))
        twist_index += 1
        twist_joints.append(twist_joint)
    if copy_end:
        end_twist = cmds.duplicate(start_joint, n=f"[{joint_name}Twist0{twist_index}_JNT", po=True)[0]
        cmds.parent(end_twist, start_joint)
        cmds.setAttr(f"{end_twist}.translate{aim_axis}", chain_distance)
        twist_joints.append(end_twist)

    for jnt in twist_joints:
        core_attr.set_attr(
            obj_list=jnt,
            attr_list=tools_rig_const.RiggerConstants.ATTR_JOINT_UUID,
            value=core_uuid.generate_uuid(remove_dashes=True),
        )
        core_attr.set_attr(
            obj_list=jnt,
            attr_list=tools_rig_const.RiggerConstants.ATTR_JOINT_PURPOSE,
            value=jnt.split("_")[1],
        )
        core_attr.set_attr(
            obj_list=jnt,
            attr_list=tools_rig_const.RiggerConstants.ATTR_JOINT_DRIVERS,
            value=tools_rig_const.RiggerDriverTypes.TWIST,
        )

    return twist_joints


def get_world_ref_loc(name=f"world_ref_{core_naming.NamingConstants.Suffix.LOC}"):
    """
    Gets the path to a world reference group or create it in case it can't be found.
    Args:
        name (str, optional): Name of the reference group (found inside the "setup_grp")
    Returns:
        Node, str: Path to the reference group - Node format has string as its base.
    """
    automation_grp = get_automation_group(name="spaceAutomation")
    cmds.setAttr(f"{automation_grp}.visibility", 0)
    # Find or create automation group (base)
    if name and cmds.objExists(name):
        _world_grp_path = name
    else:
        _world_grp_path = cmds.spaceLocator(n=name)[0]
        core_hrchy.parent(source_objects=_world_grp_path, target_parent=automation_grp)
        if not automation_grp:
            logger.debug(f'Reference group "{str(name)}" could not be properly parented. ' f"Missing automation group.")
    cmds.select(clear=True)
    return _world_grp_path


def create_follow_setup(
    control,
    parent,
    attr_name="followParent",
    ref_loc=True,
    default_value=1,
    constraint_type="orient",
):
    """
    Creates a double constraint and attribute in a control to follow the parent.
    Args:
        control (Node): Control to follow the parent/world orientation.
        parent (Node): Object that is driving the control, usually a joint or a group.
        attr_name (str): Name of the attribute to be drive the switch.
        ref_loc (bool): If reference groups are being used instead of direct constraint (useful for different rotation
        orders).
        default_value (int): 0 or 1, the default value of the attribute.
        constraint_type (str): "orient" by default, the other accepted values are "parent" and "point"
    """
    if not isinstance(constraint_type, str):
        logger.warning(
            f"The supplied constraint type is not a string."
            f" Cannot create the follow setup for {core_naming.get_short_name(control)}"
        )
        return

    if constraint_type not in ["orient", "parent", "point"]:
        logger.warning(f"The supplied constraint type is not 'orient', 'parent' or 'point'. Cannot create the follow.")
        return

    # add follow attribute type
    follow_type_name_dict = {"orient": "Rotation", "point": "Position", "parent": ""}
    attr_name = f"{attr_name}{follow_type_name_dict[constraint_type]}"
    core_attr.add_attr(
        obj_list=control,
        attributes=attr_name,
        attr_type="float",
        maximum=1,
        minimum=0,
        default=default_value,
    )
    parent_offset_suffix = f"parentOffset{follow_type_name_dict[constraint_type]}"
    parent_offset = tools_rig_frm.ModuleGeneric().create_control_groups(
        control=control, suffix_list=parent_offset_suffix
    )[0]

    ctrl_parent = cmds.listRelatives(control, p=True, fullPath=True)[0]
    cmds.parent(parent_offset, ctrl_parent)
    cmds.parent(control, parent_offset)
    world_loc = get_world_ref_loc()
    cmds.setAttr(f"{world_loc}.visibility", 0)
    ref_rev = cmds.createNode("reverse", n=f"{parent_offset.get_short_name()}_rev")
    cmds.connectAttr(f"{control}.{attr_name}", f"{ref_rev}.inputX")

    if ref_loc:
        name = core_naming.get_short_name(parent).capitalize()
        parent_ref_loc = get_world_ref_loc(name=f"{name}_ref_{core_naming.NamingConstants.Suffix.LOC}")
        core_trans.match_translate(source=parent, target_list=parent_ref_loc)
        cmds.setAttr(f"{parent_ref_loc}.visibility", 0)
        cmds.parentConstraint(parent, parent_ref_loc, mo=True)
        source_cnstr = parent_ref_loc
    else:
        source_cnstr = ctrl_parent

    constraint_string = f"cmds.{constraint_type}Constraint(source_cnstr, world_loc, parent_offset, mo=True)"
    follow_constraint = eval(constraint_string)[0]
    cmds.connectAttr(f"{control}.{attr_name}", f"{follow_constraint}.w0")
    cmds.connectAttr(f"{ref_rev}.outputX", f"{follow_constraint}.w1")

    return follow_constraint


def create_follow_enum_setup(
    control,
    parent_list,
    attribute_item=None,
    ref_loc=True,
    default_value=1,
    constraint_type="parent",
):
    """
    Creates a double constraint and attribute in a control to follow the parent.
    Args:
        control (Node): Control to follow the parent/world orientation.
        parent_list (list): List of objects that will be driving the ctrl.
        attribute_item(str): Where do we want the attribute.
        ref_loc (bool): If reference groups are being used instead of direct constraint (useful for different rotation
        orders).
        default_value (int): 0 or 1, the default value of the attribute.
        constraint_type (str): "orient" by default, the other accepted values are "parent" and "point"
    """

    if not isinstance(constraint_type, str):
        logger.warning(
            f"The supplied constraint type is not a string."
            f" Cannot create the follow setup for {core_naming.get_short_name(control)}"
        )
        return

    if constraint_type not in ["orient", "parent", "point"]:
        logger.warning(f"The supplied constraint type is not 'orient', 'parent' or 'point'. Cannot create the follow.")
        return

    # add enum attribute
    parent_grps = ["World"]
    for parent in parent_list:
        if cmds.nodeType(parent) == "joint":
            name = cmds.getAttr(f"{parent}.{tools_rig_const.RiggerConstants.ATTR_JOINT_BASE_NAME}")
        elif (
            len(core_naming.get_short_name(parent).split("_")) <= 2
            or core_naming.get_short_name(parent).split("_")[1] == ""
        ):
            name = parent
        else:
            name = core_naming.get_short_name(parent).split("_")[1].capitalize()
        parent_grps.append(name)
    attr_names = ":".join(parent_grps)
    if not attribute_item:
        attribute_item = control
    core_attr.add_attr(
        obj_list=attribute_item,
        attributes="space",
        attr_type="enum",
        enum=attr_names,
        default=default_value,
    )
    parent_offset = tools_rig_frm.ModuleGeneric().create_control_groups(control=control, suffix_list="parentOffset")[0]
    ctrl_parent = cmds.listRelatives(control, p=True, fullPath=True)[0]
    cmds.parent(parent_offset, ctrl_parent)
    cmds.parent(control, parent_offset)
    world_loc = get_world_ref_loc()
    cmds.setAttr(f"{world_loc}.visibility", 0)

    if ref_loc:
        parent_loc_list = []
        for parent in parent_list:
            name = core_naming.get_short_name(parent).capitalize()
            parent_ref_loc = get_world_ref_loc(name=f"{name}_ref_{core_naming.NamingConstants.Suffix.LOC}")
            core_trans.match_translate(source=parent, target_list=parent_ref_loc)
            cmds.setAttr(f"{parent_ref_loc}.visibility", 0)
            cmds.parentConstraint(parent, parent_ref_loc, mo=True)
            parent_loc_list.append(parent_ref_loc)
        source_cnstr = parent_loc_list
    else:
        source_cnstr = ctrl_parent
    constraint_string = f"cmds.{constraint_type}Constraint(world_loc, source_cnstr, parent_offset, mo=True)"
    follow_constraint = eval(constraint_string)[0]
    for parent in parent_grps:
        for number in range(len(parent_grps)):
            if number == parent_grps.index(parent):
                value = 1
            else:
                value = 0
            cmds.setDrivenKeyframe(
                f"{follow_constraint}.w{parent_grps.index(parent)}",
                cd=f"{core_naming.get_short_name(attribute_item)}.space",
                dv=number,
                v=value,
            )

    return follow_constraint


def get_export_skeleton_root_joint():
    """
    Gets the root joint. The first joint in world or the first joint under the main skeleton group.

    Returns:
        str: the root joint of the export skeleton.
    """
    root_joint = None
    skl_grp = tools_rig_const.RiggerConstants.GRP_SKELETON_NAME
    top_joints = [jnt for jnt in cmds.ls(assemblies=True) if cmds.nodeType(jnt) == "joint"]

    if not top_joints:
        scene_joints = [jnt for jnt in cmds.ls() if cmds.nodeType(jnt) == "joint"]
        if scene_joints:
            top_joints = [
                jnt for jnt in scene_joints if cmds.listRelatives(jnt, p=True, fullPath=True)[0].endswith(skl_grp)
            ]

    if top_joints:
        root_joint = top_joints[0]

    return root_joint


def create_control_visualization_line(control, end_obj):
    """
    Builds a line connected to start and end objects.

    Args:
        control (Node): start point for the line
        end_obj (Node): end point for the line
    """

    # variables
    _attr_show_aim = "showAimLine"
    _grp_aim_lines = f"aimLines_{core_naming.NamingConstants.Suffix.GRP}"

    # aim lines group
    aim_grp = get_automation_group(subgroup=_grp_aim_lines)
    cmds.setAttr(f"{aim_grp}.visibility", 0)

    # create line
    line_items = core_curve.create_connection_line(object_a=control, object_b=end_obj, line_width=2)
    line_curve = line_items[0]

    # parent
    core_hrchy.parent(source_objects=line_items, target_parent=aim_grp)
    core_hrchy.parent(source_objects=line_curve, target_parent=control)
    core_attr.set_attr(obj_list=line_curve, attr_list=["tx", "ty", "tz"], value=0)

    # visibility attribute
    core_attr.add_attr(obj_list=control, attributes=_attr_show_aim, attr_type="bool", default=1)
    cmds.connectAttr(f"{control}.showAimLine", f"{line_curve}.visibility")

    # attributes
    cmds.setAttr(f"{line_curve}.inheritsTransform", 0)  # So it can be parented to control
    cmds.setAttr(f"{line_curve}.overrideEnabled", 1)  # Enable Modes (So it can be seen as template)
    cmds.setAttr(f"{line_curve}.overrideDisplayType", 1)  # Template
    core_attr.hide_lock_default_attrs(obj_list=line_curve, translate=True, rotate=True, scale=True, visibility=True)

    # change line name based on control
    control_name = control.get_short_name()
    current_suffix = control_name.split("_")[-1]
    if any(current_suffix == value for key, value in core_naming.NamingConstants.Suffix.__dict__.items()):
        new_line_name = control_name.replace(f"_{current_suffix}", f"_{core_naming.NamingConstants.Suffix.LINE}")
    else:
        new_line_name = f"{control_name}_{core_naming.NamingConstants.Suffix.LINE}"
    line_curve = cmds.rename(line_curve, new_line_name)

    return line_curve


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    # cmds.file(new=True, force=True)
    # create_direction_curve()
    # create_proxy_root_curve()
    # out = get_generic_driver("chest")
    # out = find_drivers_from_joint("hip")
    # create_ctrl_global()
    # cmds.select(out)
    cmds.viewFit(all=True)
