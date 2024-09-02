"""
Skin Module

Code Namespace:
    core_skin  # import gt.core.skin as core_skin
"""

import maya.api.OpenMayaAnim as apiOpenMayaAnim
import maya.api.OpenMaya as apiOpenMaya
import gt.core.feedback as core_fback
import maya.OpenMaya as OpenMaya
import gt.core.io as core_io
import maya.cmds as cmds
import maya.mel as mel
import os.path
import logging

# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def is_mesh_bound(obj):
    """
    Check if the specified object is bound to a skeleton.

    Parameters:
    object_name (str): The name of the object to check.

    Returns:
    bool: True if the object is bound to a skeleton, False otherwise.
    """
    skin_clusters = cmds.ls(cmds.listHistory(obj), type="skinCluster")
    return len(skin_clusters) > 0


def get_skin_cluster(obj):
    """
    Retrieves the skin cluster associated with the given object.

    This function looks for a skin cluster connected to the provided object and returns
    the name of the skin cluster if found.

    Args:
        obj (str): The name of the Maya object, usually a mesh.

    Returns:
        str or None: The name of the skin cluster associated with the given mesh,
                     or None if no skin cluster is found.

    Examples:
        skin_cluster_name = get_skin_cluster(mesh_name)
        print(skin_cluster_name)
    """

    if not cmds.objExists(obj):
        raise ValueError(f'Invalid object name: "{obj}" does not exist.')

    mfn_skin_list = get_mfn_skin_from_geometry(obj)

    if not mfn_skin_list[0]:
        logger.debug(f"No skin clusters attached to the object: '{obj}'")
        return None

    skin_cluster = mfn_skin_list[1]
    return skin_cluster


def get_influences(skin_cluster):
    """
    Retrieves the joint influences associated with the given skin cluster.
    This function returns a list of joint names that influence the specified skin cluster.
    Args:
        skin_cluster (str): The name of the skin cluster to get influences of.

    Returns:
        list[str]: A list of joint names as strings, representing the joints
                   that influence the given skin cluster.

    Examples:
        skin_cluster_name = 'skinCluster1'
        influences = get_influences(skin_cluster_name)
        print(influences)
        ['joint1', 'joint2', 'joint3', ...]
    """
    joints = cmds.skinCluster(skin_cluster, weightedInfluence=True, query=True)
    return joints


def get_bound_joints(obj):
    """
    Gets a list of joints bound to the skin cluster of the object
    Args:
        obj: Name of the object to extract joints from (must contain a skinCluster node)

    Returns:
        list: List of joints bound to this object
    """
    if not cmds.objExists(obj):
        logger.warning(f'Object "{obj}" was not found.')
        return []

    skin_cluster = get_skin_cluster(obj)
    if not skin_cluster:
        logger.debug("skin_clusters: ", str(skin_cluster))
        logger.warning('Object "' + obj + "\" doesn't seem to be bound to any joints.")
        return []
    else:
        influences = get_influences(skin_cluster)
        joints = []
        for obj in influences:
            if cmds.objectType(obj) == "joint":
                joints.append(obj)
        return joints


def get_geos_from_skin_cluster(skin_cluster):
    """
    Retrieve the connected geometry from the given skin cluster.

    This function takes the name of a skin cluster as input and returns a list of connected
    geometry affected by the skin cluster.

    Args:
        skin_cluster (str): The name of the skin cluster to query.

    Returns:
        list: A list of strings containing the names of connected geometries affected by the skin cluster.

    Raises:
        ValueError: If the provided skin cluster name does not exist in the scene.

    Example:
        # Get the skin cluster name
        skin_cluster_name = "skinCluster1"
        # Retrieve connected geometry
        affected_geometry_list = get_skin_cluster_geometry(skin_cluster_name)
        print(affected_geometry_list)
        # Output: ['pCube1', 'pSphere1', 'pCylinder1']
    """

    if not cmds.objExists(skin_cluster):
        raise ValueError(f'Invalid skin cluster name: "{skin_cluster}" does not exist.')

    affected_geometry_list = []
    mfn_skin_cluster = get_mfn_skin_from_skin_cluster(skin_cluster)
    input_plugs = mfn_skin_cluster.findPlug("input", False)
    input_nums = input_plugs.evaluateNumElements()

    for inp_num in range(input_nums):
        shape_obj = mfn_skin_cluster.inputShapeAtIndex(inp_num)
        shape_dag_path = OpenMaya.MDagPath.getAPathTo(shape_obj)
        transform_dag_path = OpenMaya.MDagPath(shape_dag_path)
        transform_dag_path.pop()
        affected_geometry_list.append(transform_dag_path.partialPathName())

    return affected_geometry_list


