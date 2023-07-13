"""
Setup Utilities - install/uninstall package from system
"""
from session_utils import is_script_in_py_maya, filter_loaded_modules_path_containing
from system_utils import get_available_maya_preferences_dirs
from feedback_utils import print_when_true
import maya.cmds as cmds
import logging
import shutil
import os

# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

PACKAGE_NAME = "gt-tools"
PACKAGE_REQUIREMENTS = ['tools', 'utils', 'ui', '__init__.py']
PACKAGE_ENTRY_LINE = 'python("import gt_tools_loader");'
PACKAGE_LEGACY_LINE = 'source "gt_tools_menu.mel";'
PACKAGE_USER_SETUP = "userSetup.mel"


def get_maya_preferences_dir():
    """
    Get maya preferences dir using cmds
    Usually Documents/maya
    Returns:
        Path to maya settings directory. Usually "C:/Users/<user-name>/Documents/maya"
    """
    return os.path.dirname(cmds.about(preferences=True))


def get_package_requirements():
    """
    Gets required folders elements from the package root
    Returns:
        Dictionary with required files as keys and paths as values
        e.g. { "tools": "C:\\tools"}
        If nothing is found, it returns an empty dictionary
    """
    source_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(source_dir)
    found_requirements = {}
    if os.path.exists(parent_dir):
        package_root = os.listdir(parent_dir)
        for item in package_root:
            if item in PACKAGE_REQUIREMENTS:
                found_requirements[item] = os.path.join(parent_dir, item)
    else:
        logger.warning(f'Missing package root: "{parent_dir}"')
        return {}
    if sorted(list(found_requirements)) != sorted(PACKAGE_REQUIREMENTS):
        logger.warning(f'Missing package requirement: Expected items: "{PACKAGE_REQUIREMENTS}"')
        return {}
    return found_requirements


def copy_package_requirements(target_folder, package_requirements):
    """
    Copies files and directories from provided package_requirements to target folder
    Args:
        target_folder (str): Target folder. That's where the files will be copied to.
        package_requirements (dict): Dictionary containing key:"element name" and value:"element path"
                                     Essentially: file_name: file_path
                                     e.g {"tools": "C:/tools"}
                                     This can be generated using the function "get_package_requirements()"
    """
    # Is target a directory
    if not os.path.isdir(target_folder):
        raise NotADirectoryError(f'Unable to copy package requirements. "{target_folder}" is not a directory')
    # Copy
    for requirement, requirement_path in package_requirements.items():
        if os.path.isdir(requirement_path):  # Directories
            shutil.copytree(src=requirement_path,
                            dst=os.path.join(target_folder, requirement),
                            # dirs_exist_ok=True,  # Not needed for now + Only available on Python 3.8+
                            ignore=shutil.ignore_patterns('*.pyc', '__pycache__'))
        elif os.path.isfile(requirement_path):  # Files
            shutil.copy(requirement_path, target_folder)


def remove_previous_install(target_path):
    """
    Remove target path in case it exists and matches the name of the package.
    Function used to perform a clean installation.
    If package is not found or doesn't match the name, the operation is ignored.
    Args:
        target_path (str): Path to a directory that is a previous installation of the package
    """
    if os.path.exists(target_path):
        if os.path.basename(target_path) == PACKAGE_NAME:
            logger.debug(f'Removing previous install: "{target_path}"')
            shutil.rmtree(target_path)


def check_installation_integrity(package_target_folder):
    """
    Checks if all requirements were copied to the installation folder

    Parameters:
        package_target_folder (str): Path to the installation folder

    Returns:
        bool: True if all requirements were found. False otherwise.
    """
    if not package_target_folder or not os.path.isdir(package_target_folder):
        return False
    file_list = os.listdir(package_target_folder)
    missing_list = []
    for requirement in PACKAGE_REQUIREMENTS:
        if requirement not in file_list:
            missing_list.append(requirement)
    missing_string = ', '.join(missing_list)
    if len(missing_list) > 0:
        print(f"Missing required files: {missing_string}")
        return False
    return True


