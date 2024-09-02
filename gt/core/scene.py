"""
Scene Module

Code Namespace:
    core_scene  # import gt.core.scene as core_scene
"""

import maya.cmds as cmds
import subprocess
import logging
import sys
import os

# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

MAX_FRAME_RATE = 48000


def get_frame_rate():
    """
    Get the scene frame rate as a number
    Result:
        float: describing the scene frame rate. If operation fails "0.0" is returned instead
    """
    frame_rate = cmds.currentUnit(query=True, time=True) or ""
    if frame_rate == "film":
        return 24.0
    if frame_rate == "show":
        return 48.0
    if frame_rate == "pal":
        return 25.0
    if frame_rate == "ntsc":
        return 30.0
    if frame_rate == "palf":
        return 50.0
    if frame_rate == "ntscf":
        return 60.0
    if "fps" in frame_rate:
        return float(frame_rate.replace("fps", ""))
    logger.debug('Unable to detect scene frame rate. Returned "0.0".')
    return 0.0


def set_frame_rate(frame_rate):
    """
    Sets the frame rate of the current Maya scene.

    This function allows you to set the frame rate of the current Maya scene
    by providing either a numerical frame rate (e.g., 24, 30, 60) or a valid
    time unit string (e.g., "film", "ntsc", "palf"). The function maps common
    frame rates to Maya's internal time unit names and sets the scene's frame
    rate accordingly.

    Args:
        frame_rate (int | float | str): The desired frame rate for the scene.
            This can be either a number representing the frame rate (e.g., 24, 30, 60)
            or a string representing Maya's internal time unit name
            (e.g., "film", "ntsc", "palf").

    Notes:
        - If an unsupported numerical frame rate is provided, the function logs a
          debug message indicating that the input is invalid.
        - If an unsupported or invalid string is provided, the function logs a
          debug message indicating that the input is invalid.

    Examples:
        To set the scene's frame rate to 24 fps:
        set_frame_rate(24)

        To set the scene's frame rate using a time unit string:
        set_frame_rate("film")
    """
    # Dictionary mapping common frame-rates to Maya's internal time unit names
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

    if isinstance(frame_rate, str):
        # Set the scene's frame rate directly if a valid string is provided
        if frame_rate in frame_rate_mapping.values():
            cmds.currentUnit(time=frame_rate)
            logger.debug(f"Scene frame rate set to {frame_rate}.")
            return
        elif frame_rate.endswith("fps"):
            try:
                cmds.currentUnit(time=frame_rate)
                return
            except Exception as e:
                logger.debug(f"Unrecognized frame rate value. Issue: {e}")
    elif isinstance(frame_rate, (int, float)):
        # Check if the provided numerical frame-rate is supported
        if frame_rate in frame_rate_mapping:
            # Set the scene's frame rate using the mapped value
            cmds.currentUnit(time=frame_rate_mapping[frame_rate])
            logger.debug(f"Scene frame rate set to {frame_rate} fps.")
            return
        elif frame_rate <= MAX_FRAME_RATE:
            try:
                cmds.currentUnit(time=f"{int(frame_rate)}fps")
                return
            except Exception as e:
                logger.debug(f"Unrecognized frame rate value. Issue: {e}")
    logger.debug("Invalid input. Please provide a number or a valid time unit string.")


def get_distance_in_meters():
    """
    Get the number units necessary to make a meter
    Returns:
        float describing the amount of units necessary to make a meter
    """
    unit = cmds.currentUnit(query=True, linear=True) or ""
    if unit == "mm":
        return 1000
    elif unit == "cm":
        return 100
    elif unit == "km":
        return 0.001
    elif unit == "in":
        return 39.3701
    elif unit == "ft":
        return 3.28084
    elif unit == "yd":
        return 1.09361
    elif unit == "mi":
        return 0.000621371
    return 1


def force_reload_file():
    """Reopens the opened file (to revert any changes done to the file)"""
    if cmds.file(query=True, exists=True):  # Check to see if it was ever saved
        file_path = cmds.file(query=True, expandName=True)
        if file_path is not None:
            cmds.file(file_path, open=True, force=True)
    else:
        cmds.warning("Unable to force reload. File was never saved.")


def open_file_dir():
    """Opens the directory where the Maya file is saved"""
    fail_message = "Unable to open directory. Path printed to script editor instead."

    def open_dir(path):
        """
        Open path
        Args:
            path (str): Path to open using
        """
        if sys.platform == "win32":  # Windows
            # explorer needs forward slashes
            filebrowser_path = os.path.join(os.getenv("WINDIR"), "explorer.exe")
            path = os.path.normpath(path)

            if os.path.isdir(path):
                subprocess.run([filebrowser_path, path])
            elif os.path.isfile(path):
                subprocess.run([filebrowser_path, "/select,", path])
        elif sys.platform == "darwin":  # Mac-OS
            try:
                subprocess.call(["open", "-R", path])
            except Exception as exception:
                logger.debug(str(exception))
                print(path)
                cmds.warning(fail_message)
        else:  # Linux/Other
            print(path)
            cmds.warning(fail_message)

    if cmds.file(query=True, exists=True):  # Check to see if it was ever saved
        file_path = cmds.file(query=True, expandName=True)
        if file_path is not None:
            try:
                open_dir(file_path)
            except Exception as e:
                logger.debug(str(e))
                print(file_path)
                cmds.warning(fail_message)
    else:
        cmds.warning("Unable to open directory. File was never saved.")


if __name__ == "__main__":
    from pprint import pprint

    set_frame_rate("2fps")
    out = None
    # out = get_distance_in_meters()
    pprint(out)
