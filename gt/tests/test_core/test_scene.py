import os
import sys
import logging
import unittest

# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Import Utility and Maya Test Tools
test_utils_dir = os.path.dirname(__file__)
tests_dir = os.path.dirname(test_utils_dir)
package_root_dir = os.path.dirname(tests_dir)
for to_append in [package_root_dir, tests_dir]:
    if to_append not in sys.path:
        sys.path.append(to_append)
from gt.tests import maya_test_tools
from gt.core import scene as core_scene

cmds = maya_test_tools.cmds


def import_test_scene():
    """
    Open files from inside the test_*/data folder/cube_namespaces.mb
    Scene contains a cube named: "parentNS:childNS:grandchildNS:pCube1"
    """
    maya_test_tools.import_data_file("cube_namespaces.ma")


class TestSceneCore(unittest.TestCase):
    def setUp(self):
        maya_test_tools.force_new_scene()

    @classmethod
    def setUpClass(cls):
        maya_test_tools.import_maya_standalone(initialize=True)  # Start Maya Headless (mayapy.exe)

    def test_get_frame_rate(self):
        import_test_scene()
        expected = 24
        result = core_scene.get_frame_rate()
        self.assertEqual(expected, result)

        cmds.currentUnit(time="ntsc")
        expected = 30
        result = core_scene.get_frame_rate()
        self.assertEqual(expected, result)

    def test_set_frame_rate(self):
        frame_rate_mapping = {
            23.976: "23.976fps",
            24: "film",
            25: "pal",
            29.97: "29.97fps",
            30: "ntsc",
            47.952: "47.952fps",
            48: "show",
            50: "palf",
            59.94: "59.94fps",
            60: "ntscf",
        }

        for number_fr, string_fr in frame_rate_mapping.items():
            core_scene.set_frame_rate(number_fr)
            expected = string_fr
            result = cmds.currentUnit(query=True, time=True)
            self.assertEqual(expected, result)

        for number_fr, string_fr in frame_rate_mapping.items():
            core_scene.set_frame_rate(string_fr)
            expected = string_fr
            result = cmds.currentUnit(query=True, time=True)
            self.assertEqual(expected, result)

    def test_set_frame_rate_non_listed_frame_rate(self):
        core_scene.set_frame_rate(2)
        expected = "2fps"
        result = cmds.currentUnit(query=True, time=True)
        self.assertEqual(expected, result)
        core_scene.set_frame_rate(6)
        expected = "6fps"
        result = cmds.currentUnit(query=True, time=True)
        self.assertEqual(expected, result)
        core_scene.set_frame_rate(48000)
        expected = "48000fps"
        result = cmds.currentUnit(query=True, time=True)
        self.assertEqual(expected, result)

    def test_set_frame_rate_too_high(self):
        core_scene.set_frame_rate(24)
        core_scene.set_frame_rate(48001)  # Unavailable, it will retain initial valid value
        expected = "film"
        result = cmds.currentUnit(query=True, time=True)
        self.assertEqual(expected, result)

    def test_set_frame_rate_with_fps_string(self):
        core_scene.set_frame_rate("12fps")
        expected = "12fps"
        result = cmds.currentUnit(query=True, time=True)
        self.assertEqual(expected, result)
        core_scene.set_frame_rate("120fps")
        expected = "120fps"
        result = cmds.currentUnit(query=True, time=True)
        self.assertEqual(expected, result)

    def test_get_frame_rate_changed(self):
        import_test_scene()
        maya_test_tools.set_scene_framerate(time="ntscf")
        expected = 60
        result = core_scene.get_frame_rate()
        self.assertEqual(expected, result)

    def test_get_distance_in_meters(self):
        import_test_scene()
        expected = 100
        result = core_scene.get_distance_in_meters()
        self.assertEqual(expected, result)