def add_entry_line(file_path, create_missing_file=True):
    """
    Add entry line to provided path. The entry line is a line of code used to initialize package.

    Parameters:
        file_path (str): File path, usually an "userSetup" file
        create_missing_file (bool, optional): If provided file doesn't exist, a file is created.
    """
    # Determine if file is available and create missing ones
    if not file_path or not os.path.exists(file_path):
        if os.path.isdir(os.path.dirname(file_path)) and create_missing_file:
            open(file_path, 'a').close()  # Create empty file
            with open(file_path, 'w') as file:
                file.write(PACKAGE_ENTRY_LINE + "\n")
            return
        else:
            logger.warning(f'Unable to add entry line. Missing file: "{str(file_path)}".')
            return
    # Find if line exists before adding
    file_lines = []
    is_present = False
    with open(file_path, "r+") as file:
        file_lines = file.readlines()
        for line in file_lines:
            if line.startswith(PACKAGE_ENTRY_LINE):
                is_present = True

    if not is_present:
        with open(file_path, "w") as file:
            prefix = ""
            if len(file_lines) > 0:
                if not file_lines[-1].endswith("\n"):  # Is new line necessary?
                    prefix = "\n"
            file_lines.append(prefix + PACKAGE_ENTRY_LINE + "\n")
            file.writelines(file_lines)


def remove_entry_line(file_path, line_to_remove, delete_empty_file=True):
    """
    Remove entry line to provided path. The entry line is a line of code used to initialize package.
    If the file is empty after removing the line, it's also deleted to avoid keeping an empty file (default behaviour)

    Args:
        file_path (str): File path, usually an "userSetup" file
        line_to_remove (str): String to remove from the userSetup file
        delete_empty_file (bool, optional): If file is empty after removing the entry line, it gets deleted.
    Returns:
        int: How many lines were found and removed
    """
    # Determine if file is available and create missing ones
    if not file_path or not os.path.exists(file_path):
        logger.warning(f'Unable to remove entry line. Missing file: "{str(file_path)}".')
        return
    # Find if line exists and store non-matching lines
    new_lines = []
    is_present = False
    matching_line_counter = 0
    with open(file_path, "r+") as file:
        file_lines = file.readlines()
        for line in file_lines:
            if line.startswith(line_to_remove):
                matching_line_counter += 1
            else:
                new_lines.append(line)
    # Write file with lines that don't match entry line
    if matching_line_counter > 0:
        with open(file_path, "w") as file:
            file.writelines(new_lines)
    if delete_empty_file:
        content = ""
        with open(file_path, "r") as file:
            content = file.read()
        if content.strip() == "":
            try:
                os.remove(file_path)
            except Exception as e:
                logger.debug(f"Unable to delete empty file. Issue: {str(e)}")
    return matching_line_counter


def add_entry_point_to_maya_installs():
    """
    Add entry line to all available maya settings.
    For example, if Maya 2023 and 2024 are installed:
    Both of these files would get the string PACKAGE_ENTRY_LINE appended to them (if not yet present):
        "C:/Users/<user-name>/Documents/maya/2023/scripts/userSetup.py"
        "C:/Users/<user-name>/Documents/maya/2024/scripts/userSetup.py"
    """
    user_setup_list = generate_user_setup_list(only_existing=False)  # False so it generates missing files
    for user_setup_path in user_setup_list:
        add_entry_line(file_path=user_setup_path)


def remove_entry_point_from_maya_installs():
    """
    Remove entry line from all available maya settings.
    For example, if Maya 2023 and 2024 are installed:
    Both of these files would be searched for the string PACKAGE_ENTRY_LINE and cleaned if present:
        "C:/Users/<user-name>/Documents/maya/2023/scripts/userSetup.py"
        "C:/Users/<user-name>/Documents/maya/2024/scripts/userSetup.py"
    If the file is empty after removing the line, it's also deleted to avoid keeping an empty file
    """
    user_setup_list = generate_user_setup_list(only_existing=True)
    for user_setup_path in user_setup_list:
        remove_entry_line(file_path=user_setup_path, line_to_remove=PACKAGE_ENTRY_LINE)


