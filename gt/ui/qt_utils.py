from PySide2.QtWidgets import QApplication, QWidget, QDesktopWidget, QDialog, QMainWindow
from gt.utils.session_utils import is_script_in_interactive_maya
from PySide2.QtGui import QFontDatabase, QColor, QFont
from gt.utils.system_utils import get_system, OS_MAC
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtCore import QPoint
import logging
import os
import re

# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class MayaWindowMeta(type):
    """
    Maya Window Metaclass. Used to make a QT Windows in Maya with extra functionalities such as docking and overwrites.
    It also handles the Singleton and Mac focus behaviour of the window (when in Maya)

    This metaclass modifies the base class of a QT object class to enable the dock ability in Maya.
    It dynamically adjusts the class inheritance to include "MayaQWidgetDockableMixin" based on the context
    (interactive Maya session or not).
    """
    def __new__(mcs, name, bases, attrs, base_inheritance=None, dockable=True):
        """
        Create a new class with modified inheritance for the dock ability in Maya.

        This method is responsible for creating a new class with modified base inheritance, which enables the dock
        ability in Maya. It checks whether the script is running in an interactive Maya session or not, and adjusts
        the base class accordingly. If running interactively, the "MayaQWidgetDockableMixin" is included in the
        inheritance; otherwise, only the specified base classes are used.

        Args:
            mcs (type): The metaclass instance (MayaDockableMeta).
            name (str): The name of the new class to be created.
            bases (tuple): The base classes of the new class.
            attrs (dict): The attributes and methods of the new class.
            base_inheritance (type, tuple, optional): The base class or classes to be included in inheritance.
                                                      Default is None, which becomes "QDialog".
                                                      If something is provided then that will be used instead.
            dockable (bool, optional): If active, then it will make the window dockable in Maya.
                                       If inactive, it will only attempt to delete existing windows before opening one.
                                       (In this case "MayaQWidgetDockableMixin" is not added as a base class)
        Returns:
            type: The newly created class with adjusted inheritance for Maya dock function.
        """
        if not base_inheritance:
            base_inheritance = (QDialog, )
            if get_system() == OS_MAC:
                base_inheritance = (QDialog, )
        if not isinstance(base_inheritance, tuple):
            base_inheritance = (base_inheritance,)
        if is_script_in_interactive_maya() and dockable:
            from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
            bases = (MayaQWidgetDockableMixin,) + base_inheritance
        else:
            bases = base_inheritance
        new_class = type(name, bases, attrs)

        # Overwrites
        base_class_vars = vars(new_class)
        if "__init__" in base_class_vars:
            original_init = base_class_vars["__init__"]

            def custom_init(self, *args, **kwargs):
                """
                Init injection (custom version of the init)
                It attempts to first close existing QT view of the same class type before opening a new one.
                It also overwrites the "show" function when using the dockable version of this metaclass.
                """
                try:
                    found_elements = get_maya_main_window_qt_elements(type(self))
                    close_ui_elements(found_elements)
                except Exception as e:
                    logger.debug(f'Unable to close previous QT elements. Issue {str(e)}')
                # Overwrite Show
                _class_dir = dir(self)
                if "show" in _class_dir and dockable:
                    original_show = self.show

                    def custom_show(*args_show, **kwargs_show):
                        """
                        This is a custom function to override the original "show".
                        It calls the original "show" method with the addition of the "dockable" argument set to True.
                        Args:
                            *args_show: Additional positional arguments for the "show" method.
                            **kwargs_show: Additional keyword arguments for the "show" method.
                        """
                        original_show(*args_show, **kwargs_show, dockable=True)
                        QWidget.setWindowIcon(self.parent().parent().parent().parent().parent(), self.iconData)
                    self.show = custom_show
                # Call Original Init
                original_init(self, *args, **kwargs)
            new_class.__init__ = custom_init
        return new_class


def get_maya_main_window_qt_elements(class_object):
    """
    Get PySide2.QtWidgets.QWidget elements of a specific class from the main Maya window.

    Args:
        class_object (type or str): The class type or fully qualified string name of the class.

    Returns:
        list: A list of PySide2.QtWidgets.QWidget elements matching the given class in the Maya window.
    """
    if isinstance(class_object, str):
        from gt.utils.system_utils import import_from_path
        class_object = import_from_path(class_object)
    if not class_object:
        logger.debug(f'The requested class was not found or is "None".')
        return []
    maya_win = get_maya_main_window()
    if not maya_win:
        logger.debug(f'Maya window was not found.')
        return []
    return maya_win.findChildren(class_object)


