"""
Resource Library View
"""

from gt.ui.syntax_highlighter import PythonSyntaxHighlighter
from gt.ui.squared_widget import SquaredWidget
import gt.ui.resource_library as ui_res_lib
import gt.ui.qt_utils as ui_qt_utils
import gt.ui.qt_import as ui_qt


class ResourceLibraryView(metaclass=ui_qt_utils.MayaWindowMeta):
    def __init__(self, parent=None, controller=None, version=None):
        """
        Initialize the ResourceLibraryView.
        This window represents the main GUI window of the tool.

        Args:
            parent (str): Parent for this window
            controller (ResourceLibraryController): ResourceLibraryController, not to be used.
                                                    Here to avoid the garbage collector.  Defaults to None.
            version (str, optional): If provided, it will be used to determine the window title. e.g. Title - (v1.2.3)
        """
        # super(ResourceLibraryView, self).__init__(parent=parent)
        super().__init__(parent=parent)
        self.controller = controller  # Only here so it doesn't get deleted by the garbage collectors
        self.splitter = None
        self.search_bar = None
        self.item_list = None
        self.save_btn = None
        self.preview_image = None
        self.description = None
        self.resource_path = None
        self.source_combo_box = None

        window_title = "Resource Library"
        if version:
            window_title += f" - (v{str(version)})"
        self.setWindowTitle(window_title)

        self.setGeometry(100, 100, 400, 300)

        self.create_widgets()
        self.create_layout()
        self.setWindowFlags(
            self.windowFlags()
            | ui_qt.QtLib.WindowFlag.WindowMaximizeButtonHint
            | ui_qt.QtLib.WindowFlag.WindowMinimizeButtonHint
        )
        self.setWindowIcon(ui_qt.QtGui.QIcon(ui_res_lib.Icon.tool_resource_library))

        stylesheet = ui_res_lib.Stylesheet.scroll_bar_base
        stylesheet += ui_res_lib.Stylesheet.maya_dialog_base
        stylesheet += ui_res_lib.Stylesheet.list_widget_base
        stylesheet += ui_res_lib.Stylesheet.combobox_base
        self.setStyleSheet(stylesheet)
        ui_qt_utils.resize_to_screen(self, percentage=35)
        ui_qt_utils.center_window(self)
        self.resize_splitter_to_screen()

    def update_preview_image(self, new_image=None):
        """
        Update the preview image displayed in the window.

        Args:
            new_image (str, QPixmap, optional): The path to the new image file.
                                                     Defaults to None, which becomes "missing_preview_file"
        """
        if new_image:
            if isinstance(new_image, str):
                new_image = ui_qt.QtGui.QPixmap(new_image)
            self.preview_image.set_pixmap(new_image)
        else:
            self.preview_image.set_pixmap(ui_qt.QtGui.QPixmap(ui_res_lib.Icon.library_missing_file))

    def create_widgets(self):
        """Create the widgets for the window."""
        font = ui_qt.QtGui.QFont()
        font.setPointSize(10)
        self.item_list = ui_qt.QtWidgets.QListWidget()
        self.item_list.setFont(font)
        self.save_btn = ui_qt.QtWidgets.QPushButton("Export Resource")
        self.save_btn.setIcon(ui_qt.QtGui.QIcon(ui_res_lib.Icon.library_build))
        self.save_btn.setStyleSheet(ui_res_lib.Stylesheet.btn_push_bright)
        self.search_bar = ui_qt.QtWidgets.QLineEdit(self)
        self.search_bar.setFont(font)
        self.search_bar.setPlaceholderText("Search...")
        self.preview_image = SquaredWidget(self, center_y=False)
        self.resource_path = ui_qt.QtWidgets.QTextEdit()
        PythonSyntaxHighlighter(self.resource_path.document())
        self.resource_path.setFontPointSize(10)

        self.source_combo_box = ui_qt.QtWidgets.QComboBox()
        self.source_combo_box.setFont(font)
        self.source_combo_box.addItem("All")
        self.source_combo_box.addItem("Package Resources")
        self.source_combo_box.addItem("Package Icons Only")
        self.source_combo_box.addItem("Package Colors Only")
        self.source_combo_box.addItem("Maya Resources")
        self.description = ui_qt.QtWidgets.QLabel("<description>")
        self.description.setFont(font)
        self.description.setAlignment(ui_qt.QtLib.AlignmentFlag.AlignCenter)
        # Initial Image Update
        self.update_preview_image()

    def create_layout(self):
        """Create the layout for the window."""
        search_layout = ui_qt.QtWidgets.QHBoxLayout()
        search_layout.addWidget(self.search_bar, 2)
        search_layout.addWidget(self.source_combo_box, 1)

        list_container = ui_qt.QtWidgets.QWidget()
        list_layout = ui_qt.QtWidgets.QVBoxLayout()
        list_layout.addLayout(search_layout)
        list_layout.addWidget(self.item_list)
        list_container.setLayout(list_layout)
        list_container.setMinimumWidth(200)
        list_container.setMinimumHeight(200)

        preview_container = ui_qt.QtWidgets.QWidget()
        side_menu_layout = ui_qt.QtWidgets.QVBoxLayout()
        side_menu_layout.addWidget(self.description)
        side_menu_layout.addWidget(self.preview_image)
        side_menu_layout.addWidget(self.resource_path)
        side_menu_layout.addWidget(self.save_btn)
        preview_container.setLayout(side_menu_layout)
        preview_container.setMinimumWidth(200)
        preview_container.setMinimumHeight(200)

        self.splitter = ui_qt.QtWidgets.QSplitter(self)
        self.splitter.setHandleWidth(5)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.addWidget(list_container)
        self.splitter.addWidget(preview_container)

        main_layout = ui_qt.QtWidgets.QHBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 11)  # Make Margins Uniform LTRB
        main_layout.addWidget(self.splitter)

    def update_resource_path(self, text):
        """
        Updates the text content of the resource path
        Args:
            text (str): New text to be displayed in the resource path box.
        """
        self.resource_path.setText(text)

    def resize_splitter_to_screen(self, percentage=20):
        """
        Resizes the splitter to match a percentage of the screen size.

        Args:
            percentage (int, optional): The percentage of the screen size that the window should inherit.
                                        Must be a value between 0 and 100. Default is 20.

        Raises:
            ValueError: If the percentage is not within the range [0, 100].
        """
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage should be between 0 and 100")
        if ui_qt.IS_PYSIDE6:
            screen = ui_qt.QtGui.QGuiApplication.primaryScreen()
            screen_geometry = screen.availableGeometry()
        else:
            screen_geometry = ui_qt.QtWidgets.QDesktopWidget().availableGeometry(self)
        width = screen_geometry.width() * percentage / 100
        self.splitter.setSizes([width * 0.2, width * 0.60])

    def clear_view_library(self):
        """
        Clears (removes) all items from the QListWidgetItem.
        """
        self.item_list.clear()

    def add_item_view_library(self, item_name, hex_color=None, icon=None, metadata=None):
        """
        Updates the view with the provided items.

        Args:
            item_name (str): A name for the item that will be added to the list
            hex_color (str, optional): A string with a hex color to be used for the added item (e.g. "#FF0000" = Red)
            icon (QIcon, optional): A icon to be added in front of the item name
            metadata (dict, optional): If provided, this will be added as metadata to the item.
        """
        _item = ui_qt.QtWidgets.QListWidgetItem(item_name)
        if hex_color and isinstance(hex_color, str):
            _item.setForeground(ui_qt.QtGui.QColor(hex_color))
        if icon and isinstance(icon, ui_qt.QtGui.QIcon):
            _item.setIcon(icon)
        if metadata and isinstance(metadata, dict):
            _item.setData(ui_qt.QtLib.ItemDataRole.UserRole, metadata)
        self.item_list.addItem(_item)

    def update_item_description(self, new_title, new_description):
        """
        Updates the curve description label (text) with the given new description.
        Args:
            new_title (str): Title for the curve description.
            new_description (str): The curve description to display. (output text)
        """
        _title = ""
        if new_title and isinstance(new_title, str):
            _title = f"{new_title}: "
        if new_description:
            ui_qt_utils.update_formatted_label(
                target_label=self.description,
                text=_title,
                text_size=3,
                text_color="grey",
                output_text=new_description,
                output_size=3,
                output_color="white",
                overall_alignment="center",
            )

    def moveEvent(self, event):
        """
        Move Event, called when the window is moved (must use this name "moveEvent").
        Updates the maximum size of the description according to the scale factor of the current screen.
        """
        default_maximum_height_description = 20
        default_maximum_height_resource = 50
        scale_factor = 1  # Default scale factor if no screen is found

        if ui_qt.IS_PYSIDE6:
            screen = ui_qt.QtGui.QGuiApplication.screenAt(self.mapToGlobal(self.rect().center()))
            if screen:
                scale_factor = screen.devicePixelRatio()
        else:
            desktop = ui_qt.QtWidgets.QDesktopWidget()
            screen_number = desktop.screenNumber(self)
            scale_factor = ui_qt_utils.get_screen_dpi_scale(screen_number)

        # Apply the scale factor to set the maximum height
        self.description.setMaximumHeight(default_maximum_height_description * scale_factor)
        self.resource_path.setMaximumHeight(default_maximum_height_resource * scale_factor)


if __name__ == "__main__":
    with ui_qt_utils.QtApplicationContext():
        window = ResourceLibraryView()
        mocked_icon = ui_qt.QtGui.QIcon(ui_res_lib.Icon.curve_library_base_curve)
        window.add_item_view_library(
            item_name="item_one", icon=ui_qt.QtGui.QIcon(ui_res_lib.Icon.curve_library_user_curve)
        )
        window.add_item_view_library(
            item_name="item_two", icon=ui_qt.QtGui.QIcon(ui_res_lib.Icon.curve_library_control)
        )
        for index in range(1, 101):
            window.add_item_view_library(
                item_name=f"item_with_a_very_long_name_for_testing_ui_{index}", icon=mocked_icon
            )
        window.show()
