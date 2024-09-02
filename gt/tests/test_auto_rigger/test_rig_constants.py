import unittest
import logging
import sys
import os

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
import gt.tools.auto_rigger.rig_constants as tools_rig_const
from gt.tests import maya_test_tools

cmds = maya_test_tools.cmds


class TestRigConstants(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        maya_test_tools.import_maya_standalone(initialize=True)  # Start Maya Headless (mayapy.exe)

    def test_proxy_constants(self):
        attributes = vars(tools_rig_const.RiggerConstants)
        keys = [attr for attr in attributes if not (attr.startswith("__") and attr.endswith("__"))]
        for key in keys:
            constant = getattr(tools_rig_const.RiggerConstants, key)
            if not constant:
                raise Exception(f"Missing proxy constant data: {key}")
            if not isinstance(constant, (str, float, int, list)):
                raise Exception(f"Incorrect proxy constant type: {key}")
