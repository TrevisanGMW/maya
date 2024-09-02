"""
Auto Rigger Utils Modules
"""

import gt.tools.auto_rigger.rig_constants as tools_rig_const
import gt.tools.auto_rigger.rig_framework as tools_rig_frm
import gt.tools.auto_rigger.rig_utils as tools_rig_utils
import gt.ui.resource_library as ui_res_lib
import gt.core.hierarchy as core_hrchy
import gt.core.naming as core_naming
import gt.core.scene as core_scene
import gt.core.skin as core_skin
import gt.core.io as core_io
import maya.cmds as cmds
import logging
import os

# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ModuleNewScene(tools_rig_frm.ModuleGeneric):
    __version__ = "0.0.1-alpha"
    icon = ui_res_lib.Icon.rigger_module_new_scene
    allow_parenting = False
    allow_multiple = True

    def __init__(self, name="New Scene", prefix=None, suffix=None):
        super().__init__(name=name, prefix=prefix, suffix=suffix)
        self.orientation = None  # Changed to None so it doesn't get serialized.
        self.set_extra_callable_function(self._force_new_scene, order=tools_rig_frm.CodeData.Order.pre_proxy)
        self.scene_options = {}

    def _force_new_scene(self):
        """
        Use maya commands to trigger a new scene without asking if the user wants to save current work.
        If initial scene options were provided, these are set after starting a new scene.
        """
        cmds.file(new=True, force=True)
        if self.scene_options:
            self.apply_scene_options()

    def set_scene_options(self, scene_options_dict):
        """
        Sets the initial options dictionary for the scene.
        The keys are the name of the attributes/options that will be affected.
        The values are the desired preferences.
        Example:
            scene_options_dict = {
            "linear_unit": "centimeter",
            "angular_unit": "degree",
            "frame_rate": "30fps",
            "multi_sample": True,
            "multi_sample_count": 8,
            "persp_clip_plane_near": 0.1,
            "persp_clip_plane_far": 10000.0,
            "display_textures": True,
            "playback_frame_start": 1,
            "playback_frame_end": 120,
            "animation_frame_start": 1,
            "animation_frame_end": 200,
            "current_time": 1,
            }

        Args:
            scene_options_dict: A dictionary describing the initial values of a scene.
        """
        if not scene_options_dict or not isinstance(scene_options_dict, dict):
            logger.warning(f"Unable to set attribute values dictionary. Incorrect input type.")
            return
        self.scene_options = scene_options_dict

    def apply_scene_options(self):
        """
        Applies the stored scene options.
        """
        # Set Scene Linear Unit (Scale)
        option_key = "linear_unit"
        if option_key in self.scene_options:
            cmds.currentUnit(linear=self.scene_options.get(option_key))

        # Set Scene Angular Unit
        option_key = "angular_unit"
        if option_key in self.scene_options:
            cmds.currentUnit(angle=self.scene_options.get(option_key))

        # Set scene frame-rate
        option_key = "frame_rate"
        if option_key in self.scene_options:
            core_scene.set_frame_rate(self.scene_options.get(option_key))

        # Set the multi-sample count (multisampling anti-aliasing level)
        option_key = "multi_sample"
        if option_key in self.scene_options:
            _value = self.scene_options.get(option_key)
            cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", _value)
        option_key = "multi_sample_count"
        if option_key in self.scene_options:
            _value = self.scene_options.get(option_key)
            cmds.setAttr("hardwareRenderingGlobals.multiSampleCount", _value)

        # Persp Camera Setup
        option_key = "persp_clip_plane_near"
        if option_key in self.scene_options:
            _value = self.scene_options.get(option_key)
            cmds.setAttr("perspShape.nearClipPlane", _value)
        option_key = "persp_clip_plane_far"
        if option_key in self.scene_options:
            _value = self.scene_options.get(option_key)
            cmds.setAttr("perspShape.farClipPlane", _value)

        # Enable texture visibility
        option_key = "display_textures"
        if option_key in self.scene_options and self.scene_options.get(option_key) is True:
            all_viewports = cmds.getPanel(type="modelPanel")
            # Iterate through each viewport and enable texture display
            for viewport in all_viewports:
                cmds.modelEditor(viewport, edit=True, displayTextures=True)

        # Playback Start and End
        option_key = "playback_frame_start"
        if option_key in self.scene_options:
            cmds.playbackOptions(min=self.scene_options.get(option_key))
        option_key = "playback_frame_end"
        if option_key in self.scene_options:
            cmds.playbackOptions(max=self.scene_options.get(option_key))

        # Animation Start and End
        option_key = "animation_frame_start"
        if option_key in self.scene_options:
            cmds.playbackOptions(animationStartTime=self.scene_options.get(option_key))
        option_key = "animation_frame_end"
        if option_key in self.scene_options:
            cmds.playbackOptions(animationEndTime=self.scene_options.get(option_key))

        # Current Time
        option_key = "current_time"
        if option_key in self.scene_options:
            cmds.currentTime(self.scene_options.get(option_key))