def remove_legacy_entry_point_from_maya_installs(verbose=True):
    """
    Remove entry line from all available maya settings.
    For example, if Maya 2023 and 2024 are installed:
    Both of these files would be searched for the string PACKAGE_ENTRY_LINE and cleaned if present:
        "C:/Users/<user-name>/Documents/maya/2023/scripts/userSetup.py"
        "C:/Users/<user-name>/Documents/maya/2024/scripts/userSetup.py"
    If the file is empty after removing the line, it's also deleted to avoid keeping an empty file

    Args:
        verbose (bool, optional): If active, a message
    Returns:
        int: Number of legacy lines detected and removed during operation.
    """
    removed_legacy_lines = 0
    user_setup_list = generate_user_setup_list(only_existing=True)
    for user_setup_path in user_setup_list:
        removed_legacy_lines = remove_entry_line(file_path=user_setup_path, line_to_remove=PACKAGE_LEGACY_LINE)
        if removed_legacy_lines > 0:
            print_when_true("Legacy version detected. Removing legacy entry line...", do_print=verbose)
    return removed_legacy_lines


def generate_scripts_dir_list(file_name, only_existing=False):
    """
    Creates a list of potential files according to available preferences folders.
    For example, if preferences for Maya 2023 and 2024 are found, the path for both of these will be generated.

    Args:
        file_name (string): Name of the file to generate the list
        only_existing (bool, optional): If true, only existing files will be returned (useful for when removing them)
                                        Default is false, so potential paths will be generated even if file is not
                                        available (does not exist).
    Returns:
        A list of paths pointing to the Maya preferences folder, including the provided file name.
        e.g. ["C://Users//<user-name>//Documents//maya/2024//scripts//userSetup.py"]
    """
    user_setup_list = []
    maya_settings_dir = get_available_maya_preferences_dirs(use_maya_commands=True)
    if not maya_settings_dir:
        logger.warning(f"Unable to add entry lines. Failed to retrieve Maya preferences folders.")
        return user_setup_list
    for version in maya_settings_dir:
        folder = maya_settings_dir.get(version)
        scripts_folder = os.path.join(folder, "scripts")
        if os.path.isdir(scripts_folder):
            user_setup_file = os.path.join(scripts_folder, file_name)
            if only_existing:
                if os.path.exists(user_setup_file):
                    user_setup_list.append(user_setup_file)
            else:
                user_setup_list.append(user_setup_file)
    return user_setup_list


def generate_user_setup_list(only_existing=False):
    """
    Creates a list of potential userSetup files according to available maya preferences folders.
    For example, if preferences for Maya 2023 and 2024 are found, the path for both of these versions will be generated.

    Args:
    only_existing (bool, optional): If true, only existing files will be returned (useful for when removing them)
                                    Default is false, so potential paths will be generated even if file is not
                                    available (does not exist).
    Returns:
        A list of paths pointing to the Maya preferences folder, including the provided file name.
        e.g. ["C://Users//<user-name>//Documents//maya/2024//scripts//userSetup.py"]
        """
    return generate_scripts_dir_list(file_name=PACKAGE_USER_SETUP, only_existing=only_existing)


def copy_package_loader_to_maya_installs():
    """
    Copy the package loader script to all available Maya preferences folders.
    e.g. Windows: "Documents/scripts/gt_tools_loader.py"
    """
    to_copy_list = generate_scripts_dir_list(file_name="gt_tools_loader.py", only_existing=False)
    utils_dir = os.path.dirname(__file__)
    package_loader_script = os.path.join(utils_dir, "data", "package_loader.py")  # utils/data/package_loader.py
    if os.path.isfile(package_loader_script):
        for path in to_copy_list:
            shutil.copy(package_loader_script, path)
    else:
        logger.warning(f"Unable to find loader script. Expected location: {package_loader_script}")


