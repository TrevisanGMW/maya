"""
System Utilities - Utilities related to system activities, such as paths, open explorer, etc...
This script should not import "maya.cmds" as it's also intended to be used outside of Maya.
github.com/TrevisanGMW/gt-tools
"""
import base64
import subprocess
import tempfile
import logging
import pathlib
import sys
import os
import re

OS_MAC = 'darwin'
OS_LINUX = 'linux'
OS_WINDOWS = 'win32'
known_systems = [OS_WINDOWS, OS_MAC, OS_LINUX]

# Logging Setup
logging.basicConfig()
logger = logging.getLogger("system_utils")
logger.setLevel(logging.INFO)


def get_system():
    """
    Get system in which this script is running
    Returns:
        System name.
        e.g. "win32" for Windows, or "darwin" for MacOS
    """
    system = sys.platform
    if system not in known_systems:
        logger.debug(f'Unexpected system returned: {system}]')
    return system


def get_temp_folder():
    """
    Get path to the tempo folder. It will be different depending on the system
    e.g. "C:\\Users\\<User-Name>>\\AppData\\Local\\Temp"
    Returns:
        String path to temp folder
    """
    return tempfile.gettempdir()


def get_home_dir():
    """
    Returns home path

    Returns:
        Home path
        Windows example: "C:/Users/<UserName>"
        MacOS example: TBD
    """
    # Maya uses the HOME environment variable on Windows causing it to add "Documents" to the path
    if get_system() == OS_WINDOWS:
        return os.path.expanduser(os.getenv('USERPROFILE'))
    else:
        return pathlib.Path.home()


def get_desktop_path():
    """
    Get path to the Desktop folder of the current user
    Returns:
        String (path) to the desktop folder
    """
    return os.path.join(get_home_dir(), 'Desktop')


def get_maya_install_dir(system):
    """
    Get Maya installation folder (Autodesk folder where you find all Maya versions)
    Return:
        Path to autodesk folder (where you find maya#### folders
        e.g. "C:/Program Files/Autodesk/"
    """
    autodesk_default_paths = {
        OS_LINUX: "/usr/bin/",
        OS_MAC: f"/Applications/Autodesk/",
        OS_WINDOWS: f"C:\\Program Files\\Autodesk\\",
    }
    if system not in autodesk_default_paths.keys():
        raise KeyError(f'Unable to find the given system in listed paths. System: "{system}"')

    return autodesk_default_paths.get(system)


def get_maya_path(system, version, get_maya_python=False):
    """
    Get a path to Maya executable or maya headless
    Args
        system (string): System name
        version (string): Software version - #### e.g. "2023" or "2024"
        get_maya_python (optional, bool): If active, it will return maya python executable instead of maya interactive
    Returns:
        Path to Maya interactive or headless
    """
    install_dir = get_maya_install_dir(system)
    executable_name = "maya"
    if get_maya_python:
        executable_name = "mayapy"
    maya_paths = {
        OS_LINUX: "/usr/bin/",
        OS_MAC: f"{install_dir}/maya{version}/Maya.app/Contents/bin/{executable_name}",
        OS_WINDOWS: f"{install_dir}\\Maya{version}\\bin\\{executable_name}.exe",
    }
    if system not in maya_paths.keys():
        raise KeyError(f'Unable to find the given system in listed paths. System: "{system}"')

    return maya_paths.get(system)


def open_file_dir(path):
    """
    Opens the directory where the provided path points to
    Args:
        path (string): A path to a file or directory
    """
    system = get_system()
    if system == OS_WINDOWS:  # Windows
        # explorer needs forward slashes
        filebrowser_path = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
        path = os.path.normpath(path)

        if os.path.isdir(path):
            subprocess.run([filebrowser_path, path])
        elif os.path.isfile(path):
            subprocess.run([filebrowser_path, '/select,', path])
    elif system == OS_MAC:  # Mac-OS
        try:
            subprocess.call(["open", "-R", path])
        except Exception as exception:
            logger.warning(f'Unable to open directory. Issue: {exception}')
    else:  # Linux/Other
        logger.warning(f'Unable to open directory. Unsupported system: "{system}".')


def get_maya_settings_dir(system):
    """
    Get maya settings folder (folder contains scripts, prefs, etc..)
    Args:
        system (string): System string
    Returns:
        Path to settings folder (folder where you find scripts, prefs, etc..)
    """
    win_maya_settings_dir = ""
    mac_maya_settings_dir = ""
    if system == OS_WINDOWS:
        win_maya_settings_dir = os.path.expanduser('~')
        win_maya_settings_dir = os.path.join(win_maya_settings_dir, "Documents")
        win_maya_settings_dir = os.path.join(win_maya_settings_dir, "maya")
    elif system == OS_MAC:
        mac_maya_settings_dir = os.path.expanduser('~')
        mac_maya_settings_dir = os.path.join(mac_maya_settings_dir, "Library")
        mac_maya_settings_dir = os.path.join(mac_maya_settings_dir, "Preferences")
        mac_maya_settings_dir = os.path.join(mac_maya_settings_dir, "Autodesk")
        mac_maya_settings_dir = os.path.join(mac_maya_settings_dir, "maya")

    maya_settings_paths = {
        OS_LINUX: "/usr/bin/",
        OS_MAC: mac_maya_settings_dir,
        OS_WINDOWS: win_maya_settings_dir,
    }
    if system not in maya_settings_paths.keys():
        raise KeyError(f'Unable to find the given system in listed paths. System: "{system}"')

    return maya_settings_paths.get(system)


