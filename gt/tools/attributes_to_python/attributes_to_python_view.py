"""
Attributes To PythonView View/Window
"""

from gt.ui.syntax_highlighter import PythonSyntaxHighlighter
from gt.ui.line_text_widget import LineTextWidget
import gt.ui.resource_library as ui_res_lib
import gt.ui.qt_utils as ui_qt_utils
import gt.ui.qt_import as ui_qt


class AttributesToPythonView(metaclass=ui_qt_utils.MayaWindowMeta):
    def __init__(self, parent=None, controller=None, version=None):
        """
        Initialize the AttributesToPythonView.
        This window represents the main GUI window of the tool.

        Args:
            parent (str): Parent for this window
            controller (AttributesToPythonViewController): AttributesToPythonViewController, not to be used, here so
                                                          it's not deleted by the garbage collector.  Defaults to None.
            version (str, optional): If provided, it will be used to determine the window title. e.g. Title - (v1.2.3)
        """
        super().__init__(parent=parent)

        self.controller = controller  # Only here so it doesn't get deleted by the garbage collectors

        # Window Title
        self.window_title = "Attributes to Python"
        _window_title = self.window_title
        if version:
            _window_title += f" - (v{str(version)})"
        self.setWindowTitle(_window_title)

        # Labels
        self.title_label = None
        self.output_python_label = None
        # Buttons
        self.help_btn = None
        self.extract_trs_set_attr_btn = None
        self.extract_trs_list_btn = None
        self.extract_user_attr_btn = None
        self.run_code_btn = None
        self.save_to_shelf_btn = None
        # Misc
        self.output_python_box = None

        self.create_widgets()
        self.create_layout()

        self.setWindowFlags(
            self.windowFlags()
            | ui_qt.QtLib.WindowFlag.WindowMaximizeButtonHint
            | ui_qt.QtLib.WindowFlag.WindowMinimizeButtonHint
        )
        self.setWindowIcon(ui_qt.QtGui.QIcon(ui_res_lib.Icon.tool_attributes_to_python))

        stylesheet = ui_res_lib.Stylesheet.scroll_bar_base
        stylesheet += ui_res_lib.Stylesheet.maya_dialog_base
        stylesheet += ui_res_lib.Stylesheet.list_widget_base
        self.setStyleSheet(stylesheet)
        self.extract_trs_set_attr_btn.setStyleSheet(ui_res_lib.Stylesheet.btn_push_bright)
        self.extract_trs_list_btn.setStyleSheet(ui_res_lib.Stylesheet.btn_push_bright)
        self.extract_user_attr_btn.setStyleSheet(ui_res_lib.Stylesheet.btn_push_bright)
        ui_qt_utils.resize_to_screen(self, percentage=40, width_percentage=55)
        ui_qt_utils.center_window(self)

    def create_widgets(self):
        """Create the widgets for the window."""
        self.title_label = ui_qt.QtWidgets.QLabel(self.window_title)
        self.title_label.setStyleSheet(
            "background-color: rgb(93, 93, 93); border: 0px solid rgb(93, 93, 93); \
                                        color: rgb(255, 255, 255); padding: 10px; margin-bottom: 0; text-align: left;"
        )
        self.title_label.setFont(ui_qt_utils.get_font(ui_res_lib.Font.roboto))
        self.help_btn = ui_qt.QtWidgets.QPushButton("Help")
        self.help_btn.setToolTip("Open Help Dialog.")
        self.help_btn.setStyleSheet(
            "color: rgb(255, 255, 255); padding: 10px; " "padding-right: 15px; padding-left: 15px; margin: 0;"
        )
        self.help_btn.setFont(ui_qt_utils.get_font(ui_res_lib.Font.roboto))

        self.output_python_label = ui_qt.QtWidgets.QLabel("Output Python Code:")
        self.output_python_label.setStyleSheet(
            f"font-weight: bold; font-size: 8; margin-top: 0; " f"color: {ui_res_lib.Color.RGB.gray_lighter};"
        )

        self.output_python_box = LineTextWidget(self)

        self.output_python_box.setMinimumHeight(150)
        PythonSyntaxHighlighter(self.output_python_box.get_text_edit().document())
        #
        self.output_python_label.setAlignment(ui_qt.QtLib.AlignmentFlag.AlignCenter)
        self.output_python_label.setFont(ui_qt_utils.get_font(ui_res_lib.Font.roboto))
        #
        self.output_python_box.setSizePolicy(ui_qt.QtLib.SizePolicy.Expanding, ui_qt.QtLib.SizePolicy.Expanding)

        self.extract_trs_set_attr_btn = ui_qt.QtWidgets.QPushButton('Extract Default Attributes to "setAttr"')
        self.extract_trs_set_attr_btn.setToolTip("Extracts translate, rotate and scale attributes to set attributes.")
        self.extract_user_attr_btn = ui_qt.QtWidgets.QPushButton("Extract User-Defined Attributes")
        self.extract_user_attr_btn.setToolTip("Extracts user-defined attributes.")
        self.extract_trs_list_btn = ui_qt.QtWidgets.QPushButton("Extract Default Attributes to List")
        self.extract_trs_list_btn.setToolTip("Extract translate, rotate and scale attributes to a lists.")
        self.run_code_btn = ui_qt.QtWidgets.QPushButton("Run Code")
        self.run_code_btn.setStyleSheet("padding: 10;")
        self.save_to_shelf_btn = ui_qt.QtWidgets.QPushButton("Save to Shelf")
        self.save_to_shelf_btn.setStyleSheet("padding: 10;")

    def create_layout(self):
        """Create the layout for the window."""

        top_buttons_layout = ui_qt.QtWidgets.QVBoxLayout()
        two_horizontal_btn_layout = ui_qt.QtWidgets.QHBoxLayout()
        two_horizontal_btn_layout.addWidget(self.extract_trs_set_attr_btn)
        two_horizontal_btn_layout.addWidget(self.extract_trs_list_btn)
        top_buttons_layout.addLayout(two_horizontal_btn_layout)
        top_buttons_layout.addWidget(self.extract_user_attr_btn)

        mid_layout = ui_qt.QtWidgets.QVBoxLayout()
        mid_layout.addWidget(self.output_python_label)
        mid_layout.addWidget(self.output_python_box)
        mid_layout.setContentsMargins(0, 5, 0, 5)  # L-T-R-B

        bottom_buttons_layout = ui_qt.QtWidgets.QVBoxLayout()
        two_horizontal_btn_layout = ui_qt.QtWidgets.QHBoxLayout()
        two_horizontal_btn_layout.addWidget(self.run_code_btn)
        two_horizontal_btn_layout.addWidget(self.save_to_shelf_btn)
        bottom_buttons_layout.addLayout(two_horizontal_btn_layout)

        separator = ui_qt.QtWidgets.QFrame()
        separator.setFrameShape(ui_qt.QtLib.FrameStyle.HLine)
        separator.setFrameShadow(ui_qt.QtLib.FrameStyle.Sunken)

        title_layout = ui_qt.QtWidgets.QHBoxLayout()
        title_layout.setSpacing(0)
        title_layout.addWidget(self.title_label, 5)
        title_layout.addWidget(self.help_btn)

        main_layout = ui_qt.QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        top_layout = ui_qt.QtWidgets.QVBoxLayout()
        bottom_layout = ui_qt.QtWidgets.QVBoxLayout()
        top_layout.addLayout(title_layout)
        top_layout.addLayout(top_buttons_layout)
        top_layout.setContentsMargins(15, 15, 15, 15)  # L-T-R-B
        main_layout.addLayout(top_layout)
        main_layout.addWidget(separator)
        bottom_layout.addLayout(mid_layout)
        bottom_layout.addLayout(bottom_buttons_layout)
        bottom_layout.setContentsMargins(15, 0, 15, 15)  # L-T-R-B
        main_layout.addLayout(bottom_layout)

    def clear_python_output(self):
        """Removes all text from the changelog box"""
        self.output_python_box.get_text_edit().clear()

    def set_python_output_text(self, text):
        """
        Add text to the python output box.

        Args:
            text (str): The text to set.
        """
        self.output_python_box.get_text_edit().setText(text)

    def get_python_output_text(self):
        """
        Gets the plain text found in the python output box.

        Returns:
            str: Text found inside the python output text edit box.
        """
        return self.output_python_box.get_text_edit().toPlainText()

    def close_window(self):
        """Closes this window"""
        self.close()


if __name__ == "__main__":
    import inspect
    import sys

    with ui_qt_utils.QtApplicationContext():
        window = AttributesToPythonView(version="1.2.3")  # View
        window.set_python_output_text(text=inspect.getsource(sys.modules[__name__]))
        window.show()