def get_skin_weights(skinned_mesh):
    """
    Retrieve skin weights data from a given skinned mesh.
    This function returns skin weight information for each vertex analysing the skin cluster
    related to the supplied skinned mesh.
    The skin weights represent the influence of each bone (influence object) on the vertices of the mesh.

    Args:
        skinned_mesh (str): The name of the skinned mesh

    Raises:
        ValueError: If the provided skin_cluster does not exist in the scene.

    Returns:
        dict: A dictionary containing skin weight data for each vertex in the skin cluster. The dictionary is
        structured as follows:

        {
            0: {'joint1': 0.75, 'joint2': 0.25},
            1: {'joint2': 1.0},
            2: {'joint3': 0.5, 'joint1': 0.5},
            ...
        }
        This data assigns the weights for each vertex (index 0, 1, 2, ...) to the respective joints.

    Example:
        # Assuming a valid 'pCube1' exists in the scene.
        weights_data = get_skin_weights('pCube1')
        # Resulting output will be a dictionary containing skin weight data for each vertex in the cluster.
    """
    if not cmds.objExists(skinned_mesh):
        raise ValueError("Mesh '{}' does not exist.".format(skinned_mesh))

    vertices_num = cmds.polyEvaluate(skinned_mesh, v=True)

    # get om2 mfn_skin_cluster
    sel_list = apiOpenMaya.MSelectionList()
    sel_list.add(skinned_mesh)
    mesh_dag = sel_list.getDagPath(0)
    mfn_skin_cluster, skin_cluster_name = get_mfn_skin_from_geometry(skinned_mesh)

    if not skin_cluster_name:
        raise ValueError("Mesh '{}' does not have a skin cluster.".format(skinned_mesh))

    # get om2 mfn mesh components
    components_ids = [c for c in range(vertices_num)]
    mfn_single_component = apiOpenMaya.MFnSingleIndexedComponent()
    mesh_vert_component = mfn_single_component.create(apiOpenMaya.MFn.kMeshVertComponent)
    mfn_single_component.addElements(components_ids)

    # get weights from the skin cluster
    weights, inf_num = mfn_skin_cluster.getWeights(mesh_dag, mesh_vert_component)

    # get the plugs for the influences
    weight_plug = mfn_skin_cluster.findPlug("weights", False)
    list_plug = mfn_skin_cluster.findPlug("weightList", False).attribute()
    inf_dags = mfn_skin_cluster.influenceObjects()
    inf_num = len(inf_dags)
    inf_names = [inf_dag.partialPathName() for inf_dag in inf_dags]
    sparse_map = {mfn_skin_cluster.indexForInfluenceObject(inf_dag): i for i, inf_dag in enumerate(inf_dags)}

    # create the dictionary for the skin data
    skin_data = {}
    for comp_id, vertex_num in enumerate(components_ids):
        weight_plug.selectAncestorLogicalIndex(vertex_num, list_plug)
        valid_ids = weight_plug.getExistingArrayAttributeIndices()

        # bitwise operation to ignore false positives if any
        valid_ids = set(valid_ids) & sparse_map.keys()

        comp_weights = {}
        flat_index = int(comp_id) * inf_num
        for valid_id in valid_ids:
            inf_index = sparse_map[valid_id]
            comp_weights[inf_names[inf_index]] = weights[flat_index + inf_index]

        skin_data[vertex_num] = comp_weights

    return skin_data


