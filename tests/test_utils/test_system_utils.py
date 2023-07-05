import os
import sys
import pathlib
import logging
import unittest
import tempfile
from unittest.mock import patch

# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Import Tested Utility and Maya Test Tools
test_utils_dir = os.path.dirname(__file__)
tests_dir = os.path.dirname(test_utils_dir)
package_root_dir = os.path.dirname(tests_dir)
for to_append in [package_root_dir, tests_dir]:
    if to_append not in sys.path:
        sys.path.append(to_append)
from tests import maya_test_tools
from utils import system_utils


class TestSystemUtils(unittest.TestCase):
    def tearDown(self):
        maya_test_tools.delete_test_temp_dir()

    def test_get_system(self):
        result = system_utils.get_system()
        expected = sys.platform
        self.assertEqual(expected, result)

    @patch('sys.platform', 'mocked_platform')
    def test_get_system_two(self):
        result = system_utils.get_system()
        expected = "mocked_platform"
        self.assertEqual(expected, result)

    def test_get_temp_folder(self):
        result = system_utils.get_temp_folder()
        expected = tempfile.gettempdir()
        self.assertEqual(expected, result)

    @patch('utils.system_utils.get_system')
    def test_get_home_dir(self, mock_get_system):
        mock_get_system.return_value = "mocked_value"
        result = system_utils.get_home_dir()
        expected = pathlib.Path.home()  # Exactly what the function returns
        self.assertEqual(expected, result)

    @patch('utils.system_utils.get_home_dir')
    def test_get_desktop_path(self, mock_get_home_dir):
        mock_get_home_dir.return_value = "path"
        result = system_utils.get_desktop_path()
        expected = os.path.join("path", "Desktop")
        self.assertEqual(expected, result)

    def test_get_maya_install_dir_win32(self):
        result = system_utils.get_maya_install_dir(system_utils.OS_WINDOWS)
        expected = f"C:\\Program Files\\Autodesk\\"
        self.assertEqual(expected, result)

    def test_get_maya_install_dir_mac(self):
        result = system_utils.get_maya_install_dir(system_utils.OS_MAC)
        expected = f"/Applications/Autodesk/"
        self.assertEqual(expected, result)

    def test_get_maya_install_dir_key_error(self):
        with self.assertRaises(KeyError):
            system_utils.get_maya_install_dir("random_missing_key")

    def test_get_maya_path_win32(self):
        result = system_utils.get_maya_path(system=system_utils.OS_WINDOWS,
                                            version='2024',
                                            get_maya_python=False)
        expected = os.path.normpath(f'C:\\Program Files\\Autodesk\\Maya2024\\bin\\maya.exe')
        self.assertEqual(expected, result)

    def test_get_maya_path_mac(self):
        result = system_utils.get_maya_path(system=system_utils.OS_MAC,
                                            version='2023',
                                            get_maya_python=False)
        expected = os.path.normpath(f"/Applications/Autodesk//maya2023/Maya.app/Contents/bin/maya")
        self.assertEqual(expected, result)

    def test_get_maya_path_key_error(self):
        with self.assertRaises(KeyError):
            system_utils.get_maya_path(system="random_missing_key",
                                       version='2024',
                                       get_maya_python=False)

    @patch('subprocess.run')
    def test_open_file_dir_win32(self, mock_subprocess_run):
        with patch('utils.system_utils.get_system') as mock_get_system:
            temp_folder = tempfile.gettempdir()
            mock_get_system.return_value = system_utils.OS_WINDOWS
            system_utils.open_file_dir(temp_folder)
            mock_get_system.assert_called_once()  # Make sure get system is called
            mock_subprocess_run.assert_called_once()  # Make sure subprocess.run is called
            result = mock_subprocess_run.call_args.args[0]
            expected = ['C:\\WINDOWS\\explorer.exe', temp_folder]
            self.assertEqual(expected, result)

    @patch('subprocess.call')
    def test_open_file_dir_mac(self, mock_subprocess_call):
        with patch('utils.system_utils.get_system') as mock_get_system:
            temp_folder = tempfile.gettempdir()
            mock_get_system.return_value = system_utils.OS_MAC
            system_utils.open_file_dir(temp_folder)
            mock_get_system.assert_called_once()  # Make sure get system is called
            mock_subprocess_call.assert_called_once()  # Make sure subprocess.run is called
            result = mock_subprocess_call.call_args.args[0]
            expected = ["open", "-R", temp_folder]
            self.assertEqual(expected, result)

    def test_get_maya_settings_dir_win32(self):
        result = system_utils.get_maya_settings_dir(system=system_utils.OS_WINDOWS)
        generated_path = os.path.join(os.path.expanduser('~'), "Documents", "maya")
        expected = os.path.normpath(generated_path)
        self.assertEqual(expected, result)

    def test_get_maya_settings_dir_mac(self):
        result = system_utils.get_maya_settings_dir(system=system_utils.OS_MAC)
        generated_path = os.path.join(os.path.expanduser('~'), "Library", "Preferences", "Autodesk", "maya")
        expected = os.path.normpath(generated_path)
        self.assertEqual(expected, result)

    @patch('utils.system_utils.get_maya_settings_dir')
    def test_get_available_maya_preferences(self, mock_get_maya_settings_dir):
        test_temp_dir = maya_test_tools.generate_test_temp_dir()
        mock_get_maya_settings_dir.return_value = test_temp_dir
        result = {}
        try:
            for folder in ["2020", "2024", "folder", "scripts", "2023backup"]:
                test_obj = os.path.join(test_temp_dir, folder)
                if not os.path.exists(test_obj):
                    os.mkdir(test_obj)
            result = system_utils.get_available_maya_preferences_dirs(use_maya_commands=False)
        except Exception as e:
            logger.warning(f"Failed to test maya preferences: Issue:{e}")
        mock_get_maya_settings_dir.assert_called_once()

        expected = {"2020": os.path.join(test_temp_dir, "2020"),
                    "2024": os.path.join(test_temp_dir, "2024")}
        self.assertEqual(expected, result)

    @patch('utils.system_utils.get_maya_install_dir')
    def test_get_available_maya_install_dirs(self, mock_get_maya_install_dir):
        test_temp_dir = maya_test_tools.generate_test_temp_dir()
        mock_get_maya_install_dir.return_value = test_temp_dir
        result = {}
        try:
            for folder in ["Maya2020", "maya2024", "folder", "scripts", "2023backup", "maya2023backup"]:
                test_obj = os.path.join(test_temp_dir, folder)
                if not os.path.exists(test_obj):
                    os.mkdir(test_obj)
            result = system_utils.get_available_maya_install_dirs()
        except Exception as e:
            logger.warning(f"Failed to test maya preferences: Issue:{e}")
        mock_get_maya_install_dir.assert_called_once()

        expected = {"2020": os.path.join(test_temp_dir, "Maya2020"),
                    "2024": os.path.join(test_temp_dir, "maya2024")}
        self.assertEqual(expected, result)

    def test_get_maya_executable_win32(self):
        with patch('utils.system_utils.get_available_maya_install_dirs') as mock_install_dirs, \
             patch('utils.system_utils.get_system') as mock_get_system, \
             patch('os.path.exists') as mock_exists:
            mock_install_dirs.return_value = {"2022": "fake_path",
                                              "2024": "fake_path"}
            mock_get_system.return_value = system_utils.OS_WINDOWS
            mock_exists.return_value = True
            result = system_utils.get_maya_executable()
            mock_install_dirs.assert_called_once()
            mock_exists.assert_called_once()

            expected = os.path.normpath("C:\\Program Files\\Autodesk\\Maya2024\\bin\\maya.exe")
            self.assertEqual(expected, result)

    def test_get_maya_executable_win32_preferred_version(self):
        with patch('utils.system_utils.get_available_maya_install_dirs') as mock_install_dirs, \
             patch('utils.system_utils.get_system') as mock_get_system, \
             patch('os.path.exists') as mock_exists:
            mock_install_dirs.return_value = {"2020": "fake_path",
                                              "2024": "fake_path"}
            mock_get_system.return_value = system_utils.OS_WINDOWS
            mock_exists.return_value = True
            result = system_utils.get_maya_executable(preferred_version="2020")
            mock_install_dirs.assert_called_once()
            mock_exists.assert_called_once()

            expected = os.path.normpath("C:\\Program Files\\Autodesk\\Maya2020\\bin\\maya.exe")
            self.assertEqual(expected, result)

    def test_get_maya_executable_win32_maya_python(self):
        with patch('utils.system_utils.get_available_maya_install_dirs') as mock_install_dirs, \
             patch('utils.system_utils.get_system') as mock_get_system, \
             patch('os.path.exists') as mock_exists:
            mock_install_dirs.return_value = {"2020": "fake_path",
                                              "2024": "fake_path"}
            mock_get_system.return_value = system_utils.OS_WINDOWS
            mock_exists.return_value = True  # Skip check to see if it exists
            result = system_utils.get_maya_executable(get_maya_python=True)
            mock_install_dirs.assert_called_once()
            mock_exists.assert_called_once()

            expected = os.path.normpath("C:\\Program Files\\Autodesk\\Maya2024\\bin\\mayapy.exe")
            self.assertEqual(expected, result)

    def test_get_maya_executable_mac(self):
        with patch('utils.system_utils.get_available_maya_install_dirs') as mock_install_dirs, \
             patch('utils.system_utils.get_system') as mock_get_system, \
             patch('os.path.exists') as mock_exists:
            mock_install_dirs.return_value = {"2022": "fake_path",
                                              "2024": "fake_path"}
            mock_get_system.return_value = system_utils.OS_MAC
            mock_exists.return_value = True  # Skip check to see if it exists
            result = system_utils.get_maya_executable()
            mock_install_dirs.assert_called_once()
            mock_exists.assert_called_once()

            expected = os.path.normpath("\\Applications\\Autodesk\\maya2024\\Maya.app\\Contents\\bin\\maya")
            self.assertEqual(expected, result)

    def test_get_maya_executable_mac_preferred_version(self):
        with patch('utils.system_utils.get_available_maya_install_dirs') as mock_install_dirs, \
             patch('utils.system_utils.get_system') as mock_get_system, \
             patch('os.path.exists') as mock_exists:
            mock_install_dirs.return_value = {"2020": "fake_path",
                                              "2024": "fake_path"}
            mock_get_system.return_value = system_utils.OS_MAC
            mock_exists.return_value = True  # Skip check to see if it exists
            result = system_utils.get_maya_executable(preferred_version="2020")
            mock_install_dirs.assert_called_once()
            mock_exists.assert_called_once()

            expected = os.path.normpath("\\Applications\\Autodesk\\maya2020\\Maya.app\\Contents\\bin\\maya")
            self.assertEqual(expected, result)

    def test_get_maya_executable_mac_maya_python(self):
        with patch('utils.system_utils.get_available_maya_install_dirs') as mock_install_dirs, \
             patch('utils.system_utils.get_system') as mock_get_system, \
             patch('os.path.exists') as mock_exists:
            mock_install_dirs.return_value = {"2020": "fake_path",
                                              "2024": "fake_path"}
            mock_get_system.return_value = system_utils.OS_MAC  # Force Mac
            mock_exists.return_value = True  # Skip check to see if it exists
            result = system_utils.get_maya_executable(get_maya_python=True)
            mock_install_dirs.assert_called_once()
            mock_exists.assert_called_once()

            expected = os.path.normpath("\\Applications\\Autodesk\\maya2024\\Maya.app\\Contents\\bin\\mayapy")
            self.assertEqual(expected, result)

    def test_launch_maya_from_path(self):
        with patch('os.path.exists') as mock_exists, \
             patch('subprocess.check_call') as mock_check_call:
            mock_exists.return_value = True  # Skip check to see if it exists
            system_utils.launch_maya_from_path(maya_path="fake_path")
            mock_exists.assert_called_once()
            mock_check_call.assert_called_once()
            result = mock_check_call.call_args.args[0]
            expected = ['fake_path']
            self.assertEqual(expected, result)

    def test_launch_maya_from_path_python_script(self):
        with patch('os.path.exists') as mock_exists, \
             patch('subprocess.check_call') as mock_check_call:
            mock_exists.return_value = True  # Skip check to see if it exists
            system_utils.launch_maya_from_path(maya_path="fake_path", python_script="py")
            mock_exists.assert_called_once()
            mock_check_call.assert_called_once()
            result = mock_check_call.call_args.args[0]
            expected = ['fake_path', '-c', 'python("import base64; exec (base64.urlsafe_b64decode(b\'cHk=\'))")']
            self.assertEqual(expected, result)

    def test_launch_maya_from_path_additional_args(self):
        with patch('os.path.exists') as mock_exists, \
             patch('subprocess.check_call') as mock_check_call:
            mock_exists.return_value = True  # Skip check to see if it exists
            system_utils.launch_maya_from_path(maya_path="fake_path", additional_args=["a", "b"])
            mock_exists.assert_called_once()
            mock_check_call.assert_called_once()
            result = mock_check_call.call_args.args[0]
            expected = ["fake_path", "a", "b"]
            self.assertEqual(expected, result)

    def test_launch_maya(self):
        with patch('utils.system_utils.get_maya_executable') as mock_get_maya_executable, \
             patch('os.path.exists') as mock_exists, \
             patch('subprocess.check_call') as mock_check_call:
            mock_get_maya_executable.return_value = "fake_path"
            mock_exists.return_value = True  # Skip check to see if it exists
            system_utils.launch_maya()
            mock_exists.assert_called_once()
            mock_check_call.assert_called_once()
            result = mock_check_call.call_args.args[0]
            expected = ["fake_path"]
            self.assertEqual(expected, result)

    def test_launch_maya_preferred_version(self):
        with patch('utils.system_utils.get_maya_executable') as mock_get_maya_executable, \
             patch('os.path.exists') as mock_exists, \
             patch('subprocess.check_call') as mock_check_call:
            mock_get_maya_executable.return_value = "fake_path"
            mock_exists.return_value = True  # Skip check to see if it exists
            system_utils.launch_maya(preferred_version="2024")
            mock_exists.assert_called_once()
            mock_check_call.assert_called_once()
            result_one = mock_check_call.call_args.args[0]
            result_two = mock_get_maya_executable.call_args.kwargs
            expected = [["fake_path"], {'preferred_version': '2024'}]
            self.assertEqual(expected, [result_one, result_two])

    def test_run_script_using_maya_python(self):
        with patch('utils.system_utils.get_maya_executable') as mock_get_maya_executable, \
             patch('os.path.exists') as mock_exists, \
             patch('subprocess.call') as mock_call:
            mock_get_maya_executable.return_value = "fake_headless_path"
            mock_exists.return_value = True  # Skip check to see if it exists
            system_utils.run_script_using_maya_python("fake_script_path")
            mock_exists.assert_called_once()
            mock_call.assert_called_once()
            result = mock_call.call_args.args
            expected = (['fake_headless_path', 'fake_script_path'],)
            self.assertEqual(expected, result)

    def test_process_launch_options_value_error(self):
        with self.assertRaises(ValueError):
            system_utils.process_launch_options([])

    def test_process_launch_options_value_unrecognized(self):
        with patch('sys.stdout.write'):
            result = system_utils.process_launch_options(["fake_script_name", "-unrecognized_test"])
            expected = False
            self.assertEqual(expected, result)

    def test_process_launch_options_install(self):
        with patch('setup_utils.install_package') as mock_install_package:
            system_utils.process_launch_options(["fake_script_name", "-install"])
            mock_install_package.assert_called_once()
            result = mock_install_package.call_args.kwargs
            expected = {'clean_install': False}
            self.assertEqual(expected, result)

    def test_process_launch_options_install_clean(self):
        with patch('setup_utils.install_package') as mock_install_package:
            system_utils.process_launch_options(["fake_script_name", "-install", "-clean"])
            mock_install_package.assert_called_once()
            result = mock_install_package.call_args.kwargs
            expected = {'clean_install': True}
            self.assertEqual(expected, result)

    def test_process_launch_options_install_gui(self):
        with patch('tools.package_setup.launcher_entry_point') as mock_launcher_entry_point:
            system_utils.process_launch_options(["fake_script_name", "-install", "-gui"])
            mock_launcher_entry_point.assert_called_once()

    def test_process_launch_options_uninstall(self):
        with patch('setup_utils.uninstall_package') as mock_uninstall_package:
            result = system_utils.process_launch_options(["fake_script_name", "-uninstall"])
            mock_uninstall_package.assert_called_once()
            expected = True
            self.assertEqual(expected, result)

    def test_process_launch_options_launch(self):
        with patch('utils.system_utils.load_package_menu') as mock_launch:
            result = system_utils.process_launch_options(["fake_script_name", "-launch"])
            mock_launch.assert_called_once()
            expected = True
            self.assertEqual(expected, result)

    def test_process_launch_options_test(self):
        with patch('tests.run_all_tests_with_summary') as mock_tests:
            result = system_utils.process_launch_options(["fake_script_name", "-test", "-all"])
            mock_tests.assert_called_once()
            expected = True
            self.assertEqual(expected, result)

    def test_initialize_from_package_calling(self):
        with patch('importlib.import_module') as mock_import_module, \
             patch('utils.system_utils.eval') as mock_eval:
            result = system_utils.initialize_from_package("fake_import_path", "fake_entry_point_function")
            mock_import_module.assert_called_once()
            mock_eval.assert_called_once()
            expected = True
            self.assertEqual(expected, result)

    def test_initialize_from_package_arguments(self):
        with patch('importlib.import_module') as mock_import_module, \
             patch('utils.system_utils.eval') as mock_eval:
            system_utils.initialize_from_package("fake_import_path", "fake_entry_point_function")
            mock_import_module.assert_called_once()
            mock_eval.assert_called_once()
            expected = ('module.fake_entry_point_function()',)
            result = mock_eval.call_args.args
            self.assertEqual(expected, result)