def remove_package_loader_from_maya_installs():
    """
    Remove the package loader script from all available Maya preferences folders.
    e.g. Windows: "Documents/scripts/gt_tools_loader.py"  - If it exists, it will get deleted
    """
    to_remove_list = generate_scripts_dir_list(file_name="gt_tools_loader.py", only_existing=True)

    for file in to_remove_list:
        if os.path.exists(file):
            logger.debug(f'Removing loader script: "{file}"')
            try:
                os.remove(file)
            except Exception as e:
                logger.warning(f"Unable to remove loader file. Issue: {str(e)}")


def reload_package_loaded_modules():
    """
    Reloads modules containing the package fragment path in it.
    For example, if a module contains "package-name//requirement" it gets reloaded.
    e.g. "gt-tools/tools" is the fragment, if the module is "gt-tools/tools/package_setup/script.py" then it reloads.
    """
    package_path_fragments = []
    for requirement in PACKAGE_REQUIREMENTS:
        if "." not in requirement:
            undesired_fragment = os.path.join(PACKAGE_NAME, requirement)
            package_path_fragments.append(undesired_fragment)
    filtered_modules = filter_loaded_modules_path_containing(package_path_fragments)
    import importlib
    try:
        for module in filtered_modules:
            importlib.reload(module)
    except Exception as e:
        logger.debug(e)


def install_package(clean_install=True, verbose=True, passthrough_functions=None):
    """
    Installs package in the Maya Settings directory
    Args:
        clean_install (optional, bool): Will first delete the package folder before copying files. (No overwrite)
                                        Only deletes if the folder matches the name of the package. Default: True
        verbose (bool, optional): If active, script will print steps as it's going through it - Default: True
        passthrough_functions (list, callable, optional): A list of callable functions that will be called with the
                                                          feedback of the installation as their first argument.
                                                          e.g. If I provide [my_func], then the script will call
                                                          my_func("Fetching requirements...") and so on as it goes
                                                          through the operation.
    Returns:
        bool: True if function reached the end successfully
    """
    # If running in MayaPy - Initialize session
    if is_script_in_py_maya():
        print_when_true("Initializing Maya Standalone...", do_print=verbose,
                        passthrough_functions=passthrough_functions)
        try:
            import maya.standalone
            maya.standalone.initialize()
        except Exception as e:
            print_when_true(f"Failed to initialize Maya standalone. Issue: {e}", do_print=verbose,
                            passthrough_functions=passthrough_functions)
            return

    # Find Install Target Directory - Maya Settings Dir
    print_when_true("Fetching requirements...", do_print=verbose, passthrough_functions=passthrough_functions)
    maya_preferences_dir = get_maya_preferences_dir()
    if not os.path.exists(maya_preferences_dir):
        message = f'Unable to install package. Missing required path: "{maya_preferences_dir}"'
        logger.warning(message)
        print_when_true(message, do_print=False, passthrough_functions=passthrough_functions)
        return

    # Find Source Install Directories
    package_requirements = get_package_requirements()
    if not package_requirements:
        message = f'Unable to install package. Missing required directories: "{PACKAGE_REQUIREMENTS}"'
        logger.warning(message)
        print_when_true(message, do_print=False, passthrough_functions=passthrough_functions)
        return

    # Clean install
    package_target_folder = os.path.normpath(os.path.join(maya_preferences_dir, PACKAGE_NAME))
    if clean_install:
        print_when_true("Removing previous install...", do_print=verbose,
                        passthrough_functions=passthrough_functions)
        remove_previous_install(package_target_folder)
    # Create Package Folder
    if not os.path.exists(package_target_folder):
        os.makedirs(package_target_folder)
    # Copy files and directories
    print_when_true("Copying required files...", do_print=verbose,
                    passthrough_functions=passthrough_functions)
    copy_package_requirements(package_target_folder, package_requirements)
    # Add Entry Point and loader script
    print_when_true("Adding entry point to userSetup...", do_print=verbose,
                    passthrough_functions=passthrough_functions)
    add_entry_point_to_maya_installs()
    copy_package_loader_to_maya_installs()
    # Detect legacy entry lines
    if remove_legacy_entry_point_from_maya_installs(verbose=False):
        print_when_true("Legacy version detected. Removing legacy entry line...", do_print=verbose,
                        passthrough_functions=passthrough_functions)

    # Check installation integrity
    print_when_true("Checking installation integrity...", do_print=verbose,
                    passthrough_functions=passthrough_functions)
    if check_installation_integrity(package_target_folder):
        print_when_true("\nInstallation completed successfully!", do_print=verbose,
                        passthrough_functions=passthrough_functions)
        return True
    else:
        message = f'Installation failed integrity check. Package might not work as expected.'
        logger.warning(message)
        print_when_true(message, do_print=False,
                        passthrough_functions=passthrough_functions)