def set_skin_weights(skinned_mesh, skin_data, remove_unused_inf=True):
    """
    Sets the skin weights from a skin_data dictionary.

    Args:
        skinned_mesh (str): name of the skinned mesh to apply weights to.
        skin_data (dict): skin data dictionary that follows the pattern described in get_skin_weights.
        remove_unused_inf (boolean): removes unused influences at the end of the process

    Raises:
        ValueError: If the influences between the skin data and the skin cluster of the mesh are not matching.

    Example:
        The skin_data should look like this:
        {
            0: {'joint1': 0.75, 'joint2': 0.25},
            1: {'joint2': 1.0},
            2: {'joint3': 0.5, 'joint1': 0.5},
            ...
        }
        This data assigns the weights for each vertex (index 0, 1, 2, ...) to the respective joints.
    """
    if not cmds.objExists(skinned_mesh):
        raise ValueError(f"Mesh '{skinned_mesh}' does not exist.")

    sel_list = apiOpenMaya.MSelectionList()
    sel_list.add(skinned_mesh)
    mesh_dag = sel_list.getDagPath(0)
    mfn_skin_cluster, skin_cluster_name = get_mfn_skin_from_geometry(skinned_mesh)

    if not skin_cluster_name:
        raise ValueError(f"Mesh '{skinned_mesh}' does not have a skin cluster.")

    # get influences dictionary
    inf_dags = mfn_skin_cluster.influenceObjects()
    inf_count = len(inf_dags)
    inf_dict = {i_dag.partialPathName(): i_index for i_index, i_dag in enumerate(inf_dags)}

    # get influences indices MIntArray
    inf_indices = apiOpenMaya.MIntArray(len(inf_dags), 0)
    for x in range(len(inf_dags)):
        inf_indices[x] = int(mfn_skin_cluster.indexForInfluenceObject(inf_dags[x]))

    data_inf_list = get_influences_from_skin_data(skin_data)

    inf_missing = []
    for inf_name in data_inf_list:
        if inf_name not in list(inf_dict.keys()):
            inf_missing.append(inf_name)

    if inf_missing:
        raise ValueError(
            f"The skinCluster '{skin_cluster_name}' does not have the following influences:\n {str(inf_missing)}"
        )

    skin_data = {int(key): value for key, value in skin_data.items()}  # Without this JSON converted dictionaries break
    skin_data_vertices = sorted(list(skin_data.keys()))
    skin_data_vertices = sorted(skin_data_vertices)

    # initialize MDoubleArray for the weights
    weights = apiOpenMaya.MDoubleArray(len(skin_data_vertices) * inf_count, 0)

    # get om2 mfn mesh components
    vertices_num = cmds.polyEvaluate(skinned_mesh, v=True)
    components_ids = [c for c in range(vertices_num)]
    mfn_single_component = apiOpenMaya.MFnSingleIndexedComponent()
    mesh_vert_component = mfn_single_component.create(apiOpenMaya.MFn.kMeshVertComponent)
    mfn_single_component.addElements(components_ids)

    for data_i, vertex_num in enumerate(skin_data_vertices):
        start_id = data_i * inf_count

        for inf_name, weight in skin_data[vertex_num].items():
            inf_id = inf_dict[inf_name]

            # populate correctly the weights double array for the skin cluster
            weights[start_id + inf_id] = weight

    # set skin weights
    normalize = False
    return_old_weights = False

    mfn_skin_cluster.setWeights(mesh_dag, mesh_vert_component, inf_indices, weights, normalize, return_old_weights)
    logger.info(f"Successfully set weights for supplied mesh {skinned_mesh}.")

    if remove_unused_inf:
        remove_unused_influences(skin_cluster_name)
        logger.info(f"Successfully removed unused influences within {skin_cluster_name}.")