class ModulePython(tools_rig_frm.ModuleGeneric):
    __version__ = "0.0.1-alpha"
    icon = ui_res_lib.Icon.rigger_module_python
    allow_parenting = False
    allow_multiple = True

    def __init__(self, name="Python", prefix=None, suffix=None):
        super().__init__(name=name, prefix=prefix, suffix=suffix)
        self.orientation = None  # Changed to None so it doesn't get serialized.
        self.code = tools_rig_frm.CodeData()
        self.code.set_execution_code("")
        self.code.set_order(tools_rig_frm.CodeData.Order.post_build)

    def set_execution_code(self, code):
        """
        Sets a stored string that is used as python code.
        Args:
            code (str): A string to be executed as python code.
        """
        self.code.set_execution_code(code=code)


class ModuleImportFile(tools_rig_frm.ModuleGeneric):
    __version__ = "0.0.1-alpha"
    icon = ui_res_lib.Icon.rigger_module_import_file
    allow_parenting = False
    allow_multiple = True

    def __init__(self, name="Import File", prefix=None, suffix=None):
        super().__init__(name=name, prefix=prefix, suffix=suffix)
        self.orientation = None  # Changed to None so it doesn't get serialized.
        # Import Preferences
        self.file_path = ""
        self.file_type = None  # The type of the file (e.g., "OBJ", "mayaAscii").
        self.namespace = None  # Namespace for the imported objects.
        self.merge_namespaces_on_clash = False  # If True, merges namespaces on name clash.
        self.reference = False  # If True imports as a reference
        self.set_extra_callable_function(self._import_file, order=tools_rig_frm.CodeData.Order.post_skeleton)
        self._imported_cache = []  # A list of imported objects (only populated after first call)
        self.transforms_parent = None

    def _import_file(self):
        """
        Use maya commands to import a file into the current scene.
        When executed, this function stores the name of the imported elements in the "self._imported_cache" variable.
        """
        # Initial Check
        _parsed_path = self._parse_path(path=self.file_path)
        if not os.path.exists(_parsed_path):
            logger.warning(f'Unable to import missing file. Path: "{str(_parsed_path)}".')
            return
        # Extra Parameters
        extra_params = {}
        if self.file_type is not None:
            extra_params["typ"] = self.file_type
        if self.namespace is not None:
            extra_params["namespace"] = self.namespace
        if self.merge_namespaces_on_clash is not None:
            extra_params["mergeNamespacesOnClash"] = self.merge_namespaces_on_clash
        # Importing or Referencing
        if self.reference is not None and self.reference is True:
            extra_params["reference"] = self.reference  # Cannot be called at the same time as i=True
        else:
            extra_params["i"] = True  # (i=True is the long name for "import")
        # Import Function Call
        try:
            self._imported_cache = cmds.file(_parsed_path, returnNewNodes=True, **extra_params) or []
        except Exception as e:
            logger.warning(f"Unable to import file. Issue: {str(e)}.")
        # Re-parent transforms
        try:
            if self._imported_cache and self.transforms_parent:
                if not cmds.objExists(self.transforms_parent):
                    logger.warning(
                        f'Unable to re-parent imported transforms. Missing target object: "self.transforms_parent".'
                    )
                    return
                _transforms = cmds.ls(self._imported_cache, typ="transform")
                for trans in _transforms:
                    cmds.parent(trans, self.transforms_parent)
        except Exception as e:
            logger.warning(f"Unable to re-parent imported transforms. Issue: {str(e)}.")

    # ------------------------------------------- Extra Module Setters ------------------------------------------
    def set_file_path(self, file_path):
        """
        Sets the path used to import a file.
        Args:
            file_path (str): A file path to be imported. it overwrites the value even if an empty string.
        """
        if file_path is None:
            self.file_path = ""
        if not isinstance(file_path, str):
            logger.warning("Unable to set file path. Invalid data type was provided.")
            return
        self.file_path = file_path

    def set_file_type(self, file_type):
        """
        Sets the path used to import a file.
        Set the type of this file. By default, this can be any one of: "mayaAscii", "mayaBinary", "mel", "OBJ",
        "directory", "plug-in", "audio", "move", "EPS", "Adobe(R) Illustrator(R)", "image".
        Plug-ins may define their own types as well. e.g. "FBX"

        Args:
            file_type (str, None): A file type to be imported. If empty or None the value is cleared and a
                                   file type is considered to not be defined.
        """
        if file_type is None or file_type == "":
            self.file_type = None
            return
        if not isinstance(file_type, str):
            logger.warning("Unable to set file type. Invalid data type was provided.")
            return
        self.file_type = file_type

    def set_namespace(self, namespace):
        """
        Sets the namespace used by the imported elements.
        The new namespace will be created by this command and can not already exist. The old namespace will be removed.

        Args:
            namespace (str, None): A file type to be imported. If empty or None the value is cleared and a
                                   file type is considered to not be defined.
        """
        if namespace is None or namespace == "":
            self.namespace = None
            return
        if not isinstance(namespace, str):
            logger.warning("Unable to set namespace. Invalid data type was provided.")
            return
        self.namespace = namespace

    def set_merge_namespaces_on_clash(self, merge_namespaces_on_clash):
        """
        Used with the -import or -reference flag to prevent new namespaces from being created when namespaces of
        the same name already exist within Maya. For example, lets pretend a file being imported refers to
        "ref:pSphere1" and there is already a namespace called "ref" defined in Maya.
        If -mergeNamespacesOnClash is true, the existing ref namespace will be reused and pSphere1 will be moved
        into the existing namespace. If -mergeNamespacesOnClash is false, a new namespace will be created
        (in this case "ref1") and "pShere1" moved into the ref1 namespace. The default value is false.

        Args:
            merge_namespaces_on_clash (bool): If True, merge namespaces on clash. Read above for more details.
        """
        if not isinstance(merge_namespaces_on_clash, bool):
            logger.warning('Unable to set "merge namespaces on clash" state. Invalid data type was provided.')
            return
        self.merge_namespaces_on_clash = merge_namespaces_on_clash

    def set_reference(self, reference):
        """
        Determines if it should create a reference to the specified file instead of just importing.
        Args:
            reference (bool): If True, imported file will be referenced instead of simply imported.
        """
        if not isinstance(reference, bool):
            logger.warning('Unable to set "reference" state. Invalid data type was provided.')
            return
        self.reference = reference

    def set_transforms_parent(self, transforms_parent):
        """
        Sets a parent for the imported transforms.
        Args:
            transforms_parent (str, None): New parent of the imported elements. If a name is provided, and it's
                                           available in the scene, all imported transforms are re-parented to be
                                           children of this element.
        """
        if transforms_parent is None:
            self.transforms_parent = None  # Clear transforms_parent
            return
        if not isinstance(transforms_parent, str):
            logger.warning("Unable to set transforms parent. Invalid data type was provided.")
            return
        self.transforms_parent = transforms_parent