def close_ui_elements(obj_list):
    """
    Close and delete a list of UI elements.

    Args:
        obj_list (list): A list of UI elements to be closed and deleted.
    """
    for obj in obj_list:
        try:
            obj.close()
            obj.deleteLater()
        except Exception as e:
            logger.debug(f'Unable to close and delete window object. Issue: {str(e)}')
            pass


def get_cursor_position(offset_x=0, offset_y=0):
    """
    The current position of the mouse cursor

    Args:
        offset_x: (int) A value to offset the returned x position by - in pixels
        offset_y: (int) A value to offset the returned y position by - in pixels

    Returns:
        QPoint: the current cursor position, offset by the given x and y offset values>

    """
    cursor_position = QtGui.QCursor().pos()
    return QtCore.QPoint(cursor_position.x() + offset_x, cursor_position.y() + offset_y)


def get_screen_center():
    """
    Gets the center of the screen where the parent is located.

    Returns:
        QPoint: A QPoint object with X and Y coordinates for the center of the screen.
    """
    screen_number = get_main_window_screen_number()
    screen = QApplication.screens()[screen_number]
    center_x = screen.geometry().center().x()
    center_y = screen.geometry().center().y()
    center = QPoint(center_x, center_y)
    return center


def load_custom_font(font_path, point_size=-1, weight=-1, italic=False):
    """
    Loads a custom font using its path.
    NOTE: This function can only be used after loading an instance of QApplication.
    If an instance is not found, the default font is returned instead.
    Args:
        font_path (str): Path to a font file. (Accepted formats: ".ttf", "otf")
        point_size (int, optional): Font size (default -1)
        weight (int, optional): Font weight (default -1)
        italic (bool, optional): Font italic state (default False)
    Returns:
        QFont: A QFont object for the provided custom font or a default one if the operation failed
    """
    custom_font = QtGui.QFont()  # default font
    if QApplication.instance():
        # Open the font file using QFile
        file = QtCore.QFile(font_path)
        if file.open(QtCore.QIODevice.ReadOnly):
            data = file.readAll()
            file.close()

            # Load the font from the memory data
            font_id = QtGui.QFontDatabase.addApplicationFontFromData(data)
            if font_id != -1:
                font_families = QtGui.QFontDatabase.applicationFontFamilies(font_id)
                if len(font_families) > 0:
                    custom_font = QtGui.QFont(font_families[0],
                                              pointSize=point_size,
                                              weight=weight,
                                              italic=italic)
        else:
            logger.debug(f"Failed to open the font file: {font_path}")
    return custom_font


def is_font_available(font_name):
    """
    Checks the font QT font database to see if the font is available in the system.
    Args:
        font_name (str): The name of the font to check. For example: "Arial"
    Returns:
        bool: True if the font is available, false if it's not.
    """
    if QApplication.instance():
        font_db = QFontDatabase()
        available_fonts = font_db.families()
        return font_name in available_fonts


def get_font(font):
    """
    Function used to get QFont object from a font path or a font name.
    This will only work if an instance of a QApplication is present.
    Args:
        font (str): This is the font to load. It can be a font name or a font path.
                    If a name is provided, and it's found in the system, then a QFont object containing it is returned.
                    If a path is provided, it attempts to add it to the font database and create a QFont object for it.
    Returns:
        QFont: A QFont object with the provided font or a default QFont object in case the operation failed.
    """
    qt_font = QtGui.QFont()
    if not isinstance(font, str):
        return qt_font
    if is_font_available(font):
        qt_font = QtGui.QFont(font)
    elif os.path.exists(font) and os.path.isfile(font):
        qt_font = load_custom_font(font)
    return qt_font


def get_maya_main_window():
    """
    Finds the instance of maya's main window
    Returns:
        QWidget: The main maya widget
    """
    from shiboken2 import wrapInstance
    from maya import OpenMayaUI as OpenMayaUI
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    maya_window = wrapInstance(int(ptr), QWidget)
    return maya_window


