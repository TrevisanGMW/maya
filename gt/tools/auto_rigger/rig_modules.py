import inspect
import gt.core.str as core_str
import gt.ui.resource_library as ui_res_lib
import gt.tools.auto_rigger.rig_framework as tools_rig_fmr
import gt.tools.auto_rigger.module_root as tools_mod_root
import gt.tools.auto_rigger.module_spine as tools_mod_spine
import gt.tools.auto_rigger.module_biped_leg as tools_mod_leg
import gt.tools.auto_rigger.module_biped_arm as tools_mod_arm
import gt.tools.auto_rigger.module_biped_finger as tools_mod_finger
import gt.tools.auto_rigger.module_head as tools_mod_head
import gt.tools.auto_rigger.module_utils as tools_mod_utils
import gt.tools.auto_rigger.module_socket as tools_mod_socket
import gt.tools.auto_rigger.module_attr_hub as tools_mod_attr_switcher


class RigModules:
    # General
    ModuleGeneric = tools_rig_fmr.ModuleGeneric
    ModuleRoot = tools_mod_root.ModuleRoot
    ModuleSpine = tools_mod_spine.ModuleSpine
    ModuleHead = tools_mod_head.ModuleHead
    ModuleAttributeHub = tools_mod_attr_switcher.ModuleAttributeHub
    ModuleSocket = tools_mod_socket.ModuleSocket
    # Biped
    ModuleBipedArm = tools_mod_arm.ModuleBipedArm
    ModuleBipedArmLeft = tools_mod_arm.ModuleBipedArmLeft
    ModuleBipedArmRight = tools_mod_arm.ModuleBipedArmRight
    ModuleBipedFingers = tools_mod_finger.ModuleBipedFingers
    ModuleBipedFingersLeft = tools_mod_finger.ModuleBipedFingersLeft
    ModuleBipedFingersRight = tools_mod_finger.ModuleBipedFingersRight
    ModuleBipedLeg = tools_mod_leg.ModuleBipedLeg
    ModuleBipedLegLeft = tools_mod_leg.ModuleBipedLegLeft
    ModuleBipedLegRight = tools_mod_leg.ModuleBipedLegRight
    # Utils
    ModuleNewScene = tools_mod_utils.ModuleNewScene
    ModuleImportFile = tools_mod_utils.ModuleImportFile
    ModuleSkinWeights = tools_mod_utils.ModuleSkinWeights
    ModulePython = tools_mod_utils.ModulePython
    ModuleSaveScene = tools_mod_utils.ModuleSaveScene

    @staticmethod
    def get_dict_modules():
        """
        Gets all available modules as a dictionary. Key is the name of the module and value is the class.
        Returns:
            dict: Dictionary where the key is the name of the module and value is the class.
                  e.g. 'ModuleBipedArm': <class 'ModuleBipedArm'>
        """
        modules_attrs = vars(RigModules)
        class_attributes = {name: value for name, value in modules_attrs.items() if inspect.isclass(value)}
        return class_attributes

    @staticmethod
    def get_modules():
        """
        Gets the available module classes stored in the RigModules class.
        Returns:
            list: A list of modules, these use the ModuleGeneric as their base.
        """
        return list(RigModules.get_dict_modules().values())

    @staticmethod
    def get_module_names():
        """
        Gets the name of all available modules.
        Returns:
            list: A list of module names (strings)
        """
        return list(RigModules.get_dict_modules().keys())


class RigModulesCategories:
    known_categories = {
        "General": ui_res_lib.Icon.rigger_module_generic,
        "Biped": ui_res_lib.Icon.rigger_template_biped,
    }
    categories = {}
    unique_modules = {}

    # Create lists of modules with the same name that end with sides (a.k.a. Unique Modules)
    for name, module in RigModules.get_dict_modules().items():
        _name = core_str.remove_prefix(input_string=name, prefix="Module")
        _name = core_str.remove_suffix(input_string=_name, suffix="Left")
        _name = core_str.remove_suffix(input_string=_name, suffix="Right")
        if _name in unique_modules:
            unique_modules.get(_name).append(module)
        else:
            unique_modules[_name] = [module]

    # Create categories based on the name which the module starts with. Otherwise, it's general.
    for mod_name, mod_list in unique_modules.items():
        _category = "General"  # Default (Misc)
        for prefix in known_categories:
            if mod_name.startswith(prefix) and prefix != _category:
                _category = prefix
        if mod_name not in unique_modules:
            continue  # Skip Sides
        if _category in categories:
            categories.get(_category).append(mod_name)
        else:
            categories[_category] = [mod_name]


if __name__ == "__main__":
    import pprint

    # pprint.pprint(RigModules.get_dict_modules())
    pprint.pprint(RigModulesCategories.categories)
