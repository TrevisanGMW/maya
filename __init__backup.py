# GT Tools Module - Init File
import maya.cmds as cmds
import importlib
import logging
import sys
import os

# Global Vars
PACKAGE_VERSION = "3.0.0"

# Initial Setup - Add path and initialize logger
if __name__ != '__main__':
    MODULE_PATH = os.path.dirname(__file__)  # GT Tools Module Path
    sys.path.append(MODULE_PATH)  # Append Module Path

logging.basicConfig()
logger = logging.getLogger("gt_tools")
logger.setLevel(logging.INFO)


def execute_script(import_name, entry_point_function, reload=True):
    """
    Attempts to import and execute the provided script using it entry point function
    Args:
        import_name: Name of the script or module to import. For example "gt_utilities"
        entry_point_function: Name of the entry point function, usually the one that opens the script's GUI (string)
        reload: Whether to reload the module before executing it (optional, bool)

    Returns:
        succeeded: True if there were no errors (bool)
    """
    if sys.version_info.major >= 3:  # Python 3+
        # Reload Module
        try:
            module = importlib.import_module(import_name)
            if reload:
                importlib.reload(module)
        except Exception as e:
            logger.warning('"' + import_name + '" was not found.')
            logger.warning('Error: ' + str(e))
            raise e
    else:  # Python 2 and below
        try:
            module = importlib.import_module(import_name)
            if reload:
                import imp
                imp.reload(module)
        except Exception as e:
            logger.info(str(e))
            logger.warning('"' + import_name + '" was not found.')
            logger.warning('Error: ' + str(e))
            raise e

    # Call Entry Function
    entry_line = 'module.' + entry_point_function + '()'
    try:
        eval(entry_line)
        return True
    except Exception as e:
        logger.warning('"' + entry_line + '" failed to run.')
        logger.warning('Error: ' + str(e))
        cmds.warning("Failed to execute entry point. Make sure the correct functions is being called.")
        return False


def reload_package():
    """
    Unload modules starting with the name "gt_tools" - So they are reloaded when called
    """
    from gt_tools import gt_utilities
    gt_utilities.unload_packages(silent=False, packages=["gt_tools"])


if __name__ == '__main__':
    # logger.setLevel(logging.DEBUG)
    print('Logger Level: ', logger.level)
    reload_package()

    # Paths to Append
    _this_folder = os.path.dirname(__file__)
    _tools_folder = os.path.dirname(_this_folder)
    _pipe_folder = os.path.dirname(_tools_folder)

    for to_append in [_this_folder, _tools_folder, _pipe_folder]:
        if to_append not in sys.path:
            sys.path.append(to_append)