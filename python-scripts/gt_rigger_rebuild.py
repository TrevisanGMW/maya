"""
GT Rigger - Biped Rigger Re-build Script (Rebuilder)
github.com/TrevisanGMW/gt-tools - 2022-09-28

0.0.1 - 2022-09-28
Created initial setup

0.0.2 to 0.0.3 - 2022-09-30
Added initial control shape extraction
Added data object (control list)

0.0.4 to 0.0.5 - 2022-10-05
Separated extract, re-build and transfer into their own functions


TODO
    Add bound joint extraction
    Add skin weights extraction
    Add control custom attributes extraction
    Add corrective and facial reference position
    Add side GUI, fingers and feet positioning
"""
from gt_rigger_biped_gui import *
from gt_rigger_utilities import *
from gt_rigger_data import *
import maya.cmds as cmds
import logging
import json

# Logging Setup
logging.basicConfig()
logger = logging.getLogger("gt_rigger_rebuild")
logger.setLevel(logging.INFO)

# Data Object
data_rebuild = GTBipedRiggerRebuildData()
if not data_biped:  # Create one in case not already available
    data_biped = GTBipedRiggerData()


def extract_metadata(data_object):
    """ Extracts Rig Metadata """
    proxy_source_obj_name = data_object.proxy_storage_variables.get('source_object_name')
    proxy_attr_name = data_object.proxy_storage_variables.get('attr_name')

    # Source Object Validation
    if not cmds.objExists(proxy_source_obj_name):
        return

    # Source Attribute Validation
    proxy_attr = proxy_source_obj_name + '.' + proxy_attr_name
    if not cmds.objExists(proxy_attr):
        return

    # Attempt to Extract Proxy
    export_dict = cmds.getAttr(proxy_attr)
    try:
        export_dict = json.loads(str(export_dict))
    except Exception as e:
        logger.debug(str(e))

    return export_dict


def transfer_biped_base_settings(data_object, metadata):
    """
    Update base settings so when rebuilding the rig, it will follow the same rules

    ARgs:
        data_object: biped data object, used to build the rig (carry the used settings)
        metadata: Extracted metadata, JSON format containing rigging settings
    """
    to_transfer = ['using_no_ssc_skeleton', 'uniform_ctrl_orient', 'worldspace_ik_orient', 'simplify_spine']
    for option in to_transfer:
        if metadata.get(option) is not None:
            logger.debug(str(option) + ': ' + str(metadata.get(option)))
            data_object.settings[option] = metadata.get(option)


def extract_python_curve_shape_data(curve_transforms):
    """
    Extracts the Python code necessary to reshape
    Args:
        curve_transforms (list of strings): Transforms carrying curve shapes inside them (nurbs or bezier)

    Returns:
        python_string (string): Python code with the current state of the selected curves (their shape)

    Modified version of the function from "gt_shape_extract_shape"
    """
    result = {}

    for crv in curve_transforms:
        valid_types = ['nurbsCurve', 'bezierCurve']
        accepted_shapes = []
        curve_shapes = cmds.listRelatives(crv, shapes=True, fullPath=True) or []
        # Filter valid shapes:
        for shape in curve_shapes:
            current_shape_type = cmds.objectType(shape)
            if current_shape_type in valid_types:
                accepted_shapes.append(shape)

        # Extract CVs into Python code:
        for shape in accepted_shapes:
            extracted_crv_data = zip(cmds.ls('%s.cv[*]' % shape, flatten=True), cmds.getAttr(shape + '.cv[*]'))
            curve_data_list = list(extracted_crv_data)
            if curve_data_list:
                result[str(shape).split('|')[-1]] = curve_data_list
    else:
        return result


def apply_python_curve_shape_data(extracted_shapes):
    """
    Applies JSON data extracted from curves using  extract_python_curve_shape_data
    Args:
        extracted_shapes (json, dict): JSON data extracted using "extract_python_curve_shape_data"
    """
    errors = ''
    for key in extracted_shapes:
        curve_data = extracted_shapes.get(key)
        for cv in curve_data:
            try:
                cmds.xform(cv[0], os=True, t=cv[1])
            except Exception as e:
                error = str(e)
                if ".cv" in str(e):
                    error = error.split('.')[0]
                if error not in errors:
                    errors += error + '\n'

    if errors:
        print("*" * 80)
        print("Errors when updating shapes:")
        print(errors)


def extract_current_rig_data(data_rebuild_object):
    # Find Available Controls
    found_controls = []
    for control in data_rebuild.controls:
        if cmds.objExists(control):
            found_controls.append(control)

    # Missing Main Ctrl - Exit
    if data_rebuild_object.main_ctrl not in found_controls:
        return False

    # Extract Proxy Data
    extracted_proxy_json = extract_metadata(data_biped)  # Re-build proxy
    data_rebuild_object.extracted_proxy_json = extracted_proxy_json

    # Extract Rig Settings
    if find_item(name=data_rebuild_object.main_ctrl, item_type='transform', log_fail=False):
        extracted_biped_metadata = get_metadata(data_rebuild_object.main_ctrl)  # Find previous settings
        data_rebuild_object.extracted_biped_metadata = extracted_biped_metadata

    # Extract Shapes
    data_rebuild_object.extracted_shape_data = extract_python_curve_shape_data(found_controls)


def rebuild_biped_rig(data_rebuild_object):
    print("Run tear down script")
    print("Delete current")

    # Delete current
    rig_root = ''
    if cmds.objExists(data_rebuild_object.rig_root):
        rig_root = data_rebuild_object.rig_root
    else:  # In case default rig root doesn't exist, try to find using skeleton_grp
        skeleton_grp_parent = cmds.listRelatives(data_rebuild_object.skeleton_grp, allParents=True) or []
        print(skeleton_grp_parent)
        if skeleton_grp_parent:
            rig_root = skeleton_grp_parent[0]

    # Couldn't delete the rig, cancel operation
    if not rig_root:
        return False
    else:
        cmds.delete(rig_root)

    print("Rebuild proxy")
    # create_proxy(biped_obj)
    print("Import proxy")
    print("Rebuild Rig")


def transfer_current_rig_data(data_rebuild_object):
    # Transfer Base Settings
    if data_rebuild_object.extracted_proxy_json and data_rebuild_object.extracted_biped_metadata:
        transfer_biped_base_settings(data_biped, data_rebuild_object.extracted_biped_metadata)

    # Transfer Shape Data
    if data_rebuild_object.extracted_shape_data:
        print("Yes")
        apply_python_curve_shape_data(data_rebuild_object.extracted_shape_data)

    print("Run set up script")


# Run
if __name__ == '__main__':
    # data_biped = GTBipedRiggerData()
    # data_facial = GTBipedRiggerFacialData()
    # data_corrective = GTBipedRiggerCorrectiveData()

    logger.setLevel(logging.DEBUG)

    # Extract Data to Rebuild Object
    extract_current_rig_data(data_rebuild)

    # Rebuild RIG if data is available
    rebuild_biped_rig(data_rebuild)

    # Transfer Data to Rebuilt Rig
    transfer_current_rig_data(data_rebuild)