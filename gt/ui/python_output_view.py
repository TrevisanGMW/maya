from gt.ui.syntax_highlighter import PythonSyntaxHighlighter
from gt.ui.line_text_widget import LineTextWidget
import gt.ui.resource_library as ui_res_lib
import gt.ui.qt_utils as ui_qt_utils
import gt.ui.qt_import as ui_qt
from gt.ui import qt_utils
import logging

# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class PythonOutputView(metaclass=ui_qt_utils.MayaWindowMeta):
    def __init__(self, parent=None):
        """
        Initialize the AttributesToPythonView.
        This window represents the main GUI window of the tool.

        Args:
            parent (str): Parent for this window
        """
        super().__init__(parent=parent)

        # Window Title
        self.window_title = "Python Output"
        self.setWindowTitle(self.window_title)

        # Misc
        self.output_python_box = None

        self.create_widgets()
        self.create_layout()

        self.setWindowFlags(
            self.windowFlags()
            | ui_qt.QtLib.WindowFlag.WindowMaximizeButtonHint
            | ui_qt.QtLib.WindowFlag.WindowMinimizeButtonHint
        )
        self.setWindowIcon(ui_qt.QtGui.QIcon(ui_res_lib.Icon.dev_code))

        stylesheet = ui_res_lib.Stylesheet.scroll_bar_base
        stylesheet += ui_res_lib.Stylesheet.maya_dialog_base
        stylesheet += ui_res_lib.Stylesheet.list_widget_base
        self.setStyleSheet(stylesheet)
        qt_utils.resize_to_screen(self, percentage=40, width_percentage=55)
        qt_utils.center_window(self)

    def create_widgets(self):
        """Create the widgets for the window."""

        self.output_python_box = LineTextWidget(self)

        self.output_python_box.setMinimumHeight(150)
        PythonSyntaxHighlighter(self.output_python_box.get_text_edit().document())

        self.output_python_box.setSizePolicy(
            self.output_python_box.sizePolicy().Expanding, self.output_python_box.sizePolicy().Expanding
        )

    def create_layout(self):
        """Create the layout for the window."""
        mid_layout = ui_qt.QtWidgets.QVBoxLayout()
        mid_layout.addWidget(self.output_python_box)
        mid_layout.setContentsMargins(0, 5, 0, 5)  # L-T-R-B

        main_layout = ui_qt.QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        top_layout = ui_qt.QtWidgets.QVBoxLayout()
        bottom_layout = ui_qt.QtWidgets.QVBoxLayout()

        top_layout.setContentsMargins(15, 0, 15, 15)  # L-T-R-B
        main_layout.addLayout(top_layout)
        bottom_layout.addLayout(mid_layout)
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

    with qt_utils.QtApplicationContext():
        window = PythonOutputView()  # View
        window.set_python_output_text(text=inspect.getsource(sys.modules[__name__]))
        window.show()