def get_available_maya_setting_dirs():
    """
    Gets all folders matching the pattern "####" inside the maya settings directory.
    Returns:
        Dictionary with maya versions as keys and path as value
        e.g. { "2024": "C:\\Users\\UserName\\Documents\\maya\\2024"}
    """
    maya_settings_dir = get_maya_settings_dir(get_system())
    if os.path.exists(maya_settings_dir):
        maya_folders = os.listdir(maya_settings_dir)
        existing_folders = {}
        for folder in maya_folders:
            if re.match("[0-9][0-9][0-9][0-9]", folder):
                existing_folders[folder] = os.path.join(maya_settings_dir, folder)
        return existing_folders
    else:
        logger.warning(f'Missing provided path: "{maya_settings_dir}"')


def get_available_maya_install_dirs():
    """
    Gets all folders matching the pattern "Maya####" inside the autodesk directory.
    Returns:
        Dictionary with maya versions as keys and path as value
        e.g. { "2024": "C:\\Users\\UserName\\Documents\\maya\\2024"}
        If nothing is found, it returns an empty dictionary
    """
    maya_settings_dir = get_maya_install_dir(get_system())
    if os.path.exists(maya_settings_dir):
        maya_folders = os.listdir(maya_settings_dir)
        existing_folders = {}
        for folder in maya_folders:
            if re.match("maya[0-9][0-9][0-9][0-9]", folder.lower()):
                folder_digits = re.sub("[^0-9]", "", folder)
                existing_folders[folder_digits] = os.path.join(maya_settings_dir, folder)
        return existing_folders
    else:
        logger.warning(f'Missing provided path: "{maya_settings_dir}"')
        return {}


def get_maya_executable(get_maya_python=False, preferred_version=None):
    """
    Gets a path to the executable of the latest available version of Maya detected on the system.
    If a preferred version si provided and is available, that is used instead
    Args:
        get_maya_python (optional, bool): If active, it will attempt to retrieve "mayapy" instead of "maya"
        preferred_version (optional, string): The preferred version. A string with four digits e.g. "2024"
                                              If found, that will be used, otherwise the latest detected version
                                              is returned instead.
    Returns:
        Path to Maya executable
        e.g. "C:\\Program Files\\Autodesk\\Maya2024\\bin\\maya.exe"
    """
    maya_installs = get_available_maya_install_dirs()
    if len(maya_installs) == 0:
        logger.warning("Unable to find latest Maya path. No Maya installation detected on this system.")
        return
    maya_install_dir = get_maya_path(get_system(), max(maya_installs), get_maya_python=get_maya_python)
    if preferred_version is not None and preferred_version in maya_installs:
        maya_install_dir = get_maya_path(get_system(), preferred_version, get_maya_python=get_maya_python)
    if not os.path.exists(maya_install_dir):
        logger.warning(f"Unable to find latest Maya path. Missing: {maya_install_dir}")
        return
    return maya_install_dir


def launch_maya_from_path(maya_path, python_script=None, additional_args=None):
    """
    Launches Maya using provided path
    Args:
        maya_path (string): Path to the maya executable e.g. "maya.exe" (Complete path)
        python_script (string): A python script in string format. If provided, it runs after opening Maya
        additional_args (optional, list): Additional arguments. e.g. ["-pythonver", "3"]
    Example:
        launch_maya(maya_path="C:\\Program Files\\Autodesk\\Maya2024\\bin\\maya.exe"
                    python_script='import sys; print("The arg number is: " + sys.argv[-1])',
                    preferred_version='2024',
                    additional_args=[7])  # Maya 2024 opens and prints "The arg number is: 7"
    """
    if not os.path.exists(maya_path):
        logger.warning(f"Unable to launch Maya. Provided path does not exist: {maya_path}")
        return
    args = [maya_path]
    if python_script is not None:
        encoded_python = base64.b64encode(python_script.encode('utf-8'))
        script_text = '''python("import base64; exec (base64.urlsafe_b64decode({}))")'''
        args += ['-c', script_text.format(encoded_python)]
    # Additional Arguments
    if additional_args is not None:
        if isinstance(additional_args, list):
            for arg in additional_args:
                args.append(str(arg))
        else:
            logger.warning(f"Unable to use additional arguments. Please use a list.")
    subprocess.check_call(args)


def launch_maya(preferred_version=None, python_script=None, additional_args=None):
    """
    Launches Maya latest automatically detected Maya executable
    Args:
        python_script (string): A python script in string format. If provided, it runs after opening Maya
        preferred_version (optional, string): The preferred version. A string with four digits e.g. "2024"
                                              If found, that will be used, otherwise the latest detected version
                                              is returned instead.
        additional_args (optional, list): A list of additional arguments (elements are converted to string)
                                          e.g. ["-pythonver", "3"]
    Example:
        launch_maya(python_script='import sys; print("The arg number is: " + sys.argv[-1])',
                    preferred_version='2024',
                    additional_args=[7])  # Maya 2024 opens and prints "The arg number is: 7"
    """
    maya_path = get_maya_executable(preferred_version=preferred_version)
    if maya_path:
        launch_maya_from_path(maya_path=maya_path,
                              python_script=python_script,
                              additional_args=additional_args)


def run_script_using_maya_python(script_path, preferred_version=None):
    """
    Runs provided script using the latest detected Maya Python ("mayapy")
    Args:
        script_path (string): Path to python script
        preferred_version (optional, string): The preferred version. A string with four digits e.g. "2024"
                                              If found, that will be used, otherwise the latest detected version
                                              is returned instead.
    """
    headless_maya = get_maya_executable(get_maya_python=True, preferred_version=preferred_version)
    if os.path.exists(headless_maya):
        output = subprocess.call([str(headless_maya), script_path])
        return output
    else:
        logger.warning(f"Unable to find maya python. Missing file: ")


if __name__ == "__main__":
    from pprint import pprint
    out = None
    pprint(out)