"""
Auto Rigger Leg Modules
"""

import gt.tools.auto_rigger.rig_constants as tools_rig_const
import gt.tools.auto_rigger.rig_framework as tools_rig_frm
import gt.tools.auto_rigger.rig_utils as tools_rig_utils
import gt.ui.resource_library as ui_res_lib
import gt.core.constraint as core_cnstr
import gt.core.hierarchy as core_hrchy
import gt.core.rigging as core_rigging
import gt.core.transform as core_trans
import gt.core.naming as core_naming
import gt.core.color as core_color
import gt.core.curve as core_curve
import gt.core.attr as core_attr
import gt.core.math as core_math
import gt.core.node as core_node
import maya.cmds as cmds
import logging

# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ModuleBipedLeg(tools_rig_frm.ModuleGeneric):
    __version__ = "0.0.3-alpha"
    icon = ui_res_lib.Icon.rigger_module_biped_leg
    allow_parenting = True

    # Reference Attributes
    REF_ATTR_KNEE_PROXY_PV = "lowerlegProxyPoleVectorLookupAttr"

    def __init__(self, name="Leg", prefix=None, suffix=None):
        super().__init__(name=name, prefix=prefix, suffix=suffix)

        # Module Config Vars
        self.setup_name = "leg"
        self.delete_toe_bind_jnt = True

        # Private Vars
        self._ankle_init_ty = None

        # Orientation
        _orientation = tools_rig_frm.OrientationData(aim_axis=(1, 0, 0), up_axis=(0, 0, -1), up_dir=(1, 0, 0))
        self.set_orientation(orientation_data=_orientation)

        # Module Unique Vars
        upperleg_name = "upperLeg"
        lowerleg_name = "lowerLeg"
        foot_name = "foot"
        ball_name = "ball"
        toe_name = "toe"
        heel_name = "heel"
        bank_left_name = "bankLeft"
        bank_right_name = "bankRight"

        # Extra Module Data
        self.set_extra_callable_function(self._delete_unbound_joints)  # Called after the control rig is built

        # Default Proxies
        self.upperleg_proxy = tools_rig_frm.Proxy(name=upperleg_name)
        self.upperleg_proxy.set_locator_scale(scale=2)
        self.upperleg_proxy.set_meta_purpose(value="upperLeg")
        self.upperleg_proxy.add_driver_type(
            driver_type=[tools_rig_const.RiggerDriverTypes.GENERIC, tools_rig_const.RiggerDriverTypes.FK]
        )
        self.upperleg_proxy.set_rotation_order("yzx")

        self.lowerleg_proxy = tools_rig_frm.Proxy(name=lowerleg_name)
        self.lowerleg_proxy.set_curve(curve=core_curve.get_curve("_proxy_joint_arrow_pos_z"))
        self.lowerleg_proxy.set_locator_scale(scale=2)
        self.lowerleg_proxy.add_line_parent(line_parent=self.upperleg_proxy)
        self.lowerleg_proxy.set_parent_uuid(uuid=self.upperleg_proxy.get_uuid())
        self.lowerleg_proxy.set_meta_purpose(value="lowerLeg")
        self.lowerleg_proxy.add_driver_type(
            driver_type=[
                tools_rig_const.RiggerDriverTypes.GENERIC,
                tools_rig_const.RiggerDriverTypes.FK,
                tools_rig_const.RiggerDriverTypes.IK,
            ]
        )
        self.lowerleg_proxy.set_rotation_order("xyz")

        self.foot_proxy = tools_rig_frm.Proxy(name=foot_name)
        self.foot_proxy.set_locator_scale(scale=2)
        self.foot_proxy.add_line_parent(line_parent=self.lowerleg_proxy)
        self.foot_proxy.set_meta_purpose(value="foot")
        self.foot_proxy.add_driver_type(
            driver_type=[
                tools_rig_const.RiggerDriverTypes.GENERIC,
                tools_rig_const.RiggerDriverTypes.FK,
                tools_rig_const.RiggerDriverTypes.IK,
            ]
        )
        self.foot_proxy.set_rotation_order("yzx")

        self.ball_proxy = tools_rig_frm.Proxy(name=ball_name)
        self.ball_proxy.set_locator_scale(scale=2)
        self.ball_proxy.add_line_parent(line_parent=self.foot_proxy)
        self.ball_proxy.set_parent_uuid(uuid=self.foot_proxy.get_uuid())
        self.ball_proxy.set_meta_purpose(value="ball")
        self.ball_proxy.add_driver_type(
            driver_type=[tools_rig_const.RiggerDriverTypes.GENERIC, tools_rig_const.RiggerDriverTypes.FK]
        )
        self.ball_proxy.set_rotation_order("xyz")

        self.toe_proxy = tools_rig_frm.Proxy(name=toe_name)
        self.toe_proxy.set_locator_scale(scale=1)
        self.toe_proxy.set_parent_uuid(uuid=self.ball_proxy.get_uuid())
        self.toe_proxy.set_parent_uuid_from_proxy(parent_proxy=self.ball_proxy)
        self.toe_proxy.set_meta_purpose(value="toe")
        self.toe_proxy.add_driver_type(
            driver_type=[tools_rig_const.RiggerDriverTypes.GENERIC, tools_rig_const.RiggerDriverTypes.IK]
        )

        self.heel_proxy = tools_rig_frm.Proxy(name=heel_name)
        self.heel_proxy.set_locator_scale(scale=1)
        self.heel_proxy.add_line_parent(line_parent=self.foot_proxy)
        self.heel_proxy.add_color(rgb_color=core_color.ColorConstants.RigProxy.PIVOT)
        self.heel_proxy.set_meta_purpose(value="heel")

        self.bank_left_proxy = tools_rig_frm.Proxy(name=bank_left_name)
        self.bank_left_proxy.set_locator_scale(scale=1)
        self.bank_left_proxy.add_line_parent(line_parent=self.foot_proxy)
        self.bank_left_proxy.add_color(rgb_color=core_color.ColorConstants.RigProxy.PIVOT)
        self.bank_left_proxy.set_meta_purpose(value="bankLeft")

        self.bank_right_proxy = tools_rig_frm.Proxy(name=bank_right_name)
        self.bank_right_proxy.set_locator_scale(scale=1)
        self.bank_right_proxy.add_line_parent(line_parent=self.foot_proxy)
        self.bank_right_proxy.add_color(rgb_color=core_color.ColorConstants.RigProxy.PIVOT)
        self.bank_right_proxy.set_meta_purpose(value="bankRight")

        # Initial Transforms
        upperleg_pos = core_trans.Vector3(y=84.5)
        lowerleg_pos = core_trans.Vector3(y=47.05)
        foot_pos = core_trans.Vector3(y=9.6)
        ball_pos = core_trans.Vector3(z=13.1)
        toe_pos = core_trans.Vector3(z=23.4)
        heel_pos = core_trans.Vector3()
        bank_left_pos = core_trans.Vector3(x=20.4, z=13.1)
        bank_right_pos = core_trans.Vector3(z=13.1)

        self.upperleg_proxy.set_initial_position(xyz=upperleg_pos)
        self.lowerleg_proxy.set_initial_position(xyz=lowerleg_pos)
        self.foot_proxy.set_initial_position(xyz=foot_pos)
        self.ball_proxy.set_initial_position(xyz=ball_pos)
        self.toe_proxy.set_initial_position(xyz=toe_pos)
        self.heel_proxy.set_initial_position(xyz=heel_pos)
        self.bank_left_proxy.set_initial_position(xyz=bank_left_pos)
        self.bank_right_proxy.set_initial_position(xyz=bank_right_pos)

        # Update Proxies
        self.proxies = [
            self.upperleg_proxy,
            self.lowerleg_proxy,
            self.foot_proxy,
            self.ball_proxy,
            self.toe_proxy,
            self.heel_proxy,
            self.bank_left_proxy,
            self.bank_right_proxy,
        ]

    def set_orientation_direction(self, is_positive, **kwargs):
        """
        Sets the direction of the orientation.
        If positive, it will use "1" in the desired axis.
        If negative, (not positive) it will use "-1" in the desired axis.
        Args:
            is_positive (bool): If True, it's set to a positive direction, if False to negative.
                                e.g. True = (1, 0, 0) while False (-1, 0, 0)
        """
        super().set_orientation_direction(
            is_positive=is_positive, set_aim_axis=True, set_up_axis=False, set_up_dir=False  # Only Aim Axis
        )

    def get_module_as_dict(self, **kwargs):
        """
        Overwrite to remove offset data from the export
        Args:
            kwargs: Key arguments, not used for anything
        """
        return super().get_module_as_dict(include_offset_data=False)

    def read_proxies_from_dict(self, proxy_dict):
        """
        Reads a proxy description dictionary and populates (after resetting) the proxies list with the dict proxies.
        Args:
            proxy_dict (dict): A proxy description dictionary. It must match an expected pattern for this to work:
                               Acceptable pattern: {"uuid_str": {<description>}}
                               "uuid_str" being the actual uuid string value of the proxy.
                               "<description>" being the output of the operation "proxy.get_proxy_as_dict()".
        """
        if not proxy_dict or not isinstance(proxy_dict, dict):
            logger.debug(f"Unable to read proxies from dictionary. Input must be a dictionary.")
            return
        self.read_purpose_matching_proxy_from_dict(proxy_dict)

    # --------------------------------------------------- Misc ---------------------------------------------------
    def is_valid(self):
        """
        Checks if the rig module is valid. This means, it's ready to be used and no issues were detected.
        Returns
            bool: True if valid, False otherwise
        """
        is_valid = super().is_valid()  # Passthrough
        return is_valid

    def build_proxy(self, **kwargs):
        """
        Build proxy elements in the viewport
        Returns:
            list: A list of ProxyData objects. These objects describe the created proxy elements.
        """
        if self.parent_uuid:
            self.upperleg_proxy.set_parent_uuid(self.parent_uuid)
        proxy = super().build_proxy(**kwargs)  # Passthrough
        return proxy

    def build_proxy_setup(self):
        """
        Runs post proxy script.
        When in a project, this runs after the "build_proxy" is done in all modules.
        """
        # Get Maya Elements
        global_proxy = tools_rig_utils.find_ctrl_global_proxy()
        upperleg = tools_rig_utils.find_proxy_from_uuid(self.upperleg_proxy.get_uuid())
        lowerleg = tools_rig_utils.find_proxy_from_uuid(self.lowerleg_proxy.get_uuid())
        foot = tools_rig_utils.find_proxy_from_uuid(self.foot_proxy.get_uuid())
        ball = tools_rig_utils.find_proxy_from_uuid(self.ball_proxy.get_uuid())
        heel = tools_rig_utils.find_proxy_from_uuid(self.heel_proxy.get_uuid())
        toe = tools_rig_utils.find_proxy_from_uuid(self.toe_proxy.get_uuid())
        bank_left = tools_rig_utils.find_proxy_from_uuid(self.bank_left_proxy.get_uuid())
        bank_right = tools_rig_utils.find_proxy_from_uuid(self.bank_right_proxy.get_uuid())

        self.upperleg_proxy.apply_offset_transform()
        self.lowerleg_proxy.apply_offset_transform()
        self.foot_proxy.apply_offset_transform()
        self.ball_proxy.apply_offset_transform()
        self.heel_proxy.apply_offset_transform()
        self.bank_left_proxy.apply_offset_transform()
        self.bank_right_proxy.apply_offset_transform()

        # UpperLeg -----------------------------------------------------------------------------------
        core_attr.hide_lock_default_attrs(upperleg, rotate=True, scale=True)

        # LowerLeg  ---------------------------------------------------------------------------------
        lowerleg_tag = lowerleg.get_short_name()
        core_attr.hide_lock_default_attrs(lowerleg, scale=True)

        # LowerLeg Setup - Always Between Hip and Ankle
        lowerleg_offset = tools_rig_utils.get_proxy_offset(lowerleg)
        core_cnstr.constraint_targets(
            source_driver=[upperleg, foot],
            target_driven=lowerleg_offset,
            constraint_type=core_cnstr.ConstraintTypes.POINT,
            maintain_offset=False,
        )

        lowerleg_pv_dir = cmds.spaceLocator(name=f"{lowerleg_tag}_poleVectorDir")[0]
        core_attr.add_attr(
            obj_list=lowerleg_pv_dir, attributes=ModuleBipedLeg.REF_ATTR_KNEE_PROXY_PV, attr_type="string"
        )
        core_trans.match_translate(source=lowerleg, target_list=lowerleg_pv_dir)
        cmds.move(0, 0, 13, lowerleg_pv_dir, relative=True)  # More it forward (in front of the lowerleg)
        core_hrchy.parent(lowerleg_pv_dir, lowerleg)

        # Lock LowerLeg Unstable Channels
        cmds.addAttr(lowerleg, ln="lockTranslateX", at="bool", k=True, niceName="Lock Unstable Channel")
        cmds.setAttr(f"{lowerleg}.lockTranslateX", 1)  # Active by default
        cmds.setAttr(f"{lowerleg}.minTransXLimit", 0)
        cmds.setAttr(f"{lowerleg}.maxTransXLimit", 0)
        cmds.connectAttr(f"{lowerleg}.lockTranslateX", f"{lowerleg}.minTransXLimitEnable")
        cmds.connectAttr(f"{lowerleg}.lockTranslateX", f"{lowerleg}.maxTransXLimitEnable")

        #  LowerLeg Constraints (Limits)
        lowerleg_dir_loc = cmds.spaceLocator(name=f"{lowerleg_tag}_dirParent_{core_naming.NamingConstants.Suffix.LOC}")[
            0
        ]
        lowerleg_aim_loc = cmds.spaceLocator(name=f"{lowerleg_tag}_dirAim_{core_naming.NamingConstants.Suffix.LOC}")[0]
        lowerleg_upvec_loc = cmds.spaceLocator(
            name=f"{lowerleg_tag}_dirParentUp_{core_naming.NamingConstants.Suffix.LOC}"
        )[0]
        lowerleg_upvec_loc_grp = f"{lowerleg_tag}_dirParentUp_{core_naming.NamingConstants.Suffix.GRP}"
        lowerleg_upvec_loc_grp = core_hrchy.create_group(name=lowerleg_upvec_loc_grp)

        # Hide Reference Elements
        core_attr.set_attr(
            obj_list=[lowerleg_pv_dir, lowerleg_upvec_loc_grp, lowerleg_dir_loc], attr_list="visibility", value=0
        )  # Set Visibility to Off
        core_attr.set_attr(
            obj_list=[lowerleg_pv_dir, lowerleg_upvec_loc_grp, lowerleg_dir_loc], attr_list="hiddenInOutliner", value=1
        )  # Set Outline Hidden to On

        lowerleg_upvec_loc_grp = core_hrchy.parent(lowerleg_upvec_loc_grp, global_proxy)[0]
        lowerleg_upvec_loc = core_hrchy.parent(lowerleg_upvec_loc, lowerleg_upvec_loc_grp)[0]
        lowerleg_dir_loc = core_hrchy.parent(lowerleg_dir_loc, global_proxy)[0]
        lowerleg_aim_loc = core_hrchy.parent(lowerleg_aim_loc, lowerleg_dir_loc)[0]

        lowerleg_divide_node = core_node.create_node(node_type="multiplyDivide", name=f"{lowerleg_tag}_divide")
        cmds.setAttr(f"{lowerleg_divide_node}.operation", 2)  # Change operation to Divide
        cmds.setAttr(f"{lowerleg_divide_node}.input2X", -2)
        cmds.connectAttr(f"{foot}.tx", f"{lowerleg_divide_node}.input1X")
        cmds.connectAttr(f"{lowerleg_divide_node}.outputX", f"{lowerleg_upvec_loc}.tx")

        core_trans.match_translate(source=upperleg, target_list=lowerleg_upvec_loc_grp)
        cmds.move(10, lowerleg_upvec_loc, moveY=True, relative=True)  # More it forward (in front of the lowerleg)
        cmds.pointConstraint(upperleg, lowerleg_upvec_loc_grp)
        cmds.pointConstraint(upperleg, lowerleg_dir_loc)
        cmds.pointConstraint([upperleg, foot], lowerleg_aim_loc)

        cmds.connectAttr(f"{lowerleg_dir_loc}.rotate", f"{lowerleg_offset}.rotate")

        cmds.aimConstraint(
            foot,
            lowerleg_dir_loc,
            aimVector=(0, -1, 0),
            upVector=(0, -1, 0),
            worldUpType="object",
            worldUpObject=lowerleg_upvec_loc,
        )

        cmds.aimConstraint(
            lowerleg_aim_loc, lowerleg, aimVector=(0, 0, -1), upVector=(0, 1, 0), worldUpType="none", skip=["x", "z"]
        )

        core_attr.set_attr_state(obj_list=lowerleg, attr_list="rotate", locked=True)

        # LowerLeg Limits
        cmds.setAttr(f"{lowerleg}.minTransZLimit", 0)
        cmds.setAttr(f"{lowerleg}.minTransZLimitEnable", True)

        # Foot ----------------------------------------------------------------------------------
        foot_offset = tools_rig_utils.get_proxy_offset(foot)
        core_attr.add_attr(obj_list=foot.get_long_name(), attributes="followHip", attr_type="bool", default=True)
        constraint = cmds.pointConstraint(upperleg, foot_offset, skip="y")[0]
        cmds.connectAttr(f"{foot}.followHip", f"{constraint}.w0")
        core_attr.set_attr_state(obj_list=foot, attr_list=["rx", "rz"], locked=True, hidden=True)

        # Ball -----------------------------------------------------------------------------------
        foot_tag = foot.get_short_name()
        ball_offset = tools_rig_utils.get_proxy_offset(ball)
        ball_driver = core_hrchy.create_group(name=f"{foot_tag}_pivot")
        ball_driver = core_hrchy.parent(source_objects=ball_driver, target_parent=global_proxy)[0]
        foot_pos = cmds.xform(foot, q=True, ws=True, rp=True)
        cmds.move(foot_pos[0], ball_driver, moveX=True)
        cmds.pointConstraint(foot, ball_driver, maintainOffset=True, skip=["y"])
        cmds.orientConstraint(foot, ball_driver, maintainOffset=True, skip=["x", "z"])
        cmds.scaleConstraint(foot, ball_driver, skip=["y"])
        core_hrchy.parent(ball_offset, ball_driver)

        # Keep Grounded
        for to_lock_ty in [toe, ball]:
            to_lock_ty = str(to_lock_ty)
            cmds.addAttr(to_lock_ty, ln="lockTranslateY", at="bool", k=True, niceName="Keep Grounded")
            cmds.setAttr(f"{to_lock_ty}.lockTranslateY", 0)
            cmds.setAttr(f"{to_lock_ty}.minTransYLimit", 0)
            cmds.setAttr(f"{to_lock_ty}.maxTransYLimit", 0)
            cmds.connectAttr(f"{to_lock_ty}.lockTranslateY", f"{to_lock_ty}.minTransYLimitEnable", f=True)
            cmds.connectAttr(f"{to_lock_ty}.lockTranslateY", f"{to_lock_ty}.maxTransYLimitEnable", f=True)

        # Heel -----------------------------------------------------------------------------------
        heel_offset = tools_rig_utils.get_proxy_offset(heel)
        core_attr.add_attr(obj_list=heel.get_long_name(), attributes="followAnkle", attr_type="bool", default=True)
        constraint = cmds.pointConstraint(foot, heel_offset, skip="y")[0]
        cmds.connectAttr(f"{heel}.followAnkle", f"{constraint}.w0")
        core_hrchy.parent(source_objects=ball_offset, target_parent=ball_driver)
        core_attr.hide_lock_default_attrs(heel, translate=False, rotate=True, scale=True)

        # Bank Left and Right -----------------------------------------------------------------------------------
        bank_left_offset = tools_rig_utils.get_proxy_offset(bank_left)
        core_attr.add_attr(obj_list=bank_left.get_long_name(), attributes="followAnkle", attr_type="bool", default=True)
        constraint = cmds.pointConstraint(foot, bank_left_offset, skip="y")[0]
        cmds.connectAttr(f"{bank_left}.followAnkle", f"{constraint}.w0")
        core_hrchy.parent(source_objects=ball_offset, target_parent=ball_driver)
        core_attr.hide_lock_default_attrs(bank_left, translate=False, rotate=True, scale=True)

        bank_right_offset = tools_rig_utils.get_proxy_offset(bank_right)
        core_attr.add_attr(
            obj_list=bank_right.get_long_name(), attributes="followAnkle", attr_type="bool", default=True
        )
        constraint = cmds.pointConstraint(foot, bank_right_offset, skip="y")[0]
        cmds.connectAttr(f"{bank_right}.followAnkle", f"{constraint}.w0")
        core_hrchy.parent(source_objects=ball_offset, target_parent=ball_driver)
        core_attr.hide_lock_default_attrs(bank_right, translate=False, rotate=True, scale=True)

        self.upperleg_proxy.apply_transforms()
        self.foot_proxy.apply_transforms()
        self.ball_proxy.apply_transforms()
        self.heel_proxy.apply_transforms()
        self.toe_proxy.apply_transforms()
        self.bank_left_proxy.apply_transforms()
        self.bank_right_proxy.apply_transforms()
        self.lowerleg_proxy.apply_transforms()  # Refresh due to automation

        # Hide unused ROT order attrs
        rot_order_attr = tools_rig_const.RiggerConstants.ATTR_ROT_ORDER
        core_attr.set_attr_state(f"{bank_left}.{rot_order_attr}", hidden=True)
        core_attr.set_attr_state(f"{bank_right}.{rot_order_attr}", hidden=True)
        core_attr.set_attr_state(f"{toe}.{rot_order_attr}", hidden=True)
        core_attr.set_attr_state(f"{heel}.{rot_order_attr}", hidden=True)

        # Clear
        cmds.select(clear=True)

    def build_skeleton_joints(self):
        super().build_skeleton_joints()  # Passthrough

        # Delete Unnecessary joints (Proxies used as pivots)
        heel_jnt = tools_rig_utils.find_joint_from_uuid(self.heel_proxy.get_uuid())
        bank_left_jnt = tools_rig_utils.find_joint_from_uuid(self.bank_left_proxy.get_uuid())
        bank_right_jnt = tools_rig_utils.find_joint_from_uuid(self.bank_right_proxy.get_uuid())
        joints_to_delete = [heel_jnt, bank_left_jnt, bank_right_jnt]

        for jnt in joints_to_delete:
            if jnt and cmds.objExists(jnt):
                cmds.delete(jnt)

    def build_skeleton_hierarchy(self):
        """
        Runs post rig script.
        When in a project, this runs after the "build_skeleton_joints" is done in all modules.
        """
        self.foot_proxy.set_parent_uuid(self.lowerleg_proxy.get_uuid())
        super().build_skeleton_hierarchy()  # Passthrough
        self.foot_proxy.clear_parent_uuid()

        # set the correct foot orientation (world aligned)
        foot_jnt = tools_rig_utils.find_joint_from_uuid(self.foot_proxy.get_uuid())
        module_aim = self.orientation.get_aim_axis()
        self.orientation.set_aim_axis((-module_aim[0], 0, 0))
        self.orientation.set_world_aligned(world_aligned=True)
        self.orientation.apply_automatic_orientation(joint_list=[foot_jnt])
        self.orientation.set_aim_axis(module_aim)
        self.orientation.set_world_aligned(world_aligned=False)

    def build_rig(self, **kwargs):
        """
        Build core rig setup for this module.
        """

        # Get Elements
        global_ctrl = tools_rig_utils.find_ctrl_global()
        global_offset_ctrl = tools_rig_utils.find_ctrl_global_offset()
        upperleg_jnt = tools_rig_utils.find_joint_from_uuid(self.upperleg_proxy.get_uuid())
        lowerleg_jnt = tools_rig_utils.find_joint_from_uuid(self.lowerleg_proxy.get_uuid())
        foot_jnt = tools_rig_utils.find_joint_from_uuid(self.foot_proxy.get_uuid())
        ball_jnt = tools_rig_utils.find_joint_from_uuid(self.ball_proxy.get_uuid())
        toe_jnt = tools_rig_utils.find_joint_from_uuid(self.toe_proxy.get_uuid())
        module_jnt_list = [upperleg_jnt, lowerleg_jnt, foot_jnt, ball_jnt, toe_jnt]
        # Get Formatted Prefix
        _prefix = ""
        if self.prefix:
            _prefix = f"{self.prefix}_"

        # Set Colors
        for jnt in module_jnt_list:
            core_color.set_color_viewport(obj_list=jnt, rgb_color=(0.3, 0.3, 0))

        # Get Scale
        leg_scale = core_math.dist_path_sum(input_list=[upperleg_jnt, lowerleg_jnt, foot_jnt])
        foot_scale = core_math.dist_path_sum(input_list=[foot_jnt, ball_jnt, toe_jnt])

        # Set Preferred Angle
        cmds.setAttr(f"{upperleg_jnt}.preferredAngleZ", 90)
        cmds.setAttr(f"{lowerleg_jnt}.preferredAngleZ", -90)

        # Create Parent Automation Elements
        joint_automation_grp = tools_rig_utils.find_or_create_joint_automation_group()
        general_automation_grp = tools_rig_utils.get_automation_group()
        module_parent_jnt = tools_rig_utils.get_driven_joint(self.get_parent_uuid())
        core_hrchy.parent(source_objects=module_parent_jnt, target_parent=joint_automation_grp)

        # Create Automation Skeletons (FK/IK) --------------------------------------------------------------
        upperleg_parent = module_parent_jnt
        if module_parent_jnt:
            core_color.set_color_viewport(
                obj_list=upperleg_parent, rgb_color=core_color.ColorConstants.RigJoint.AUTOMATION
            )
            core_rigging.rescale_joint_radius(
                joint_list=upperleg_parent, multiplier=tools_rig_const.RiggerConstants.LOC_RADIUS_MULTIPLIER_DRIVEN
            )
        else:
            upperleg_parent = joint_automation_grp

        upperleg_fk = core_rigging.duplicate_joint_for_automation(upperleg_jnt, suffix="fk", parent=upperleg_parent)
        lowerleg_fk = core_rigging.duplicate_joint_for_automation(lowerleg_jnt, suffix="fk", parent=upperleg_fk)
        foot_fk = core_rigging.duplicate_joint_for_automation(foot_jnt, suffix="fk", parent=lowerleg_fk)
        ball_fk = core_rigging.duplicate_joint_for_automation(ball_jnt, suffix="fk", parent=foot_fk)
        toe_fk = core_rigging.duplicate_joint_for_automation(toe_jnt, suffix="fk", parent=ball_fk)
        fk_joints = [upperleg_fk, lowerleg_fk, foot_fk, ball_fk, toe_fk]

        upperleg_ik = core_rigging.duplicate_joint_for_automation(upperleg_jnt, suffix="ik", parent=upperleg_parent)
        lowerleg_ik = core_rigging.duplicate_joint_for_automation(lowerleg_jnt, suffix="ik", parent=upperleg_ik)
        foot_ik = core_rigging.duplicate_joint_for_automation(foot_jnt, suffix="ik", parent=lowerleg_ik)
        ball_ik = core_rigging.duplicate_joint_for_automation(ball_jnt, suffix="ik", parent=foot_ik)
        toe_ik = core_rigging.duplicate_joint_for_automation(toe_jnt, suffix="ik", parent=ball_ik)
        ik_joints = [upperleg_ik, lowerleg_ik, foot_ik, ball_ik, toe_ik]

        core_rigging.rescale_joint_radius(
            joint_list=fk_joints, multiplier=tools_rig_const.RiggerConstants.LOC_RADIUS_MULTIPLIER_FK
        )
        core_rigging.rescale_joint_radius(
            joint_list=ik_joints, multiplier=tools_rig_const.RiggerConstants.LOC_RADIUS_MULTIPLIER_IK
        )
        core_color.set_color_viewport(obj_list=fk_joints, rgb_color=core_color.ColorConstants.RigJoint.FK)
        core_color.set_color_viewport(obj_list=ik_joints, rgb_color=core_color.ColorConstants.RigJoint.IK)
        core_color.set_color_outliner(obj_list=fk_joints, rgb_color=core_color.ColorConstants.RigOutliner.FK)
        core_color.set_color_outliner(obj_list=ik_joints, rgb_color=core_color.ColorConstants.RigOutliner.IK)

        # FK Controls --------------------------------------------------------------------------------------

        fk_offsets_ctrls = []
        # FK UpperLeg Control
        upperleg_fk_ctrl, upperleg_fk_offset = self.create_rig_control(
            control_base_name=self.upperleg_proxy.get_name(),
            curve_file_name="_circle_pos_x",
            parent_obj=global_offset_ctrl,
            match_obj=upperleg_jnt,
            add_offset_ctrl=False,
            rot_order=1,
            shape_scale=leg_scale * 0.1,
            color=core_color.get_directional_color(object_name=upperleg_jnt),
        )[:2]
        self._add_driver_uuid_attr(
            target_driver=upperleg_fk_ctrl,
            driver_type=tools_rig_const.RiggerDriverTypes.FK,
            proxy_purpose=self.upperleg_proxy,
        )
        core_cnstr.constraint_targets(source_driver=upperleg_fk_ctrl, target_driven=upperleg_fk)
        fk_offsets_ctrls.append(upperleg_fk_offset[0])

        # FK LowerLeg Control
        lowerleg_fk_ctrl, lowerleg_fk_offset = self.create_rig_control(
            control_base_name=self.lowerleg_proxy.get_name(),
            curve_file_name="_circle_pos_x",
            parent_obj=upperleg_fk_ctrl,
            match_obj=lowerleg_jnt,
            rot_order=0,
            add_offset_ctrl=False,
            shape_scale=leg_scale * 0.1,
            color=core_color.get_directional_color(object_name=lowerleg_jnt),
        )[:2]
        self._add_driver_uuid_attr(
            target_driver=lowerleg_fk_ctrl,
            driver_type=tools_rig_const.RiggerDriverTypes.FK,
            proxy_purpose=self.lowerleg_proxy,
        )
        core_cnstr.constraint_targets(source_driver=lowerleg_fk_ctrl, target_driven=lowerleg_fk)
        fk_offsets_ctrls.append(lowerleg_fk_offset[0])

        # FK Foot Control
        foot_fk_ctrl, foot_fk_offset = self.create_rig_control(
            control_base_name=self.foot_proxy.get_name(),
            curve_file_name="_circle_pos_x",
            parent_obj=lowerleg_fk_ctrl,
            match_obj=foot_jnt,
            add_offset_ctrl=False,
            rot_order=1,
            shape_scale=leg_scale * 0.1,
            color=core_color.get_directional_color(object_name=foot_jnt),
        )[:2]
        self._add_driver_uuid_attr(
            target_driver=foot_fk_ctrl, driver_type=tools_rig_const.RiggerDriverTypes.FK, proxy_purpose=self.foot_proxy
        )
        core_cnstr.constraint_targets(source_driver=foot_fk_ctrl, target_driven=foot_fk)
        fk_offsets_ctrls.append(foot_fk_offset[0])

        # Remove Ankle Shape Orientation
        temp_transform = core_hrchy.create_group(name=f"{foot_fk_ctrl}_rotExtraction")
        core_trans.match_translate(source=toe_jnt, target_list=temp_transform)
        core_trans.match_translate(source=foot_jnt, target_list=temp_transform, skip=["x", "z"])
        cmds.delete(
            cmds.aimConstraint(
                temp_transform,
                foot_fk_ctrl,
                offset=(0, 0, 0),
                aimVector=(0, 1, 0),
                upVector=(1, 0, 0),
                worldUpType="vector",
                worldUpVector=(0, -1, 0),
            )
        )
        cmds.delete(temp_transform)
        cmds.makeIdentity(foot_fk_ctrl, apply=True, rotate=True)

        # FK Ball Control
        ball_fk_ctrl, ball_offset = self.create_rig_control(
            control_base_name=self.ball_proxy.get_name(),
            curve_file_name="_circle_pos_x",
            parent_obj=foot_fk_ctrl,
            rot_order=0,
            match_obj=ball_jnt,
            add_offset_ctrl=False,
            shape_scale=foot_scale * 0.3,
            color=core_color.get_directional_color(object_name=foot_jnt),
        )[:2]
        self._add_driver_uuid_attr(
            target_driver=ball_fk_ctrl, driver_type=tools_rig_const.RiggerDriverTypes.FK, proxy_purpose=self.ball_proxy
        )
        core_cnstr.constraint_targets(source_driver=ball_fk_ctrl, target_driven=ball_fk)
        fk_offsets_ctrls.append(ball_offset[0])

        # IK Controls --------------------------------------------------------------------------------------
        ik_offsets_ctrls = []

        # IK LowerLeg Control
        ik_suffix = core_naming.NamingConstants.Description.IK.upper()
        lowerleg_ik_ctrl, lowerleg_offset = self.create_rig_control(
            control_base_name=f"{self.lowerleg_proxy.get_name()}_{ik_suffix}",
            curve_file_name="primitive_diamond",
            parent_obj=global_offset_ctrl,
            match_obj_pos=foot_jnt,
            add_offset_ctrl=False,
            shape_scale=leg_scale * 0.05,
            color=core_color.get_directional_color(object_name=foot_jnt),
        )[:2]
        self._add_driver_uuid_attr(
            target_driver=lowerleg_ik_ctrl,
            driver_type=tools_rig_const.RiggerDriverTypes.IK,
            proxy_purpose=self.lowerleg_proxy,
        )
        ik_offsets_ctrls.append(lowerleg_offset[0])

        # Find Pole Vector Position
        lowerleg_proxy = tools_rig_utils.find_proxy_from_uuid(uuid_string=self.lowerleg_proxy.get_uuid())
        lowerleg_proxy_children = (
            cmds.listRelatives(lowerleg_proxy, children=True, typ="transform", fullPath=True) or []
        )
        lowerleg_pv_dir = tools_rig_utils.find_object_with_attr(
            attr_name=ModuleBipedLeg.REF_ATTR_KNEE_PROXY_PV, lookup_list=lowerleg_proxy_children
        )

        temp_transform = core_hrchy.create_group(name=f"{lowerleg_ik_ctrl}_rotExtraction")
        core_trans.match_translate(source=lowerleg_jnt, target_list=temp_transform)
        cmds.delete(
            cmds.aimConstraint(
                lowerleg_pv_dir,
                temp_transform,
                offset=(0, 0, 0),
                aimVector=(1, 0, 0),
                upVector=(0, -1, 0),
                worldUpType="vector",
                worldUpVector=(0, 1, 0),
            )
        )
        cmds.move(leg_scale * 0.5, 0, 0, temp_transform, objectSpace=True, relative=True)
        cmds.delete(cmds.pointConstraint(temp_transform, lowerleg_offset))
        cmds.delete(temp_transform)

        # IK Aim Line
        tools_rig_utils.create_control_visualization_line(lowerleg_ik_ctrl, lowerleg_ik)

        # IK Foot Control
        foot_projection = cmds.xform(foot_jnt, ws=True, t=True, q=True)[1]
        if self.prefix == core_naming.NamingConstants.Prefix.RIGHT:
            rot_offset = (0, 0, 180)
            foot_projection = -foot_projection
        else:
            rot_offset = (0, 0, 0)

        foot_ik_ctrl, foot_ik_offset, foot_o_ctrl, foot_o_data = self.create_rig_control(
            control_base_name=f"{self.foot_proxy.get_name()}_{ik_suffix}",
            curve_file_name="human_foot_outline",
            parent_obj=global_offset_ctrl,
            rot_order=1,
            match_obj_pos=foot_jnt,
            add_offset_ctrl=True,
            shape_scale=foot_scale * 0.5,
            shape_rot_offset=rot_offset,
            shape_pos_offset=(0, -foot_projection, 0),
            color=core_color.get_directional_color(object_name=foot_jnt),
        )
        self._add_driver_uuid_attr(
            target_driver=foot_ik_ctrl, driver_type=tools_rig_const.RiggerDriverTypes.IK, proxy_purpose=self.foot_proxy
        )
        cmds.orientConstraint(foot_ik_ctrl, foot_ik, mo=True)
        ik_offsets_ctrls.append(foot_ik_offset[0])

        # Switch Control
        foot_proxy = tools_rig_utils.find_proxy_from_uuid(uuid_string=self.foot_proxy.get_uuid())
        ik_switch_ctrl, ik_switch_offset = self.create_rig_control(
            control_base_name=self.setup_name,
            curve_file_name="gear_eight_sides_smooth",
            parent_obj=global_ctrl,
            match_obj=foot_proxy,
            add_offset_ctrl=False,
            shape_rot_offset=(0, 0, 90),
            shape_pos_offset=(0, 0, leg_scale * -0.3),
            shape_scale=leg_scale * 0.012,
            color=core_color.get_directional_color(object_name=foot_jnt),
        )[:2]
        self._add_driver_uuid_attr(
            target_driver=ik_switch_ctrl,
            driver_type=tools_rig_const.RiggerDriverTypes.SWITCH,
            proxy_purpose=self.setup_name,
        )

        # Switch Setup
        core_rigging.create_switch_setup(
            source_a=ik_joints,
            source_b=fk_joints,
            target_base=module_jnt_list,
            attr_holder=ik_switch_ctrl,
            visibility_a=fk_offsets_ctrls,
            visibility_b=ik_offsets_ctrls,
            shape_visibility=False,
            prefix=_prefix,
            invert=True,
        )

        switch_cons = core_cnstr.constraint_targets(
            source_driver=[foot_fk_ctrl, foot_ik_ctrl], target_driven=ik_switch_offset
        )[0]
        leg_rev = cmds.createNode("reverse", name=f"{_prefix}leg_rev")
        cmds.connectAttr(f"{ik_switch_ctrl}.influenceSwitch", f"{leg_rev}.inputX")
        cmds.connectAttr(f"{leg_rev}.outputX", f"{switch_cons}.w0")
        cmds.connectAttr(f"{ik_switch_ctrl}.influenceSwitch", f"{switch_cons}.w1")

        influence_switch_attr_nice_name = "FK/IK"
        cmds.addAttr(f"{ik_switch_ctrl}.influenceSwitch", e=True, nn=influence_switch_attr_nice_name)
        cmds.setAttr(f"{ik_switch_ctrl}.influenceSwitch", 0)  # Default is FK

        # Foot Pivots

        foot_automation_grp = core_hrchy.create_group(name=f"{_prefix}{self.foot_proxy.get_name()}_automation_grp")
        core_hrchy.parent(source_objects=foot_automation_grp, target_parent=general_automation_grp)

        foot_pivot_grp = core_hrchy.create_group(name=f"{_prefix}{self.foot_proxy.get_name()}_pivot_grp")
        core_trans.match_transform(source=foot_proxy, target_list=foot_pivot_grp)
        core_hrchy.parent(source_objects=foot_pivot_grp, target_parent=foot_automation_grp)
        cmds.parentConstraint(foot_o_ctrl, foot_pivot_grp)

        bank_left_proxy = tools_rig_utils.find_proxy_from_uuid(uuid_string=self.bank_left_proxy.get_uuid())
        bank_left_pivot_grp = core_hrchy.create_group(name=f"{_prefix}{self.bank_left_proxy.get_name()}_pivot_grp")
        core_trans.match_transform(source=bank_left_proxy, target_list=bank_left_pivot_grp)
        core_hrchy.parent(source_objects=bank_left_pivot_grp, target_parent=foot_pivot_grp)

        bank_right_proxy = tools_rig_utils.find_proxy_from_uuid(uuid_string=self.bank_right_proxy.get_uuid())
        bank_right_pivot_grp = core_hrchy.create_group(name=f"{_prefix}{self.bank_right_proxy.get_name()}_pivot_grp")
        core_trans.match_transform(source=bank_right_proxy, target_list=bank_right_pivot_grp)
        core_hrchy.parent(source_objects=bank_right_pivot_grp, target_parent=bank_left_pivot_grp)

        heel_proxy = tools_rig_utils.find_proxy_from_uuid(uuid_string=self.heel_proxy.get_uuid())
        heel_pivot_grp = core_hrchy.create_group(name=f"{_prefix}{self.heel_proxy.get_name()}_pivot_grp")
        core_trans.match_transform(source=heel_proxy, target_list=heel_pivot_grp)
        core_hrchy.parent(source_objects=heel_pivot_grp, target_parent=bank_right_pivot_grp)

        ball_twist_proxy = tools_rig_utils.find_proxy_from_uuid(uuid_string=self.ball_proxy.get_uuid())
        ball_twist_pivot_grp = core_hrchy.create_group(name=f"{_prefix}{self.ball_proxy.get_name()}Twist_pivot_grp")
        core_trans.match_transform(source=ball_twist_proxy, target_list=ball_twist_pivot_grp)
        core_hrchy.parent(source_objects=ball_twist_pivot_grp, target_parent=heel_pivot_grp)

        core_trans.match_transform(source=ball_twist_proxy, target_list=ball_twist_pivot_grp)
        core_hrchy.parent(source_objects=ball_twist_pivot_grp, target_parent=heel_pivot_grp)

        toe_proxy = tools_rig_utils.find_proxy_from_uuid(uuid_string=self.toe_proxy.get_uuid())
        toe_pivot_grp = core_hrchy.create_group(name=f"{_prefix}{self.toe_proxy.get_name()}_pivot_grp")
        core_trans.match_transform(source=toe_proxy, target_list=toe_pivot_grp)
        core_hrchy.parent(source_objects=toe_pivot_grp, target_parent=ball_twist_pivot_grp)

        ball_proxy = tools_rig_utils.find_proxy_from_uuid(uuid_string=self.ball_proxy.get_uuid())
        ball_pivot_grp = core_hrchy.create_group(name=f"{_prefix}{self.ball_proxy.get_name()}_pivot_grp")
        core_trans.match_transform(source=ball_proxy, target_list=ball_pivot_grp)
        core_hrchy.parent(source_objects=ball_pivot_grp, target_parent=toe_pivot_grp)

        toe_fk_proxy = tools_rig_utils.find_proxy_from_uuid(uuid_string=self.toe_proxy.get_uuid())
        toe_fk_ctrl_offset = core_hrchy.create_group(name=f"{_prefix}{self.toe_proxy.get_name()}FK_ctrl_offset")
        core_trans.match_transform(source=ball_proxy, target_list=toe_fk_ctrl_offset)
        core_hrchy.parent(source_objects=toe_fk_ctrl_offset, target_parent=toe_pivot_grp)
        toe_fk_ctrl_grp = core_hrchy.create_group(name=f"{_prefix}{self.toe_proxy.get_name()}FK_ctrl")
        core_trans.match_transform(source=ball_proxy, target_list=toe_fk_ctrl_grp)
        core_hrchy.parent(source_objects=toe_fk_ctrl_grp, target_parent=toe_fk_ctrl_offset)
        toe_fk_pivot_grp = core_hrchy.create_group(name=f"{_prefix}{self.toe_proxy.get_name()}FK_pivot_grp")
        core_trans.match_transform(source=toe_fk_proxy, target_list=toe_fk_pivot_grp)
        core_hrchy.parent(source_objects=toe_fk_pivot_grp, target_parent=toe_fk_ctrl_grp)

        # Foot Automation
        cmds.addAttr(foot_ik_ctrl, ln="kneeTwist", nn="Knee Twist", at="float", keyable=True)
        cmds.addAttr(foot_ik_ctrl, ln="footRolls", nn="Foot Rolls", at="enum", en="-------------:", keyable=True)
        cmds.setAttr(f"{foot_ik_ctrl}.footRolls", lock=True)

        cmds.addAttr(foot_ik_ctrl, ln="footRollWeight", nn="Foot Roll Weight", at="float", keyable=True, min=0, max=1.0)
        cmds.addAttr(foot_ik_ctrl, ln="footRoll", nn="Foot Roll", at="float", keyable=True)

        foot_weight_rev = cmds.createNode("reverse", n=f"{_prefix}footWeight_rev")
        cmds.connectAttr(f"{foot_ik_ctrl}.footRollWeight", f"{foot_weight_rev}.inputX")

        foot_roll_clamp = cmds.createNode("clamp", n=f"{_prefix}footRoll_clamp")
        cmds.connectAttr(f"{foot_ik_ctrl}.footRoll", f"{foot_roll_clamp}.inputR")
        cmds.connectAttr(f"{foot_ik_ctrl}.footRoll", f"{foot_roll_clamp}.inputG")
        cmds.setAttr(f"{foot_roll_clamp}.minR", -180)
        cmds.setAttr(f"{foot_roll_clamp}.maxG", 180)

        foot_mult = cmds.createNode("multiplyDivide", n=f"{_prefix}footWeight_mult")
        cmds.connectAttr(f"{foot_weight_rev}.outputX", f"{foot_mult}.input2X")
        cmds.connectAttr(f"{foot_ik_ctrl}.footRoll", f"{foot_mult}.input1Y")
        cmds.connectAttr(f"{foot_roll_clamp}.outputG", f"{foot_mult}.input1X")
        cmds.connectAttr(f"{foot_ik_ctrl}.footRollWeight", f"{foot_mult}.input2Y")

        cmds.addAttr(foot_ik_ctrl, ln="sideRoll", nn="Side Roll", at="float", keyable=True)
        side_roll_clamp = cmds.createNode("clamp", n=f"{_prefix}sideRoll_clamp")
        cmds.setAttr(f"{side_roll_clamp}.minR", -1000)
        cmds.setAttr(f"{side_roll_clamp}.maxG", 1000)
        cmds.connectAttr(f"{foot_ik_ctrl}.sideRoll", f"{side_roll_clamp}.inputR")
        cmds.connectAttr(f"{foot_ik_ctrl}.sideRoll", f"{side_roll_clamp}.inputG")
        side_roll_rev = cmds.createNode("multiplyDivide", n=f"{_prefix}sideRoll_multRev")
        cmds.setAttr(f"{side_roll_rev}.input2X", -1)
        cmds.setAttr(f"{side_roll_rev}.input2Y", -1)
        cmds.connectAttr(f"{side_roll_clamp}.outputR", f"{side_roll_rev}.input1X")
        cmds.connectAttr(f"{side_roll_clamp}.outputG", f"{side_roll_rev}.input1Y")
        cmds.connectAttr(f"{side_roll_rev}.outputY", f"{bank_left_pivot_grp}.rotateZ")
        cmds.connectAttr(f"{side_roll_rev}.outputX", f"{bank_right_pivot_grp}.rotateZ")

        cmds.addAttr(foot_ik_ctrl, ln="heelRoll", nn="Heel Roll", at="float", keyable=True)
        heel_rev = cmds.createNode("multiplyDivide", n=f"{_prefix}heel_multRev")
        cmds.setAttr(f"{heel_rev}.input2X", -1)
        heel_add = cmds.createNode("plusMinusAverage", n=f"{_prefix}heel_add")
        cmds.setAttr(f"{heel_add}.operation", 1)
        cmds.connectAttr(f"{foot_ik_ctrl}.heelRoll", f"{heel_rev}.input1X")
        cmds.connectAttr(f"{heel_rev}.outputX", f"{heel_add}.input3D[1].input3Dx")
        cmds.connectAttr(f"{foot_roll_clamp}.outputR", f"{heel_add}.input3D[2].input3Dx")
        cmds.connectAttr(f"{heel_add}.output3D.output3Dx", f"{heel_pivot_grp}.rotateX")

        cmds.addAttr(foot_ik_ctrl, ln="ballRoll", nn="Ball Roll", at="float", keyable=True)
        ball_add = cmds.createNode("plusMinusAverage", n=f"{_prefix}ball_add")
        cmds.setAttr(f"{ball_add}.operation", 1)
        cmds.connectAttr(f"{foot_ik_ctrl}.ballRoll", f"{ball_add}.input3D[1].input3Dx")
        cmds.connectAttr(f"{foot_mult}.outputX", f"{ball_add}.input3D[2].input3Dx")
        cmds.connectAttr(f"{ball_add}.output3D.output3Dx", f"{ball_pivot_grp}.rotateX")

        cmds.addAttr(foot_ik_ctrl, ln="toeRoll", nn="Toe Roll", at="float", keyable=True)
        toe_add = cmds.createNode("plusMinusAverage", n=f"{_prefix}toe_add")
        cmds.setAttr(f"{toe_add}.operation", 1)
        cmds.connectAttr(f"{foot_ik_ctrl}.toeRoll", f"{toe_add}.input3D[1].input3Dx")
        cmds.connectAttr(f"{foot_mult}.outputY", f"{toe_add}.input3D[2].input3Dx")
        cmds.connectAttr(f"{toe_add}.output3D.output3Dx", f"{toe_pivot_grp}.rotateX")

        cmds.addAttr(foot_ik_ctrl, ln="heelPivot", nn="Heel Pivot", at="float", keyable=True)
        cmds.connectAttr(f"{foot_ik_ctrl}.heelPivot", f"{heel_pivot_grp}.rotateY")

        cmds.addAttr(foot_ik_ctrl, ln="ballPivot", nn="Ball Pivot", at="float", keyable=True)
        cmds.connectAttr(f"{foot_ik_ctrl}.ballPivot", f"{ball_pivot_grp}.rotateY")

        cmds.addAttr(foot_ik_ctrl, ln="toePivot", nn="Toe Pivot", at="float", keyable=True)
        cmds.connectAttr(f"{foot_ik_ctrl}.toePivot", f"{ball_twist_pivot_grp}.rotateY")

        cmds.addAttr(foot_ik_ctrl, ln="tipPivot", nn="Tip Pivot", at="float", keyable=True)
        cmds.connectAttr(f"{foot_ik_ctrl}.tipPivot", f"{toe_pivot_grp}.rotateY")

        cmds.addAttr(foot_ik_ctrl, ln="toeUpDown", nn="Toe Up Down", at="float", keyable=True)
        cmds.connectAttr(f"{foot_ik_ctrl}.toeUpDown", f"{toe_fk_pivot_grp}.translateY")

        # Foot IK Toe Control
        toe_ik_ctrl, toe_ik_ctrl_offset = self.create_rig_control(
            control_base_name=f"{self.toe_proxy.get_name()}_{ik_suffix}",
            curve_file_name="pin",
            parent_obj=foot_ik_ctrl,
            rot_order=0,
            match_obj_pos=ball_jnt,
            add_offset_ctrl=False,
            shape_scale=foot_scale * 0.2,
            color=core_color.get_directional_color(object_name=foot_jnt),
        )[:2]
        cmds.connectAttr(f"{toe_ik_ctrl}.translate", f"{toe_fk_ctrl_grp}.translate")
        cmds.connectAttr(f"{toe_ik_ctrl}.rotate", f"{toe_fk_ctrl_grp}.rotate")
        cmds.addAttr(
            ik_switch_ctrl, ln="footAutomation", nn="Foot Automation", at="enum", en="-------------:", keyable=True
        )
        cmds.setAttr(f"{ik_switch_ctrl}.footAutomation", lock=True)
        cmds.addAttr(ik_switch_ctrl, ln="fullToeCtrlVisibility", nn="Full Toe Ctrl Visibility", at="bool", keyable=True)
        cmds.connectAttr(f"{ik_switch_ctrl}.fullToeCtrlVisibility", f"{toe_ik_ctrl_offset[0]}.visibility")

        # Foot IK Handle
        foot_ik_handle = cmds.ikHandle(
            sj=upperleg_ik, ee=foot_ik, n=f"{_prefix}{self.foot_proxy.get_name()}_ikHandle", sol="ikRPsolver"
        )[0]
        cmds.poleVectorConstraint(lowerleg_ik_ctrl, foot_ik_handle)
        core_hrchy.parent(source_objects=foot_ik_handle, target_parent=ball_pivot_grp)

        # Twist Functionality
        twist_grp = core_hrchy.create_group(name=f"{_prefix}{self.lowerleg_proxy.get_name()}_twistGrp")
        twist_offset_grp = core_hrchy.add_offset_transform(target_list=twist_grp)[0]
        cmds.pointConstraint(upperleg_ik, foot_o_data, twist_offset_grp, mo=False)
        twist_aim_grp = core_hrchy.create_group(name=f"{_prefix}{self.lowerleg_proxy.get_name()}_aimGrp")
        core_hrchy.parent(source_objects=[twist_aim_grp, twist_offset_grp], target_parent=global_offset_ctrl)
        if self.prefix == core_naming.NamingConstants.Prefix.LEFT:
            cmds.setAttr(f"{twist_aim_grp}.translateX", 1100)
        elif self.prefix == core_naming.NamingConstants.Prefix.RIGHT:
            cmds.setAttr(f"{twist_aim_grp}.translateX", -1100)
        cmds.aimConstraint(foot_o_data, twist_offset_grp, wuo=twist_aim_grp, wut=1)
        core_hrchy.parent(source_objects=lowerleg_offset, target_parent=twist_grp)
        cmds.connectAttr(f"{foot_ik_ctrl}.kneeTwist", f"{twist_grp}.rotateX")

        # Ball IK Handle
        toe_ik_handle = cmds.ikHandle(
            sj=foot_ik, ee=ball_ik, n=f"{_prefix}{self.ball_proxy.get_name()}_ikHandle", sol="ikSCsolver"
        )
        core_hrchy.parent(source_objects=toe_ik_handle[0], target_parent=ball_pivot_grp)

        # Toe IK Handle
        toe_ik_handle = cmds.ikHandle(
            sj=ball_ik, ee=toe_ik, n=f"{_prefix}{self.toe_proxy.get_name()}_ikHandle", sol="ikSCsolver"
        )
        core_hrchy.parent(source_objects=toe_ik_handle[0], target_parent=toe_fk_pivot_grp)

        # Lock And Hide Attrs
        core_attr.hide_lock_default_attrs(
            [upperleg_fk_ctrl, lowerleg_fk_ctrl, foot_fk_ctrl, ball_fk_ctrl],
            translate=True,
            scale=True,
            visibility=True,
        )
        core_attr.hide_lock_default_attrs([lowerleg_ik_ctrl], rotate=True, scale=True, visibility=True)
        core_attr.hide_lock_default_attrs([foot_ik_ctrl, toe_ik_ctrl], scale=True, visibility=True)
        core_attr.hide_lock_default_attrs([ik_switch_ctrl], translate=True, rotate=True, scale=True, visibility=True)

        cmds.setAttr(f"{general_automation_grp}.visibility", 0)
        cmds.setAttr(f"{joint_automation_grp}.visibility", 0)

        # Follow Parent Setup
        module_parent = tools_rig_utils.find_joint_from_uuid(self.get_parent_uuid())
        if module_parent:
            for ctrls in [upperleg_fk_ctrl, lowerleg_ik_ctrl, foot_ik_ctrl]:
                core_attr.add_separator_attr(
                    target_object=ctrls, attr_name=core_rigging.RiggingConstants.SEPARATOR_SPACE
                )
            tools_rig_utils.create_follow_enum_setup(
                control=upperleg_fk_ctrl,
                parent_list=[tools_rig_utils.find_joint_from_uuid(self.get_parent_uuid())],
                constraint_type="orient",
            )
            tools_rig_utils.create_follow_enum_setup(
                control=twist_aim_grp,
                attribute_item=lowerleg_ik_ctrl,
                parent_list=[tools_rig_utils.find_joint_from_uuid(self.get_parent_uuid()), foot_ik_ctrl],
                default_value=0,
            )
            tools_rig_utils.create_follow_enum_setup(
                control=foot_ik_ctrl,
                parent_list=[global_offset_ctrl, tools_rig_utils.find_joint_from_uuid(self.get_parent_uuid())],
                default_value=0,
            )
        else:
            tools_rig_utils.create_follow_enum_setup(
                control=twist_aim_grp,
                attribute_item=lowerleg_ik_ctrl,
                parent_list=[foot_ik_ctrl],
                default_value=0,
            )
            tools_rig_utils.create_follow_enum_setup(
                control=foot_ik_ctrl,
                parent_list=[global_offset_ctrl],
                default_value=0,
            )

        # IKFK Switch Locators
        for ik_joint in [upperleg_ik, lowerleg_ik, foot_ik, ball_ik]:
            ik_name = core_node.get_short_name(ik_joint).split("_JNT_ik")[0]
            switch_loc = cmds.spaceLocator(n=f"{ik_name}FkOffsetRef_loc")[0]
            cmds.parent(switch_loc, ik_joint)
            cmds.matchTransform(switch_loc, ik_joint)
            cmds.setAttr(f"{switch_loc}.visibility", 0)

        for fk_joint in [lowerleg_fk, foot_fk, ball_fk]:
            fk_name = core_node.get_short_name(fk_joint).split("_JNT_fk")[0]
            switch_loc = cmds.spaceLocator(n=f"{fk_name}Switch_loc")[0]
            cmds.parent(switch_loc, fk_joint)
            if fk_joint is lowerleg_fk:
                core_trans.match_translate(source=lowerleg_ik_ctrl, target_list=switch_loc)
            else:
                core_trans.match_translate(source=fk_joint, target_list=switch_loc)
            cmds.setAttr(f"{switch_loc}.visibility", 0)

        # Set Children Drivers -----------------------------------------------------------------------------
        self.module_children_drivers = [upperleg_fk_offset[0]]

    def _delete_unbound_joints(self):
        """
        Deletes joints that are usually not bound to the mesh. In this case the toe joint.
        """
        if self.delete_toe_bind_jnt:
            toe_jnt = tools_rig_utils.find_joint_from_uuid(self.toe_proxy.get_uuid())
            if toe_jnt:
                cmds.delete(toe_jnt)

    # ------------------------------------------- Extra Module Setters -------------------------------------------
    def set_post_delete_toe_bind_joint(self, delete_joint):
        """
        Sets a variable to determine if the toe joint should be deleted or not
        Args:
            delete_joint (bool): If True, the toe joint will be deleted after the skeleton and control rig are created.
        """
        if not isinstance(delete_joint, bool):
            logger.warning(f'Unable to set "post_delete_toe_bind_joint". Incompatible data type provided.')
        self.delete_toe_bind_jnt = delete_joint