def get_influences_from_skin_data(skin_data):
    """
    Gets the influences (joint names) inside the supplied skin data.

    Args:
        skin_data (dict): check get_skin_weights for the pattern to use

    Returns:
        skin_influences (list)
    """
    skin_influences = []
    for vert, weights in skin_data.items():
        vert_inf = list(weights.keys())
        [skin_influences.append(vi) for vi in vert_inf if vi not in skin_influences]

    if skin_influences:
        skin_influences.sort()

    return skin_influences


def import_skin_weights_from_json(target_object, import_file_path):
    """
    Imports skin weights from a JSON file and applies them to the specified target object's skin cluster.

    Args:
        target_object (str): The name or reference of the target object to apply the skin weights to.
        import_file_path (str): The file path of the JSON file containing the skin weight data.

    Raises:
        IOError: If the JSON file cannot be read or is not found.

    Note:
        This function assumes that the JSON file contains data matching the pattern found in  "get_skin_weights()".
    """
    skin_data = core_io.read_json_dict(path=import_file_path)
    set_skin_weights(target_object, skin_data)


def bind_skin(joints, objects, bind_method=1, smooth_weights=0.5, maximum_influences=4):
    """
    Binds the specified joints to the given objects using the skinCluster command in Maya.

    Args:
        joints (list): A list of joint names to be used as influences in the skinCluster.
        objects (list, str): A list of object names (geometries) to bind the skin to.
                              If a string it becomes a list with a single element in it. e.g. [objects]
        bind_method (int, optional): The binding method used by the skinCluster command.
                                    Default is 1, which stands for 'Classic Linear'.
                                    Other options are available based on the Maya documentation.
        smooth_weights (float, optional): The smoothness level of the skin weights.
                                         It should be a value between 0.0 and 1.0.
                                         Default is 0.5.
        maximum_influences (int, optional): The maximum number of joint influences allowed per vertex.
                                           Default is 4.

    Returns:
        list: A list of skinCluster node names created during the binding process.

    Example:
        # Bind 'joints_list' to 'objects_list' with the default binding settings:
        result = bind_skin(joints_list, objects_list)

        # Bind 'joints_list' to 'objects_list' with custom binding options:
        result = bind_skin(joints_list, objects_list, bind_method=2, smooth_weights=0.8, maximum_influences=3)
    """
    if isinstance(objects, str):
        objects = [objects]
    current_selection = cmds.ls(selection=True) or []
    skin_nodes = []
    joints_found = []
    joints_missing = []
    objects_found = []
    objects_missing = []
    # Determine Existing Objects
    for jnt in joints:
        if cmds.objExists(jnt):
            joints_found.append(jnt)
        else:
            joints_missing.append(jnt)
    for geo in objects:
        if cmds.objExists(geo):
            objects_found.append(geo)
        else:
            objects_missing.append(geo)
    if objects_missing:
        logger.warning(f'Skin bound operation had missing objects: "{", ".join(objects_missing)}".')
    if joints_missing:
        logger.warning(f'Skin bound operation had missing joints: "{", ".join(joints_missing)}".')
    # Bind objects
    for geo in objects_found:
        skin_node = (
            cmds.skinCluster(
                joints_found,
                geo,
                obeyMaxInfluences=True,
                bindMethod=bind_method,
                toSelectedBones=True,
                smoothWeights=smooth_weights,
                removeUnusedInfluence=False,
                maximumInfluences=maximum_influences,
            )
            or []
        )
        if skin_node:
            skin_nodes.extend(skin_node)

    if current_selection:
        try:
            cmds.select(current_selection)
        except Exception as e:
            logger.debug(f"Unable to recover previous selection. Issue: {str(e)}")
    return skin_nodes