def get_qt_color(color):
    if isinstance(color, str):
        if re.match(r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", color):  # Hex pattern (e.g. "#FF0000"):
            return QColor(color)
        else:
            try:
                return QColor(color)
            except Exception as e:
                logger.error(f'Unable to create QColor. Issue: {e}')
    elif isinstance(color, QColor):
        return color
    elif color is not None:
        logger.error(f'Unable to create QColor. Unrecognized object type received: "{type(color)}"')


def resize_to_screen(window, percentage=20, width_percentage=None, height_percentage=None):
    """
    Resizes the window to match a percentage of the screen size.

    Args:
        window (QDialog, any): Window to be resized.
        percentage (int, optional): The percentage of the screen size that the window should inherit.
                                    Must be a value between 0 and 100. Default is 20.
        width_percentage (int, optional): If provided, it will overwrite general set percentage when setting width
        height_percentage (int, optional): If provided, it will overwrite general set percentage when setting height

    Raises:
        ValueError: If the percentage is not within the range [0, 100].
    """
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage should be between 0 and 100")

    screen_geometry = QDesktopWidget().availableGeometry(window)
    width = screen_geometry.width() * percentage / 100
    height = screen_geometry.height() * percentage / 100
    if height_percentage:
        height = screen_geometry.height() * height_percentage / 100
    if width_percentage:
        width = screen_geometry.height() * width_percentage / 100
    print(f'width:{width}')
    print(f'height:{height}')
    window.setGeometry(0, 0, width, height)


def get_main_window_screen_number():
    """
    Determine the screen number where the main Qt instance is located.

    Returns:
        int: Index of the screen where the main window is located.
    """
    app = QApplication.instance()
    if app is None:
        return -1  # No instance found
    main_window = app.activeWindow() or QMainWindow()
    screen_number = QApplication.desktop().screenNumber(main_window)
    return screen_number


def center_window(window):
    """
    Moves the given window to the center of the screen.

    Args:
        window (QDialog, any): The window to be centered on the screen.
    """
    rect = window.frameGeometry()
    center_position = get_screen_center()
    rect.moveCenter(center_position)
    window.move(rect.topLeft())


def update_formatted_label(target_label,
                           text,
                           text_size=None,
                           text_color=None,
                           text_bg_color=None,
                           text_is_bold=False,
                           output_text="",
                           output_size=None,
                           output_color=None,
                           output_bg_color=None,
                           text_output_is_bold=False,
                           overall_alignment="center"):
    """
    Updates the target QLabel with formatted text containing a text and text output.
    e.g. "Text: TextOutput" or "Status: OK"

    Args:
       target_label (QtWidgets.QLabel): The QLabel to update with the formatted text.
       text (str): The text to be displayed before the output_text.
       text_size (int, optional): The font size of the text.
       text_color (str, optional): The color of the text.
       text_bg_color (str, optional): A color fo the text background.
       text_is_bold (bool, optional): Determines if the text should be bold or not. Default: False.
       output_text (str, optional): The text output to be displayed after the text.
       output_size (int, optional): The font size of the text output.
       output_color (str, optional): The color of the text output.
       output_bg_color (str, optional): The color of the text output background.
       text_output_is_bold (bool, optional): Determines if the text output should be bold or not. Default: False.
       overall_alignment (str, optional): The overall alignment of the formatted text. Default is "center".
                                          Possible values are "left", "center", and "right".
    """
    _html = f"<html><div style='text-align:{overall_alignment};'>"
    if text_is_bold:
        _html += "<b>"
    _html += f"<font"
    # Text
    if text_size:
        _html += f" size='{str(text_size)}'"
    if text_color:
        _html += f" color='{text_color}'"
    if text_bg_color:
        _html += f" style='background-color:{text_bg_color};'"
    _html += f">{text}</font>"
    if text_is_bold:
        _html += "</b>"
    # Output Text
    if output_text:
        if text_output_is_bold:
            _html += "<b>"
        _html += "<font"
        if output_size:
            _html += f" size='{str(output_size)}'"
        if output_color:
            _html += f" color='{output_color}'"
        if output_bg_color:
            _html += f" style='background-color:{output_bg_color};'"
        _html += f">{output_text}</font>"
        if text_output_is_bold:
            _html += "</b>"
    _html += "</div></html>"
    target_label.setText(_html)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    out = None
    print(out)