def uninstall_package(verbose=True, passthrough_functions=None):
    """
    Uninstalls package from the Maya Settings directory
    Args:
        verbose (bool, optional): If active, script will print steps as it's going through it - Default: True
        passthrough_functions (list, callable, optional): A list of callable functions that will be called with the
                                                          feedback of the uninstallation as their first argument.
                                                          e.g. If I provide [my_func], then the script will call
                                                          my_func("Fetching install location...") and so on as it goes
                                                          through the operation.
    Returns:
        bool: True if function reached the end successfully
    """
    # If running in MayaPy - Initialize session
    if is_script_in_py_maya():
        print_when_true("Initializing Maya Standalone...", do_print=verbose,
                        passthrough_functions=passthrough_functions)
        try:
            import maya.standalone
            maya.standalone.initialize()
        except Exception as e:
            print_when_true(f"Failed to initialize Maya standalone. Issue: {e}", do_print=verbose,
                            passthrough_functions=passthrough_functions)
            return

    # Find Install Target Directory - Maya Settings Dir
    print_when_true("Fetching install location...", do_print=verbose,
                    passthrough_functions=passthrough_functions)
    maya_preferences_dir = get_maya_preferences_dir()
    if not os.path.exists(maya_preferences_dir):
        message = f'Unable to uninstall package. Unable to find install location: "{maya_preferences_dir}"'
        logger.warning(message)
        print_when_true(message, do_print=False, passthrough_functions=passthrough_functions)
        return

    # Find Source Install Directories
    print_when_true("Checking installed files...", do_print=verbose, passthrough_functions=passthrough_functions)
    package_target_folder = os.path.normpath(os.path.join(maya_preferences_dir, PACKAGE_NAME))
    if not os.path.exists(package_target_folder):
        message = f'Unable to uninstall package. No previous installation detected.'
        logger.warning(message)
        print_when_true(message, do_print=False, passthrough_functions=passthrough_functions)
        return

    # Remove installed package
    print_when_true("Removing package...", do_print=verbose,
                    passthrough_functions=passthrough_functions)
    remove_previous_install(package_target_folder)
    # Remove entry point and loader script
    print_when_true("Removing entry point lines...", do_print=verbose,
                    passthrough_functions=passthrough_functions)
    remove_entry_point_from_maya_installs()
    print_when_true("Removing loader scripts...", do_print=verbose,
                    passthrough_functions=passthrough_functions)
    remove_package_loader_from_maya_installs()
    print_when_true("\nUninstallation completed successfully!", do_print=verbose,
                    passthrough_functions=passthrough_functions)
    return True


if __name__ == "__main__":
    from pprint import pprint
    import maya.standalone as standalone
    standalone.initialize()
    # logger.setLevel(logging.DEBUG)
    out = None
    out = install_package()
    # out = uninstall_package()
    pprint(out)