def get_python_influences_code(obj_list, include_bound_mesh=True, include_existing_filter=True):
    """
    Extracts the python code necessary to select influence joints. (bound joints)
    Args:
        obj_list (list, str): Items to extract influence from. If a string is provided it becomes a list with one item.
        include_bound_mesh (bool, optional): If active, it will include the bound mesh in the return list.
        include_existing_filter (bool, optional): If active, it will include a filter for existing items.
    Returns:
        str or None: Returns the code to select influence joints or None there was an issue.
    """
    if isinstance(obj_list, str):
        obj_list = [obj_list]
    valid_nodes = []
    for obj in obj_list:
        shapes = cmds.listRelatives(obj, shapes=True, children=False, fullPath=True) or []
        if shapes:
            if cmds.objectType(shapes[0]) == "mesh" or cmds.objectType(shapes[0]) == "nurbsSurface":
                valid_nodes.append(obj)

    commands = []
    for transform in valid_nodes:
        message = '# Joint influences found in "' + transform + '":'
        message += "\nbound_list = "
        bound_joints = get_bound_joints(transform)

        if not bound_joints:
            cmds.warning('Unable to find skinCluster for "' + transform + '".')
            continue

        if include_bound_mesh:
            bound_joints.insert(0, transform)

        message += str(bound_joints)

        if include_existing_filter:
            message += "\nbound_list = [jnt for jnt in bound_list if cmds.objExists(jnt)]"

        message += "\ncmds.select(bound_list)"

        commands.append(message)

    _code = ""
    for cmd in commands:
        _code += cmd + "\n\n"
    if _code.endswith("\n\n"):  # Removes unnecessary spaces at the end
        _code = _code[:-2]
    return _code


def selected_get_python_influences_code(include_bound_mesh=True, include_existing_filter=True):
    """
    Uses selection when extracting influence joints python code.
    Args:
        include_bound_mesh (bool, optional): If active, it will include the bound mesh in the return list.
        include_existing_filter (bool, optional): If active, it will include a filter for existing items.
    Returns:
        str or None: Returns the code to select influence joints or None there was an issue.
    """
    sel = cmds.ls(selection=True) or []

    if len(sel) == 0:
        cmds.warning("Nothing selected. Please select a bound mesh and try again.")
        return
    return get_python_influences_code(
        obj_list=sel, include_bound_mesh=include_bound_mesh, include_existing_filter=include_existing_filter
    )


def add_influences_to_set(obj_list, include_bound_mesh=True, set_suffix="influenceSet"):
    """
    Create selection sets with the influence joints of the provided elements.
    Args:
        obj_list (list, str): Items to extract influence from. If a string is provided it becomes a list with one item.
        include_bound_mesh (bool, optional): If active, it will include the bound mesh in the set.
        set_suffix (str, optional): Added as a suffix to the created set.
    Returns:
        list: A list of created selection sets (sorted list)
    """
    selection_sets = set()
    if isinstance(obj_list, str):
        obj_list = [obj_list]
    valid_nodes = []
    for obj in obj_list:
        shapes = cmds.listRelatives(obj, shapes=True, children=False) or []
        if shapes:
            if cmds.objectType(shapes[0]) == "mesh" or cmds.objectType(shapes[0]) == "nurbsSurface":
                valid_nodes.append(obj)

    for transform in valid_nodes:
        bound_joints = get_bound_joints(transform)
        if include_bound_mesh:
            bound_joints.insert(0, transform)
        new_set = cmds.sets(name=f"{transform}_{set_suffix}", empty=True)
        for jnt in bound_joints:
            selection_sets.add(cmds.sets(jnt, add=new_set))
    return sorted(list(selection_sets))


def selected_add_influences_to_set():
    """
    Uses selection when extracting influence joints to a selection set.
    Returns:
        str or None: Returns the code to select influence joints or None there was an issue.
    """
    sel = cmds.ls(selection=True) or []

    if len(sel) == 0:
        cmds.warning("Nothing selected. Please select a bound mesh and try again.")
        return
    return add_influences_to_set(sel)