class ModuleBipedLegLeft(ModuleBipedLeg):
    def __init__(self, name="Left Leg", prefix=core_naming.NamingConstants.Prefix.LEFT, suffix=None):
        super().__init__(name=name, prefix=prefix, suffix=suffix)

        _orientation = tools_rig_frm.OrientationData(aim_axis=(1, 0, 0), up_axis=(0, 0, -1), up_dir=(1, 0, 0))
        self.set_orientation(orientation_data=_orientation)

        # Initial Pose
        overall_pos_offset = core_trans.Vector3(x=10.2)
        upperleg_pos = core_trans.Vector3(y=84.5) + overall_pos_offset
        lowerleg_pos = core_trans.Vector3(y=47.05) + overall_pos_offset
        foot_pos = core_trans.Vector3(y=9.6) + overall_pos_offset
        ball_pos = core_trans.Vector3(z=13.1) + overall_pos_offset
        toe_pos = core_trans.Vector3(z=23.4) + overall_pos_offset
        heel_pos = core_trans.Vector3() + overall_pos_offset

        self.upperleg_proxy.set_initial_position(xyz=upperleg_pos)
        self.lowerleg_proxy.set_initial_position(xyz=lowerleg_pos)
        self.foot_proxy.set_initial_position(xyz=foot_pos)
        self.ball_proxy.set_initial_position(xyz=ball_pos)
        self.toe_proxy.set_initial_position(xyz=toe_pos)
        self.heel_proxy.set_initial_position(xyz=heel_pos)

    def build_skeleton_hierarchy(self):
        super().build_skeleton_hierarchy()