class ModuleSkinWeights(tools_rig_frm.ModuleGeneric):
    __version__ = "0.0.1-alpha"
    icon = ui_res_lib.Icon.rigger_module_skin_weights
    allow_parenting = False
    allow_multiple = True

    def __init__(self, name="Skin Weights", prefix=None, suffix=None):
        super().__init__(name=name, prefix=prefix, suffix=suffix)
        self.orientation = None  # Changed to None so it doesn't get serialized.
        # Module User Preferences
        self.influences_lookup_method = "path"  # path, uuid
        self.influences_dir = r"$PROJECT_DIR\influences"
        self.weights_lookup_method = "path"  # path TODO, add other auto detection methods?
        self.weights_dir = r"$PROJECT_DIR\weights"
        # Module Data
        self._file_format = ".json"

        self.set_extra_callable_function(
            self._read_influences_and_weights, order=tools_rig_frm.CodeData.Order.post_build
        )

    def _read_influences_and_weights(self):
        """
        Reads all influences and skin weights files found under the stored paths.
        """
        self._read_influences()
        self._read_weights()

    def _read_influences(self):
        """
        Reads all influences found under the influences directory and attempts to apply them.
        """
        # Initial Check
        _parsed_path = self._parse_path(path=self.influences_dir)
        if not os.path.exists(_parsed_path):
            logger.warning(f'Unable to import influences. Path: "{str(_parsed_path)}".')
            return
        for filename in os.listdir(_parsed_path):
            if filename.endswith(self._file_format):  # TODO add UUID lookup method
                _influence_file = os.path.join(_parsed_path, filename)
                _influence_data = core_io.read_json_dict(_influence_file)
                # Unpack data
                joints = _influence_data.get("influences")
                mesh = _influence_data.get("mesh")
                max_influences = _influence_data.get("max_influences")
                maintain_max_influences = _influence_data.get("maintain_max_influences")
                # Basic checks
                if not cmds.objExists(mesh):
                    logger.warning(f"Unable to bind missing mesh: {mesh}")
                    continue
                if core_skin.is_mesh_bound(mesh):
                    logger.warning(f"Mesh is already bound. Influence import was skipped: {mesh}")
                    continue
                # Bind elements
                skin_cluster = core_skin.bind_skin(joints=joints, objects=mesh, maximum_influences=max_influences)
                if skin_cluster:
                    cmds.setAttr(f"{skin_cluster[0]}.maintainMaxInfluences", maintain_max_influences)

    def _read_weights(self):
        """
        Reads all weights found under the influences directory and attempts to apply them.
        """
        # Initial Check
        _parsed_path = self._parse_path(path=self.weights_dir)
        if not os.path.exists(_parsed_path):
            logger.warning(f'Unable to import skin weights from missing directory. Path: "{str(_parsed_path)}".')
            return
        for filename in os.listdir(_parsed_path):
            if filename.endswith(self._file_format):  # TODO add UUID lookup method
                _weights_file = os.path.join(_parsed_path, filename)
                _weights_data = core_io.read_json_dict(_weights_file)
                # Unpack data
                mesh = _weights_data.get("mesh")
                weights = _weights_data.get("weights")
                # Basic checks
                if not cmds.objExists(mesh):
                    logger.warning(f"Unable to apply skin weights on missing mesh: {mesh}")
                    continue
                if not core_skin.is_mesh_bound(mesh):
                    logger.warning(f"Mesh is not bound. Weights import was skipped: {mesh}")
                    continue
                # Import skin weights
                core_skin.set_skin_weights(skinned_mesh=mesh, skin_data=weights)

    def write_influences(self, skinned_meshes, clear_target_dir=True):
        """
        Write influences for the provided elements.
        Args:
            skinned_meshes (list): A list of skinned meshes
            clear_target_dir (bool, optional): If True, all files with the influence extension found in the target
                                               directory get purged/deleted before writing new ones.
        """
        # Get write directory
        _parsed_path = self._parse_path(path=self.influences_dir)
        _parsed_path = core_io.make_directory(_parsed_path)
        if not os.path.exists(_parsed_path):
            logger.warning(f'Unable to write influences. Invalid path: "{str(_parsed_path)}".')
            return
        # Clear existing
        if clear_target_dir:
            for filename in os.listdir(_parsed_path):
                if filename.endswith(self._file_format):
                    core_io.delete_paths(os.path.join(_parsed_path, filename))
        # Write Influences
        for skinned_mesh in skinned_meshes:
            if not core_skin.is_mesh_bound(skinned_mesh):
                logger.warning(f"Unable to write influences for unbound mesh: {skinned_mesh}")
                continue
            _skin_cluster = core_skin.get_skin_cluster(skinned_mesh)
            _bound_joints = core_skin.get_bound_joints(skinned_mesh)  # TODO enforce full path
            _influences_dict = {
                "mesh": skinned_mesh,
                "lookup_method": self.influences_lookup_method,  # TODO create UUID method
                "max_influences": cmds.getAttr(f"{_skin_cluster}.maxInfluences"),
                "maintain_max_influences": cmds.getAttr(f"{_skin_cluster}.maintainMaxInfluences"),
                "influences": _bound_joints,
            }
            _mesh_short_name = core_naming.get_short_name(skinned_mesh)  # TODO make sure name is unique
            _file_path = os.path.join(_parsed_path, f"{_mesh_short_name}{self._file_format}")
            core_io.write_json(path=_file_path, data=_influences_dict)

    def write_influences_from_selection(self):
        """
        Same as "write_influences" but automatically populates the skinned meshes parameter with selection.
        """
        selection = cmds.ls(selection=True, long=True) or []
        # TODO, filter skinned meshes - log bad selection
        self.write_influences(skinned_meshes=selection)

    def write_weights(self, skinned_meshes, clear_target_dir=True):
        """
        Write weights for the provided elements.
        Args:
            skinned_meshes (list): A list of skinned meshes
            clear_target_dir (bool, optional): If True, all files with the influence extension found in the target
                                               directory get purged/deleted before writing new ones.
        """
        # Get write directory
        _parsed_path = self._parse_path(path=self.weights_dir)
        _parsed_path = core_io.make_directory(_parsed_path)
        if not os.path.exists(_parsed_path):
            logger.warning(f'Unable to write weights. Invalid path: "{str(_parsed_path)}".')
            return
        # Clear existing
        if clear_target_dir:
            for filename in os.listdir(_parsed_path):
                if filename.endswith(self._file_format):
                    core_io.delete_paths(os.path.join(_parsed_path, filename))
        # Write Weights
        # core_skin.export_weights_to_target_folder(obj_list=skinned_meshes, target_folder=_parsed_path)
        for skinned_mesh in skinned_meshes:
            if not core_skin.is_mesh_bound(skinned_mesh):
                logger.warning(f"Unable to write skin weights for unbound mesh: {skinned_mesh}")
                continue
            _skin_cluster = core_skin.get_skin_cluster(skinned_mesh)
            _weights = core_skin.get_skin_weights(skinned_mesh)  # TODO enforce full path
            _weights_dict = {
                "mesh": skinned_mesh,
                "weights": _weights,
            }
            _mesh_short_name = core_naming.get_short_name(skinned_mesh)  # TODO make sure name is unique
            _file_path = os.path.join(_parsed_path, f"{_mesh_short_name}{self._file_format}")
            core_io.write_json(path=_file_path, data=_weights_dict)

    def write_weights_from_selection(self):
        """
        Same as "write_weights" but automatically populates the skinned meshes parameter with selection.
        """
        selection = cmds.ls(selection=True, long=True) or []
        # TODO, filter skinned meshes - log bad selection
        self.write_weights(skinned_meshes=selection)

    # ------------------------------------------- Extra Module Setters ------------------------------------------
    def set_influences_dir(self, influences_dir):
        """
        Sets the directory path used to import influence files.
        Args:
            influences_dir (str): A file path to be used when writing or reading a list of influences.
        """
        if influences_dir is None:
            self.influences_dir = ""
        if not isinstance(influences_dir, str):
            logger.warning("Unable to influences path. Invalid data type was provided.")
            return
        self.influences_dir = influences_dir

    def set_weights_dir(self, weights_dir):
        """
        Sets the directory path used to import weight files.
        Args:
            weights_dir (str): A file path to be used when writing or reading a list of weights.
        """
        if weights_dir is None:
            self.weights_dir = ""
        if not isinstance(weights_dir, str):
            logger.warning("Unable to weight path. Invalid data type was provided.")
            return
        self.weights_dir = weights_dir