#  TODO: Not yet tested --------------------------------------------------------------------------------------------
def export_influences_to_target_folder(obj_list, target_folder, verbose=False):
    """
    WIP Function
        TODO:
            add existing checks
            extract maximum influences and skin cluster options
            extract target name
    """

    if isinstance(obj_list, str):  # If a string is provided, convert it to list
        obj_list = [obj_list]

    if not os.path.exists(target_folder) or not os.path.isdir(target_folder):
        logger.warning(f"Unable to export influences. Missing target folder: {str(target_folder)}")
        return

    exported_files = set()
    for obj in obj_list:
        file_name = f"influences_{obj}.json"
        file_path = os.path.join(target_folder, file_name)
        joints = get_influences(get_skin_cluster(obj))
        influences_dict = {"obj_name": obj, "influences": joints}
        json_file = core_io.write_json(path=file_path, data=influences_dict)
        if json_file:
            exported_files.add(json_file)
            core_fback.print_when_true(
                input_string=f'Influences for "{obj}" exported to "{json_file}".', do_print=verbose
            )
    return list(exported_files)


def import_influences_from_target_folder(source_folder, verbose=False):
    """
    WIP
    TODO:
        Check if exists, add existing checks, check pattern before using it
    """

    if not os.path.exists(source_folder) or not os.path.isdir(source_folder):
        logger.warning(f"Unable to import influences. Missing source folder: {str(source_folder)}")
        return

    for source_file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, source_file_name)
        influences_dict = core_io.read_json_dict(file_path)
        obj_name = influences_dict.get("obj_name")
        joints = influences_dict.get("influences")
        bind_skin(joints, [obj_name])
        core_fback.print_when_true(
            input_string=f'Influences for {obj_name} imported from "{source_file_name}".', do_print=verbose
        )


def export_weights_to_target_folder(obj_list, target_folder, verbose=False, file_format=".json"):
    """
    WIP
    TODO:
        Check if exists, add existing checks, check pattern before using it Add suffix?
    """
    if isinstance(obj_list, str):  # If a string is provided, convert it to list
        obj_list = [obj_list]

    if not os.path.exists(target_folder) or not os.path.isdir(target_folder):
        logger.warning(f"Unable to export skin weights. Missing target folder: {str(target_folder)}")
        return

    exported_files = set()
    for obj in obj_list:
        import gt.core.naming as core_naming

        file_name = f"weights_{core_naming.get_short_name(obj)}.{file_format}"
        file_path = os.path.join(target_folder, file_name)
        skin_weights_data = get_skin_weights(obj)
        json_file = core_io.write_json(path=file_path, data=skin_weights_data)
        if json_file:
            exported_files.add(json_file)
            core_fback.print_when_true(input_string=f'Weights for "{obj}" exported to "{json_file}".', do_print=verbose)
    return list(exported_files)