class ModuleBipedLegRight(ModuleBipedLeg):
    def __init__(self, name="Right Leg", prefix=core_naming.NamingConstants.Prefix.RIGHT, suffix=None):
        super().__init__(name=name, prefix=prefix, suffix=suffix)

        _orientation = tools_rig_frm.OrientationData(aim_axis=(-1, 0, 0), up_axis=(0, 0, -1), up_dir=(1, 0, 0))
        self.set_orientation(orientation_data=_orientation)

        # Initial Pose
        overall_pos_offset = core_trans.Vector3(x=-10.2)
        upperleg_pos = core_trans.Vector3(y=84.5) + overall_pos_offset
        lowerleg_pos = core_trans.Vector3(y=47.05) + overall_pos_offset
        foot_pos = core_trans.Vector3(y=9.6) + overall_pos_offset
        ball_pos = core_trans.Vector3(z=13.1) + overall_pos_offset
        toe_pos = core_trans.Vector3(z=23.4) + overall_pos_offset
        heel_pos = core_trans.Vector3() + overall_pos_offset
        bank_left_pos = core_trans.Vector3(z=13.1)
        bank_right_pos = core_trans.Vector3(x=-20.4, z=13.1)

        self.upperleg_proxy.set_initial_position(xyz=upperleg_pos)
        self.lowerleg_proxy.set_initial_position(xyz=lowerleg_pos)
        self.foot_proxy.set_initial_position(xyz=foot_pos)
        self.ball_proxy.set_initial_position(xyz=ball_pos)
        self.toe_proxy.set_initial_position(xyz=toe_pos)
        self.heel_proxy.set_initial_position(xyz=heel_pos)
        self.bank_right_proxy.set_initial_position(xyz=bank_right_pos)
        self.bank_left_proxy.set_initial_position(xyz=bank_left_pos)

    def build_skeleton_hierarchy(self):
        super().build_skeleton_hierarchy()


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)

    # Auto Reload Script - Must have been initialized using "Run-Only" mode.
    from gt.core.session import remove_modules_startswith

    remove_modules_startswith("gt.tools.auto_rigger.module")
    remove_modules_startswith("gt.tools.auto_rigger.rig")
    cmds.file(new=True, force=True)

    import gt.tools.auto_rigger.rig_framework as tools_rig_fmr
    import gt.tools.auto_rigger.rig_utils as tools_rig_utils
    import gt.tools.auto_rigger.module_biped_leg as tools_rig_mod_biped_leg
    import gt.tools.auto_rigger.module_spine as tools_rig_mod_spine
    import gt.tools.auto_rigger.module_root as module_root
    import importlib

    importlib.reload(tools_rig_mod_biped_leg)
    importlib.reload(tools_rig_mod_spine)
    importlib.reload(tools_rig_fmr)
    importlib.reload(tools_rig_utils)

    a_root = module_root.ModuleRoot()
    a_spine = tools_rig_mod_spine.ModuleSpine()
    # a_leg = tools_rig_mod_biped_leg.ModuleBipedLeg()
    a_leg_lf = tools_rig_mod_biped_leg.ModuleBipedLegLeft()
    a_leg_rt = tools_rig_mod_biped_leg.ModuleBipedLegRight()

    root_uuid = a_root.root_proxy.get_uuid()
    spine_upperleg_uuid = a_spine.hip_proxy.get_uuid()
    a_leg_lf.set_parent_uuid(spine_upperleg_uuid)
    a_leg_rt.set_parent_uuid(spine_upperleg_uuid)
    a_spine.set_parent_uuid(root_uuid)
    # a_leg_lf.set_post_delete_toe_bind_joint(False)

    a_project = tools_rig_fmr.RigProject()
    a_project.add_to_modules(a_root)
    a_project.add_to_modules(a_spine)
    a_project.add_to_modules(a_leg_lf)
    a_project.add_to_modules(a_leg_rt)
    a_project.build_proxy()
    # a_project.set_pref_build_control_rig(False)
    # a_project.build_skeleton()
    a_project.build_rig()

    # Frame all
    cmds.viewFit(all=True)