class ModuleSaveScene(tools_rig_frm.ModuleGeneric):
    __version__ = "0.0.1-alpha"
    icon = ui_res_lib.Icon.rigger_module_save_scene
    allow_parenting = False
    allow_multiple = True

    def __init__(self, name="Save Scene", prefix=None, suffix=None):
        super().__init__(name=name, prefix=prefix, suffix=suffix)
        self.orientation = None  # Changed to None so it doesn't get serialized.
        self.file_path = r"$PROJECT_DIR/Rig/character_rig.ma"
        self.file_extension = ".ma"  # MayaAscii
        self.set_extra_callable_function(self._force_save_scene, order=tools_rig_frm.CodeData.Order.post_build)

    def _force_save_scene(self):
        """
        Use maya commands to save the scene as mayaAscii.
        """
        if not self.file_path:
            logger.warning("File path empty. Please set first a file path.")
            return

        _parsed_path = self._parse_path(path=self.file_path)
        if not os.path.isdir(os.path.dirname(_parsed_path)):
            logger.warning("Unable to find the scene directory. Please set a valid directory.")
            return
        if not _parsed_path.lower().endswith(self.file_extension):
            logger.warning(f"File path has a wrong extension. Please set a {self.file_extension} file path.")
            return

        cmds.file(rename=_parsed_path)
        cmds.file(save=True, force=True, type="mayaAscii")

        logger.info(f"Maya scene has been saved: {_parsed_path}")
        return True

    def set_file_path(self, file_path=None, make_dir=True):
        """
        Sets the file path (complete path with filename) used to save the Maya scene.
        Eventual extension will be replaced by the defined extension value (see set_file_extension).

        Args:
            file_path (str): the complete path of the Maya scene.
            make_dir (bool): if True and the directory is missing, it will create it.
        """
        if not file_path:
            logger.warning("Unable to set the scene path. Provided empty value.")
            return
        if not isinstance(file_path, str):
            logger.warning("Unable to set the scene path. Invalid data type was provided.")
            return

        _parsed_path = self._parse_path(path=file_path)

        # Check folder
        if not os.path.exists(os.path.dirname(_parsed_path)) and make_dir:
            os.makedirs(os.path.dirname(_parsed_path))

        # Force mayaAscii extension
        if not _parsed_path.lower().endswith(self.file_extension):
            if _parsed_path.find(".") > -1:
                extension = _parsed_path.split(".")[-1]
                file_path = _parsed_path.replace(f".{extension}", self.file_extension)
            else:
                file_path = f"{_parsed_path}{self.file_extension}"

        file_path = file_path.replace("\\", "/")
        self.file_path = file_path

    def set_file_extension(self, extension=None):
        """
        Sets the file extension used to save the Maya scene.

        Args:
            extension (str): accepted only: "ma", "mb", by default the value used is "ma".
                             If None, the file extension will remain the default one.
        """
        if not extension:
            logger.warning("Unable to set the scene extension. Provided empty value.")
            return
        if not isinstance(extension, str):
            logger.warning("Unable to set the scene extension. Invalid data type was provided.")
            return
        if extension not in ["ma", "mb"]:
            logger.warning("Unable to set the scene extension. You can use only 'ma' or 'mb'.")
            return
        else:
            self.file_extension = f".{extension}"


