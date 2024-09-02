"""
Version Module

Code Namespace:
    core_version # import gt.core.version as core_version
"""

from gt.core.feedback import print_when_true
from collections import namedtuple
import importlib.util
import logging
import os
import re

# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

VERSION_BIGGER = 1
VERSION_SMALLER = -1
VERSION_EQUAL = 0
SemanticVersion = namedtuple("SemanticVersion", ["major", "minor", "patch"])


def is_semantic_version(version_str, metadata_ok=True):
    """
    Checks if a given string adheres to the semantic versioning pattern.

    Args:
        version_str (str): The version string to be checked.
        metadata_ok (bool, optional): Optionally, it may include build metadata as a suffix,
                                      preceded by a hyphen (e.g., "1.12.3-alpha").

    Returns:
        bool: True if the version string matches the semantic versioning pattern, False otherwise.

    Examples:
        is_semantic_version("1.12.3")  # True
        is_semantic_version("1.2")  # False
        is_semantic_version("1.3.4-alpha", metadata_ok=False)  # False
        is_semantic_version("1.3.4-alpha", metadata_ok=True)  # True
    """

    if metadata_ok:
        pattern = (
            r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-((?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-]"
            r"[0-9a-zA-Z-]*)(?:\.(?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+"
            r"(?:\.[0-9a-zA-Z-]+)*))?$"
        )
    else:
        pattern = r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$"
    return bool(re.match(pattern, str(version_str)))


def parse_semantic_version(version_string, as_tuple=False):
    """
    Parses semantic version string input into a tuple with major, minor and patch integers.
    Args:
        version_string (str): String describing a version (must be semantic version) e.g. "1.2.3" or "2.14.5"
                                 Only two separating "." are allowed, otherwise it throws a ValueError.
                                 Any extra characters that are not digits will be ignored e.g. "v1.2.3dev" = "1.2.3"
        as_tuple (bool, optional): If active, it will return a namedtuple with the version e.g. (1, 2, 3)
                                   if inactive, it will return a string. e.g. "1.2.3"
    Returns:
        str or namedtuple: String: When "as_tuple" is inactive, a string with the version is returned. e.g. "1.2.3"
                           SemanticVersion: A named tuple with major, minor and patch information for the version.
                           e.g. (1, 2, 3)
                           e.g. (major=1, minor=2, patch=3)
    """
    try:
        version_string = re.sub("[^\d.]", "", version_string)  # Remove non-digits (keeps ".")
        major, minor, patch = map(int, version_string.split(".")[:3])
        if as_tuple:
            return SemanticVersion(major=major, minor=minor, patch=patch)
        else:
            return f"{str(major)}.{str(minor)}.{str(patch)}"
    except ValueError:
        raise ValueError(f'Invalid version format: "{version_string}". Use semantic versioning: e.g. "1.2.3".')


def compare_versions(version_a, version_b):
    """
    Compare two semantic versions and return the comparison result: newer, older or equal?
    Args:
        version_a (str): String describing a version (must be semantic version) e.g. "1.2.3" or "2.14.5"
        version_b (str): A string describing a version to be compared with version_a
    Returns:
        int: Comparison result
             -1: if older ("a" older than "b")
             0: if equal,
             1: if newer ("a" newer than "b")
    """
    major_a, minor_a, patch_a = parse_semantic_version(version_a, as_tuple=True)
    major_b, minor_b, patch_b = parse_semantic_version(version_b, as_tuple=True)

    if major_a > major_b:
        return VERSION_BIGGER
    elif major_a < major_b:
        return VERSION_SMALLER
    elif minor_a > minor_b:
        return VERSION_BIGGER
    elif minor_a < minor_b:
        return VERSION_SMALLER
    elif patch_a > patch_b:
        return VERSION_BIGGER
    elif patch_a < patch_b:
        return VERSION_SMALLER
    else:
        return VERSION_EQUAL


def get_package_version(package_path=None):
    """
    Gets the package version, independently of the package folder name.
    Args:
        package_path (str, optional): If provided, the path will be used to determine the package path.
                                      It assumes that the package is using the same variable name "PACKAGE_VERSION"
    Returns:
        str or None: Package version as a string. "major.minor.patch" e.g. "3.0.0", None if not found.
    """
    package_dir = package_path
    if package_path and not os.path.exists(str(package_path)):
        return
    if package_path is None:
        utils_dir = os.path.dirname(__file__)
        package_dir = os.path.dirname(utils_dir)
    init_path = os.path.join(package_dir, "__init__.py")
    if not os.path.exists(init_path):
        return
    try:
        # Load the module from the specified path
        module_spec = importlib.util.spec_from_file_location("module", init_path)
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        return module.__version__
    except Exception as e:
        logger.debug(f"Unable to retrieve current version. Issue: {str(e)}")
        return


def get_installed_version(verbose=True):
    """
    Get Installed Package Version
    Args:
        verbose (bool, optional): If active, it will print feedback messages
    Returns:
        str or None: A semantic version string or None if not installed. e.g. "1.2.3"
    """
    from gt.core.setup import get_installed_core_module_path

    package_core_module = get_installed_core_module_path(only_existing=False)
    if not os.path.exists(package_core_module):
        message = f'Package not installed. Missing path: "{package_core_module}"'
        print_when_true(message, do_print=verbose, use_system_write=True)
        return


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    from pprint import pprint

    # import maya.standalone
    # maya.standalone.initialize()
    out = None
    pprint(out)