def import_weights_from_target_folder(obj_list, target_folder, remove_unused_inf=True):
    """
    Imports the skin weights from a target folder.

    Args:
        obj_list (list): list of skinned meshes
        target_folder (string): folder path with exported skin data files
        remove_unused_inf (bool): remove unused influences after the process

    Returns:

    """
    import gt.core.joint as core_joint
    import gt.core.scene as core_scene

    if not os.path.exists(target_folder) or not os.path.isdir(target_folder):
        logger.warning(f"Unable to export skin weights. Missing target folder: {str(target_folder)}")
        return

    data_file_prefix = "weights_"
    data_file_ext = ".json"
    available_meshes_in_data = []
    weights_data = {}

    for weights_file_name in os.listdir(target_folder):
        if weights_file_name.startswith(data_file_prefix) and weights_file_name.endswith(data_file_ext):
            file_path = os.path.join(target_folder, weights_file_name)
            json_weights_dict = core_io.read_json_dict(file_path)

            # fix json string dictionary keys back to int
            weights_dict = {}
            for k, v in json_weights_dict.items():
                weights_dict[int(k)] = v

            data_mesh_name = weights_file_name.replace(data_file_prefix, "").replace(data_file_ext, "")
            available_meshes_in_data.append(data_mesh_name)
            weights_data[data_mesh_name] = weights_dict

    for obj in obj_list:
        if not cmds.objExists(obj):
            logger.warning(f"Skipped set weights for supplied mesh {obj}")
            continue

        skin_cluster_name = mel.eval('findRelatedSkinCluster "{}"'.format(obj))
        if not skin_cluster_name:
            logger.warning(f"Skipped set weights for supplied mesh {obj}. The SkinCluster is missing.")
            continue

        # set skin weights
        if obj in available_meshes_in_data:

            try:
                set_skin_weights(obj, weights_data[obj], remove_unused_inf=remove_unused_inf)

            except Exception as e:
                print(e)
                if "kInvalidParameter" not in str(e):
                    logger.error(e)
                    logger.warning(f"Skipped set weights for supplied mesh {obj}. Errors occur.")

                else:
                    # root joint from current influences
                    first_key = list(weights_data[obj].keys())[0]
                    first_joint = list(weights_data[obj][first_key].keys())[0]
                    root_joint = core_joint.get_root_from_joint(first_joint)
                    joint_hierarchy = core_scene.get_hierarchy(root_joint, maya_type=OpenMaya.MFn.kJoint)
                    # re-bind
                    cmds.delete(obj, constructionHistory=True)
                    bind_skin(joint_hierarchy, [obj])
                    logger.info(f"Unused influences were removed. Successfully re-bound {obj} to the skeleton.")
                    set_skin_weights(obj, weights_data[obj], remove_unused_inf=remove_unused_inf)

        else:
            logger.warning(f"Skipped set weights for supplied mesh {obj}. Data not found.")


def get_mfn_skin_from_skin_cluster(skin_cluster):
    """
    Returns the MObject related to the supplied skinCluster node.
    Args:
        skin_cluster (string): skin cluster name

    Returns:
        mfn_skin_cluster (MObject)
    """
    # get om2 mfn_skin_cluster
    sel_list = apiOpenMaya.MSelectionList()
    sel_list.add(skin_cluster)
    skin_cluster_dep = sel_list.getDependNode(0)
    mfn_skin_cluster = apiOpenMayaAnim.MFnSkinCluster(skin_cluster_dep)

    return mfn_skin_cluster


def get_mfn_skin_from_geometry(skinned_mesh):
    """
    Returns skin cluster MObject related to the supplied mesh

    Args:
        skinned_mesh (string): skinned mesh name

    Returns:
      -  skinCluster:   MFnSkinCluster      Maya skin cluster function set
      -  skinName:      string              DG name of skinCluster
    """
    skin_cluster_name = mel.eval('findRelatedSkinCluster "{}"'.format(skinned_mesh))
    mfn_skin_cluster = get_mfn_skin_from_skin_cluster(skin_cluster_name)

    return mfn_skin_cluster, skin_cluster_name


def get_unused_influences(skin_cluster):
    """
    Gets the unused influences as dagPaths.

    Args:
        skin_cluster: skin cluster node name

    Returns:
        unused_influences (dagPaths)
    """
    unused_influences = []
    mfn_skin_cluster = get_mfn_skin_from_skin_cluster(skin_cluster)
    influences = mfn_skin_cluster.influenceObjects()

    for inf in influences:
        comp_path, weights = mfn_skin_cluster.getPointsAffectedByInfluence(inf)

        if comp_path.length() == 0:
            unused_influences.append(inf)

    return unused_influences


def remove_unused_influences(skin_cluster):
    """
    Removes unused influences in a skin cluster.

    Args:
        skin_cluster: skin cluster node name
    """
    unused_influences = get_unused_influences(skin_cluster)
    if unused_influences:
        for inf in unused_influences:
            cmds.skinCluster(skin_cluster, edit=True, removeInfluence=inf.fullPathName())


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)

    import json

    skin_data_test = get_skin_weights(skinned_mesh="cylinder")
    print(skin_data_test)
    test_export_json = json.dumps(skin_data_test)
    test_import_json = json.loads(test_export_json)
    print(test_import_json)
    set_skin_weights(skinned_mesh="cylinder", skin_data=test_import_json)