if __name__ == "__main__":  # pragma: no cover
    logger.setLevel(logging.DEBUG)
    from gt.tools.auto_rigger.rig_framework import RigProject, ModuleGeneric

    # Create Test Modules ---------------------------------------------------------------------------------
    a_generic_module = ModuleGeneric()
    a_new_scene_module = ModuleNewScene()
    an_import_file_module = ModuleImportFile()
    a_skin_weights_module = ModuleSkinWeights()
    a_python_module = ModulePython()
    a_save_scene_module = ModuleSaveScene()

    # Test File Paths -------------------------------------------------------------------------------------
    import gt.tests.test_auto_rigger as test_auto_rigger
    import inspect
    import os

    module_path = inspect.getfile(test_auto_rigger)
    module_dir = os.path.dirname(module_path)
    a_cube_obj = os.path.join(module_dir, "data", "cylinder_project", "cylinder.obj")
    a_cube_fbx = os.path.join(module_dir, "data", "cylinder_project", "cylinder.fbx")

    # Configure Modules -----------------------------------------------------------------------------------
    p1 = a_generic_module.add_new_proxy()
    p2 = a_generic_module.add_new_proxy()
    p3 = a_generic_module.add_new_proxy()
    p1.set_name("first")
    p2.set_name("second")
    p3.set_name("third")
    p2.set_initial_position(y=15)
    p3.set_initial_position(y=30)
    p2.set_parent_uuid(p1.get_uuid())
    p3.set_parent_uuid(p2.get_uuid())
    p1.set_locator_scale(6)
    p2.set_locator_scale(5)
    p3.set_locator_scale(4)
    # New Scene
    scene_options = {
        "frame_rate": "30fps",
        "multi_sample": True,
        "multi_sample_count": 8,
        "persp_clip_plane_near": 0.1,
        "persp_clip_plane_far": 10000.0,
        "display_textures": True,
        "view_fit_all": True,
    }
    a_new_scene_module.set_scene_options(scene_options)
    # Import File
    an_import_file_module.set_file_path(file_path=a_cube_obj)
    an_import_file_module.set_file_path(file_path=a_cube_fbx)
    an_import_file_module.set_file_path(file_path=r"$TESTS_DATA_DIR\cylinder_project\geo\cylinder.obj")
    an_import_file_module.set_transforms_parent(transforms_parent="geometry")
    # Skin Weights
    a_skin_weights_module.set_influences_dir(r"$TESTS_DATA_DIR\cylinder_project\influences")
    a_skin_weights_module.set_weights_dir(r"$TESTS_DATA_DIR\cylinder_project\weights")
    # Python Module
    a_python_module.set_execution_code('print("hello world!")')
    # Save Scene
    a_save_scene_module.set_file_path(file_path=r"$TESTS_DATA_DIR\Rig\cylinder_rig.ma")

    # Create Project and Build ----------------------------------------------------------------------------
    a_project = RigProject()
    a_project.add_to_modules(a_new_scene_module)
    a_project.add_to_modules(a_generic_module)
    a_project.add_to_modules(an_import_file_module)
    a_project.add_to_modules(a_skin_weights_module)
    a_project.add_to_modules(a_python_module)
    a_project.add_to_modules(a_save_scene_module)
    a_project.set_project_dir_path(r"$DESKTOP_DIR\test_folder")
    # print(a_project.get_project_dir_path(parse_vars=True))  # Absolute path to Desktop\test_folder
    # a_project.add_to_modules(a_generic_module)  # Should be the only thing in the scene after building

    # # Creates new scene after building resulting in empty scene
    a_project.build_proxy()
    a_project.build_rig()

    # # Module Utilities
    # a_skin_weights_module.set_parent_project(a_project)
    # a_skin_weights_module.write_influences_from_selection()
    # a_skin_weights_module._read_influences()
    # a_skin_weights_module.write_weights_from_selection()
    # a_skin_weights_module._read_weights()

    # -----------------------------------------------------------------------------------------------------
    # # Test CodeData Saving Order Capabilities (It should be able to transfer the "post_build" change done above)
    # a_project_as_dict = a_project.get_project_as_dict()
    # a_project_2 = RigProject()
    # a_project_2.read_data_from_dict(a_project_as_dict)
    # a_project_2.build_proxy()
    # a_project_2.build_rig()

    # -----------------------------------------------------------------------------------------------------
    # # Test CodeData String Execution
    # # THIS IS JUST AN EXAMPLE. WE WOULDN'T"T OVERWRITE THE CODE DATA LIKE THAT AS WE CAN USE
    # # "set_extra_callable_function()" to achieve the same thing through python.
    # # THE STRING EXECUTION IS FOR USER INPUT AS CODE IN FUTURE MODULES
    # a_modified_new_scene_module = ModuleNewScene()  # This doesn't create a new scene, but print hello world instead
    # code_data = tools_rig_frm.CodeData()
    # code_data.set_order(tools_rig_frm.CodeData.Order.pre_proxy)
    # code_data.set_execution_code(code="print('hello world')")
    # a_modified_new_scene_module.set_code_data(code_data)
    #
    # a_project_3 = RigProject()
    # a_project_3.add_to_modules(a_modified_new_scene_module)
    # a_project_3.build_proxy()
    # a_project_3.build_rig()

    # Frame all
    cmds.viewFit(all=True)
