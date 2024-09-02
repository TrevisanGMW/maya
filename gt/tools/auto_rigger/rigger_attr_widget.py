"""
Auto Rigger Attr Widgets
"""

import gt.tools.auto_rigger.rigger_orient_view as tools_rig_orient_view
import gt.tools.auto_rigger.rig_constants as tools_rig_const
import gt.tools.auto_rigger.rig_framework as tools_rig_frm
import gt.tools.auto_rigger.rig_utils as tools_rig_utils
import gt.ui.input_window_text as ui_input_window_text
import gt.ui.resource_library as ui_res_lib
import gt.ui.qt_utils as ui_qt_utils
import gt.core.iterable as core_iter
import gt.ui.qt_import as ui_qt
import gt.core.str as core_str
import gt.core.io as core_io
from functools import partial
import logging
import ast


# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# --------------------------------------------------- Base ---------------------------------------------------
class AttrWidget(ui_qt.QtWidgets.QWidget):
    """
    Base Widget for managing attributes of a module.
    """

    PROXY_ROLE = ui_qt.QtLib.ItemDataRole.UserRole
    PARENT_ROLE = ui_qt.QtLib.ItemDataRole.UserRole + 1

    def __init__(self, parent=None, module=None, project=None, refresh_parent_func=None, *args, **kwargs):
        """
        Initialize the AttrWidget.

        Args:
            parent (QWidget): The parent widget.
            module (ModuleGeneric): The module associated with this widget.
            project (RigProject): The project associated with this widget.
            refresh_parent_func (callable): A function used to refresh the widget's parent.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(parent, *args, **kwargs)

        # Basic Variables
        self.project = project
        self.module = module
        self.known_proxies = {}  # Used to populate drop-down lists
        self.table_proxy_basic_wdg = None
        self.table_proxy_parent_wdg = None
        self.mod_name_field = None
        self.mod_prefix_field = None
        self.mod_suffix_field = None
        self.mod_orient_method = None
        self.mod_edit_orient_btn = None
        self.refresh_parent_func = None

        if refresh_parent_func:
            self.set_refresh_parent_func(refresh_parent_func)

        # Content Layout
        self.content_layout = ui_qt.QtWidgets.QVBoxLayout()
        self.content_layout.setAlignment(ui_qt.QtLib.AlignmentFlag.AlignTop)

        # Create Layout
        self.scroll_content_layout = ui_qt.QtWidgets.QVBoxLayout(self)
        self.scroll_content_layout.setAlignment(ui_qt.QtLib.AlignmentFlag.AlignTop)
        self.scroll_content_layout.addLayout(self.content_layout)

    # Parameter Widgets ----------------------------------------------------------------------------------------
    def add_widget_module_header(self):
        """
        Adds the header for controlling a module. With Icon, Type, Name and modify buttons.
        """
        # Module Header (Icon, Type, Name, Buttons)
        _layout = ui_qt.QtWidgets.QHBoxLayout()
        _layout.setContentsMargins(0, 0, 0, 5)  # L-T-R-B
        _layout.setAlignment(ui_qt.QtLib.AlignmentFlag.AlignTop)

        # Active Checkbox
        active_chk = ui_qt.QtWidgets.QCheckBox()
        active_chk.setChecked(self.module.is_active())
        active_chk.setStyleSheet("QCheckBox { spacing: 0px; }")
        active_chk.setToolTip("Module Active State")
        active_chk.stateChanged.connect(self.on_checkbox_active_state_changed)
        _layout.addWidget(active_chk)

        # Icon
        icon = ui_qt.QtGui.QIcon(self.module.icon)
        icon_label = ui_qt.QtWidgets.QLabel()
        icon_label.setPixmap(icon.pixmap(32, 32))
        label_tooltip = self.module.get_module_class_name(remove_module_prefix=True, formatted=True, remove_side=True)
        icon_label.setToolTip(label_tooltip)
        _layout.addWidget(icon_label)

        # Type (Module Class)
        module_type = self.module.get_module_class_name(remove_module_prefix=True, formatted=True, remove_side=False)
        _layout.addWidget(ui_qt.QtWidgets.QLabel(f"{module_type}"))

        # Name (User Custom)
        name = self.module.get_name()
        self.mod_name_field = ui_qt_utils.ConfirmableQLineEdit()
        self.mod_name_field.setPlaceholderText(f"<{module_type}>")
        self.mod_name_field.setFixedHeight(35)
        if name:
            self.mod_name_field.setText(name)
        self.mod_name_field.editingFinished.connect(self.set_module_name)
        _layout.addWidget(self.mod_name_field)

        # Edit Button
        edit_mod_btn = ui_qt.QtWidgets.QPushButton()
        edit_mod_btn.setIcon(ui_qt.QtGui.QIcon(ui_res_lib.Icon.rigger_dict))
        edit_mod_btn.setToolTip("Edit Raw Data")
        edit_mod_btn.clicked.connect(self.on_button_edit_module_clicked)
        _layout.addWidget(edit_mod_btn)
        self.content_layout.addLayout(_layout)

        # Delete Button
        delete_mod_btn = ui_qt.QtWidgets.QPushButton()
        delete_mod_btn.setIcon(ui_qt.QtGui.QIcon(ui_res_lib.Icon.ui_delete))
        delete_mod_btn.clicked.connect(self.delete_module)
        _layout.addWidget(delete_mod_btn)

    def add_widget_module_prefix_suffix(self):
        """
        Adds widgets to control the prefix of the module
        """
        _layout = ui_qt.QtWidgets.QHBoxLayout()
        _layout.setContentsMargins(0, 0, 0, 5)  # L-T-R-B
        # Prefix
        prefix_label = ui_qt.QtWidgets.QLabel("Prefix:")
        prefix_label.setFixedWidth(50)
        self.mod_prefix_field = ui_qt_utils.ConfirmableQLineEdit()
        self.mod_prefix_field.setPlaceholderText("<Prefix>")
        self.mod_prefix_field.setFixedHeight(35)
        _layout.addWidget(prefix_label)
        _layout.addWidget(self.mod_prefix_field)
        prefix = self.module.get_prefix()
        self.mod_prefix_field.textChanged.connect(self.set_module_prefix)
        if prefix:
            self.mod_prefix_field.setText(prefix)
        # Suffix
        suffix_label = ui_qt.QtWidgets.QLabel("Suffix:")
        suffix_label.setFixedWidth(50)
        self.mod_suffix_field = ui_qt_utils.ConfirmableQLineEdit()
        self.mod_suffix_field.setPlaceholderText("<Suffix>")
        self.mod_suffix_field.setFixedHeight(35)
        _layout.addWidget(suffix_label)
        _layout.addWidget(self.mod_suffix_field)
        suffix = self.module.get_suffix()
        if suffix:
            self.mod_suffix_field.setText(suffix)
        self.mod_suffix_field.textChanged.connect(self.set_module_suffix)
        self.content_layout.addLayout(_layout)

    def add_widget_module_orientation(self):
        """
        Adds widgets to control the module orientation
        """
        _layout = ui_qt.QtWidgets.QHBoxLayout()
        _layout.setContentsMargins(0, 0, 0, 5)  # L-T-R-B
        # Prefix
        orient_label = ui_qt.QtWidgets.QLabel("Orientation Method:")
        orient_label.setFixedWidth(170)
        self.mod_orient_method = ui_qt.QtWidgets.QComboBox()
        self.mod_orient_method.setFixedHeight(35)

        for method in self.module.get_orientation_data().get_available_methods():
            self.mod_orient_method.addItem(str(method).capitalize())

        self.mod_edit_orient_btn = ui_qt.QtWidgets.QPushButton("Edit Orientation Data")
        self.mod_edit_orient_btn.setFixedHeight(35)

        _layout.addWidget(orient_label)
        _layout.addWidget(self.mod_orient_method)
        _layout.addWidget(self.mod_edit_orient_btn)
        self.mod_orient_method.currentIndexChanged.connect(self.on_orientation_combobox_change)
        self.mod_edit_orient_btn.clicked.connect(self.on_orientation_edit_clicked)

        self.content_layout.addLayout(_layout)

    def add_widget_module_parent(self):
        """
        Adds a widget to control the parent of the module
        """
        _layout = ui_qt.QtWidgets.QHBoxLayout()
        _layout.setContentsMargins(0, 0, 0, 5)  # L-T-R-B
        self.refresh_known_proxy_dict(ignore_list=self.module.get_proxies())
        parent_label = ui_qt.QtWidgets.QLabel("Parent:")
        parent_label.setFixedWidth(60)
        module_parent_combo_box = self.create_widget_parent_combobox(target=self.module)
        _layout.addWidget(parent_label)
        _layout.addWidget(module_parent_combo_box)
        module_parent_combo_box.setMinimumSize(1, 1)
        combo_func = partial(self.on_parent_combo_box_changed, combobox=module_parent_combo_box)
        module_parent_combo_box.currentIndexChanged.connect(combo_func)
        self.content_layout.addLayout(_layout)

    def add_widget_proxy_parent_table(self, table_minimum_height=250):
        """
        Adds a table widget to control proxies with options to determine parent or delete the proxy
        Args:
            table_minimum_height (int): The minimum height of the created table
        """
        _layout = ui_qt.QtWidgets.QVBoxLayout()
        self.table_proxy_parent_wdg = ui_qt.QtWidgets.QTableWidget()
        self.clear_proxy_parent_table()
        columns = ["", "Name", "Parent", "", ""]  # Icon, Name, Parent, Edit, Delete
        self.table_proxy_parent_wdg.setColumnCount(len(columns))
        self.table_proxy_parent_wdg.setHorizontalHeaderLabels(columns)
        header_view = ui_qt_utils.QHeaderWithWidgets()
        self.table_proxy_parent_wdg.setHorizontalHeader(header_view)
        header_view.setSectionResizeMode(0, ui_qt.QtLib.QHeaderView.ResizeToContents)
        header_view.setSectionResizeMode(1, ui_qt.QtLib.QHeaderView.Interactive)
        header_view.setSectionResizeMode(2, ui_qt.QtLib.QHeaderView.Stretch)
        header_view.setSectionResizeMode(3, ui_qt.QtLib.QHeaderView.ResizeToContents)
        header_view.setSectionResizeMode(4, ui_qt.QtLib.QHeaderView.ResizeToContents)
        _layout.addWidget(self.table_proxy_parent_wdg)
        self.table_proxy_parent_wdg.setColumnWidth(1, 110)
        self.table_proxy_parent_wdg.setMinimumHeight(table_minimum_height)
        self.refresh_proxy_parent_table()
        self.table_proxy_parent_wdg.cellChanged.connect(self.on_proxy_parent_table_cell_changed)
        add_proxy_btn = ui_qt.QtWidgets.QPushButton()
        add_proxy_btn.setIcon(ui_qt.QtGui.QIcon(ui_res_lib.Icon.ui_add))
        add_proxy_btn.clicked.connect(self.on_button_add_proxy_clicked)
        add_proxy_btn.setToolTip("Add New Proxy")
        header_view.add_widget(4, add_proxy_btn)
        self.content_layout.addLayout(_layout)

    def add_widget_proxy_basic_table(self):
        """
        Adds a table widget to control the parent of the proxies inside this proxy
        """
        _layout = ui_qt.QtWidgets.QVBoxLayout()
        self.table_proxy_basic_wdg = ui_qt.QtWidgets.QTableWidget()
        self.clear_proxy_basic_table()
        columns = ["", "Name", ""]  # Icon, Name, Edit
        self.table_proxy_basic_wdg.setColumnCount(len(columns))
        self.table_proxy_basic_wdg.setHorizontalHeaderLabels(columns)
        header_view = self.table_proxy_basic_wdg.horizontalHeader()
        header_view.setSectionResizeMode(0, ui_qt.QtLib.QHeaderView.ResizeToContents)
        header_view.setSectionResizeMode(1, ui_qt.QtLib.QHeaderView.Stretch)
        header_view.setSectionResizeMode(2, ui_qt.QtLib.QHeaderView.ResizeToContents)
        _layout.addWidget(self.table_proxy_basic_wdg)
        self.table_proxy_basic_wdg.setColumnWidth(1, 110)
        self.refresh_proxy_basic_table()
        self.content_layout.addLayout(_layout)

    def add_widget_action_buttons(self):
        """
        Adds actions buttons (read proxy, build proxy, etc…)
        """
        _layout = ui_qt.QtWidgets.QHBoxLayout()
        # Build Module Proxy
        build_mod_proxy_btn = ui_qt.QtWidgets.QPushButton("Build Proxy (This Module Only)")
        build_mod_proxy_btn.setIcon(ui_qt.QtGui.QIcon(ui_res_lib.Icon.library_build))
        build_mod_proxy_btn.clicked.connect(self.on_button_build_mod_proxy_clicked)
        build_mod_proxy_btn.setToolTip("Read Scene Data")
        _layout.addWidget(build_mod_proxy_btn)
        # Read Scene Data
        read_scene_data_btn = ui_qt.QtWidgets.QPushButton("Read Scene Data")
        read_scene_data_btn.setIcon(ui_qt.QtGui.QIcon(ui_res_lib.Icon.library_parameters))
        read_scene_data_btn.clicked.connect(self.on_button_read_scene_data_clicked)
        read_scene_data_btn.setToolTip("Read Scene Data")
        _layout.addWidget(read_scene_data_btn)
        self.scroll_content_layout.addLayout(_layout)

    def add_module_attr_widget_text_field(
        self,
        attr_name,
        attr_value=None,
        nice_name=None,
        placeholder=None,
        layout=None,
    ):
        """
        Creates a module attribute text field widget.
        Args:
            attr_name (str): The name of the attribute found in the module class (name of the variable)
                       This name is used to find the variable and set its value in the module instance.
            attr_value (str, optional): The initial value of the attribute used to set the value
                                        of the created widget.
            nice_name (str, optional): If a nice name is provided, that's what is shown in the UI, otherwise an auto
                                       formatted version of the variable name is used instead (title case)
            placeholder (str, optional): If a placeholder is provided, that will be set as the textfield placeholder,
                                         otherwise the attribute name is used instead.
            layout (QBoxLayout, optional): If provided, this layout receives the created element instead of creating
                                           a new QHBoxLayout.

        Returns:
            ConfirmableQLineEdit or tuple: The created QLineEdit object or a tuple with all created QT elements.
        """
        _formatted_attr_name = core_str.snake_to_title(attr_name)
        if nice_name:
            _formatted_attr_name = nice_name
        # Create Layout
        if layout:
            _layout = layout
        else:
            _layout = ui_qt.QtWidgets.QHBoxLayout()
            _layout.setContentsMargins(0, 0, 0, 5)  # L-T-R-B
            self.content_layout.addLayout(_layout)
        # Create Widgets
        label = ui_qt.QtWidgets.QLabel(f"{_formatted_attr_name}:")
        text_field = ui_qt_utils.ConfirmableQLineEdit()
        if attr_value is None:
            attr_value = getattr(self.module, attr_name)
        if placeholder is None:
            placeholder = f"<{attr_name}>"
        text_field.setText(attr_value)
        text_field.setFixedHeight(35)
        text_field.setPlaceholderText(placeholder)
        # Add to Widgets
        _layout.addWidget(label)
        _layout.addWidget(text_field)
        # Connect
        _func = partial(self.set_module_serialized_value_from_field, attr=attr_name, field=text_field)
        text_field.textChanged.connect(_func)
        return text_field

    def add_module_attr_widget_int_slider(
        self, attr_name, attr_value=None, min_int=-10, max_int=10, nice_name=None, layout=None
    ):
        """
        Creates a module attribute text field widget.
        Args:
            attr_name (str): The name of the attribute found in the module class (name of the variable)
                       This name is used to find the variable and set its value in the module instance.
            attr_value (int, optional): The initial value of the attribute used to set the value of the created widget.
            min_int (int, str): Minimum value of the slider and the spinbox.
            max_int (int, str): Maximum value of the slider and the spinbox.
            nice_name (str, optional): If a nice name is provided, that's what is shown in the UI, otherwise an auto
                                       formatted version of the variable name is used instead (title case)
            layout (QBoxLayout, optional): If provided, this layout is used instead of creating a new QHBoxLayout.

        Returns:
            QIntSlider: A QSlider carrying a linked QSpinBox
        """
        _formatted_attr_name = core_str.snake_to_title(attr_name)
        if nice_name:
            _formatted_attr_name = nice_name
        # Create Layout
        if layout:
            _layout = layout
        else:
            _layout = ui_qt.QtWidgets.QHBoxLayout()
            _layout.setContentsMargins(0, 0, 0, 5)  # L-T-R-B
            self.content_layout.addLayout(_layout)
        # Create Widgets
        label = ui_qt.QtWidgets.QLabel(f"{_formatted_attr_name}:")
        int_slider = ui_qt_utils.QIntSlider(ui_qt.QtLib.Orientation.Horizontal)
        spinbox = ui_qt.QtWidgets.QSpinBox()
        int_slider.link_spin_box(spinbox)
        int_slider.set_int_range(min_int=min_int, max_int=max_int)
        if attr_value is None:
            attr_value = getattr(self.module, attr_name)
        int_slider.set_int_value(attr_value)
        # Add to Widgets
        _layout.addWidget(label)
        _layout.addWidget(int_slider)
        _layout.addWidget(spinbox)
        # Connect
        _func = partial(self.set_module_serialized_value_from_field, attr=attr_name, field=int_slider)
        int_slider.intValueChanged.connect(_func)
        return int_slider

    def add_module_attr_widget_double_slider(
        self, attr_name, attr_value=None, min_double=-10, max_double=10, precision=3, nice_name=None, layout=None
    ):
        """
        Creates a module attribute text field widget.
        Args:
            attr_name (str): The name of the attribute found in the module class (name of the variable)
                       This name is used to find the variable and set its value in the module instance.
            attr_value (float, optional): Initial value of the attribute used to set the value of the created widget.
            min_double (int, str): Minimum value of the slider and the spinbox.
            max_double (int, str): Maximum value of the slider and the spinbox.
            precision (int): The precision of the double spin box (decimals)
            nice_name (str, optional): If a nice name is provided, that's what is shown in the UI, otherwise an auto
                                       formatted version of the variable name is used instead (title case)
            layout (QBoxLayout, optional): If provided, this layout is used instead of creating a new QHBoxLayout.

        Returns:
            QDoubleSlider: A QSlider a linked spinbox.
        """
        _formatted_attr_name = core_str.snake_to_title(attr_name)
        if nice_name:
            _formatted_attr_name = nice_name
        # Create Layout
        if layout:
            _layout = layout
        else:
            _layout = ui_qt.QtWidgets.QHBoxLayout()
            _layout.setContentsMargins(0, 0, 0, 5)  # L-T-R-B
            self.content_layout.addLayout(_layout)
        # Create Widgets
        label = ui_qt.QtWidgets.QLabel(f"{_formatted_attr_name}:")
        double_slider = ui_qt_utils.QDoubleSlider(ui_qt.QtLib.Orientation.Horizontal)
        spinbox = ui_qt.QtWidgets.QDoubleSpinBox()
        spinbox.setDecimals(precision)
        double_slider.link_spin_box(spinbox)
        double_slider.set_double_range(min_double=min_double, max_double=max_double)
        if attr_value is None:
            attr_value = getattr(self.module, attr_name)
        double_slider.set_double_value(attr_value)
        # Add to Widgets
        _layout.addWidget(label)
        _layout.addWidget(double_slider)
        _layout.addWidget(spinbox)
        # Connect
        _func = partial(self.set_module_serialized_value_from_field, attr=attr_name, field=double_slider)
        double_slider.doubleValueChanged.connect(_func)
        return double_slider

    def add_module_attr_widget_checkbox(self, attr_name, attr_value=None, nice_name=None, layout=None):
        """
        Creates a module attribute text field widget.
        Args:
            attr_name (str): The name of the attribute found in the module class (name of the variable)
                       This name is used to find the variable and set its value in the module instance.
            attr_value (bool, optional): The initial value of the attribute used to set the value
                                        of the created widget.
            nice_name (str, optional): If a nice name is provided, that's what is shown in the UI, otherwise an auto
                                       formatted version of the variable name is used instead (title case)
            layout (QBoxLayout, optional): If provided, this layout is used instead of creating a new QHBoxLayout.

        Returns:
            QCheckBox: A QCheckBox object.
        """
        _formatted_attr_name = core_str.snake_to_title(attr_name)
        if nice_name:
            _formatted_attr_name = nice_name
        # Create Layout
        if layout:
            _layout = layout
        else:
            _layout = ui_qt.QtWidgets.QHBoxLayout()
            _layout.setContentsMargins(0, 0, 0, 5)  # L-T-R-B
            self.content_layout.addLayout(_layout)
        # Create Widgets
        label = ui_qt.QtWidgets.QLabel(f"{_formatted_attr_name}:")
        checkbox = ui_qt.QtWidgets.QCheckBox()
        if attr_value is None:
            attr_value = getattr(self.module, attr_name)
        checkbox.setChecked(attr_value)
        # Add to Widgets
        _layout.addWidget(label)
        _layout.addWidget(checkbox)
        # Connect
        _func = partial(self.set_module_serialized_value_from_field, attr=attr_name, field=checkbox)
        checkbox.stateChanged.connect(_func)
        return checkbox

    def add_widget_auto_serialized_fields(self, filter_attr=None):
        """
        Automatically creates widgets based on the found attributes.

        Args:
            filter_attr (None, List[str]): A list of attributes (variable names) to ignore.
                                           e.g. ["variable_one"]
        """
        instance_attrs = self.get_module_serialized_attrs()

        for attr_name, attr_value in instance_attrs.items():
            if filter_attr and attr_name in filter_attr:
                continue
            if isinstance(attr_value, str):
                self.add_module_attr_widget_text_field(attr_name=attr_name, attr_value=attr_value)
            if isinstance(attr_value, float):
                self.add_module_attr_widget_double_slider(attr_name=attr_name, attr_value=attr_value)
            if not isinstance(attr_value, bool) and isinstance(attr_value, int):
                self.add_module_attr_widget_int_slider(attr_name=attr_name, attr_value=attr_value)
            if isinstance(attr_value, bool):
                self.add_module_attr_widget_checkbox(attr_name=attr_name, attr_value=attr_value)

    # Utils ---------------------------------------------------------------------------------------------------
    def refresh_current_widgets(self):
        """
        Refreshes available widgets. For example, tables, so they display the correct module name.
        """
        if self.mod_name_field:
            _name = self.module.get_name()
            if _name:
                self.mod_name_field.setText(_name)
        if self.mod_prefix_field:
            _prefix = self.module.get_prefix()
            if _prefix:
                self.mod_prefix_field.setText(_prefix)
        if self.mod_suffix_field:
            _suffix = self.module.get_suffix()
            if _suffix:
                self.mod_suffix_field.setText(_suffix)
        if self.table_proxy_parent_wdg:
            self.refresh_proxy_parent_table()
        if self.table_proxy_basic_wdg:
            self.refresh_proxy_basic_table()

    def refresh_known_proxy_dict(self, ignore_list=None):
        """
        Refreshes the "known_proxies" attribute with all proxies that could be used as parents.
        Args:
            ignore_list (list, optional): A list of proxies to be ignored
        """
        for module in self.project.get_modules():
            for proxy in module.get_proxies():
                if ignore_list and proxy in ignore_list:
                    continue
                self.known_proxies[proxy.get_uuid()] = (proxy, module)

    def refresh_proxy_parent_table(self):
        """
        Refresh the table with proxies associated with the module.
        With extra options to edit parent or delete the proxy.
        """
        self.clear_proxy_parent_table()
        for row, proxy in enumerate(self.module.get_proxies()):
            self.table_proxy_parent_wdg.insertRow(row)
            # Icon ---------------------------------------------------------------------------
            self.insert_item(
                row=row,
                column=0,
                table=self.table_proxy_parent_wdg,
                icon_path=ui_res_lib.Icon.util_reset_transforms,
                editable=False,
                centered=True,
            )

            # Name ---------------------------------------------------------------------------
            self.insert_item(
                row=row, column=1, table=self.table_proxy_parent_wdg, text=proxy.get_name(), data_object=proxy
            )

            # Parent Combobox ----------------------------------------------------------------
            self.refresh_known_proxy_dict()
            combo_box = self.create_widget_parent_combobox(target=proxy, parent_filter=False)
            combo_func = partial(self.on_table_parent_combo_box_changed, source_row=row, source_col=2)
            combo_box.currentIndexChanged.connect(combo_func)
            self.table_proxy_parent_wdg.setCellWidget(row, 2, combo_box)

            # Edit Proxy ---------------------------------------------------------------------
            edit_proxy_btn = ui_qt.QtWidgets.QPushButton()
            edit_proxy_btn.setIcon(ui_qt.QtGui.QIcon(ui_res_lib.Icon.rigger_dict))
            edit_proxy_func = partial(self.on_button_edit_proxy_clicked, proxy=proxy)
            edit_proxy_btn.clicked.connect(edit_proxy_func)
            edit_proxy_btn.setToolTip("Edit Raw Data")
            self.table_proxy_parent_wdg.setCellWidget(row, 3, edit_proxy_btn)

            # Delete Setup --------------------------------------------------------------------
            delete_proxy_btn = ui_qt.QtWidgets.QPushButton()
            delete_proxy_btn.setIcon(ui_qt.QtGui.QIcon(ui_res_lib.Icon.ui_delete))
            delete_proxy_func = partial(self.delete_proxy, proxy=proxy)
            delete_proxy_btn.clicked.connect(delete_proxy_func)
            delete_proxy_btn.setToolTip("Delete Proxy")
            self.table_proxy_parent_wdg.setCellWidget(row, 4, delete_proxy_btn)

    def refresh_proxy_basic_table(self):
        """
        Refresh the table with proxies associated with the module.
        """
        self.clear_proxy_basic_table()
        for row, proxy in enumerate(self.module.get_proxies()):
            self.table_proxy_basic_wdg.insertRow(row)
            # Icon ---------------------------------------------------------------------------
            self.insert_item(
                row=row,
                column=0,
                table=self.table_proxy_basic_wdg,
                icon_path=ui_res_lib.Icon.util_reset_transforms,
                editable=False,
                centered=True,
            )

            # Name ---------------------------------------------------------------------------
            self.insert_item(
                row=row, column=1, table=self.table_proxy_basic_wdg, text=proxy.get_name(), data_object=proxy
            )

            # Edit Proxy ---------------------------------------------------------------------
            edit_proxy_btn = ui_qt.QtWidgets.QPushButton()
            edit_proxy_btn.setIcon(ui_qt.QtGui.QIcon(ui_res_lib.Icon.rigger_dict))
            edit_proxy_func = partial(self.on_button_edit_proxy_clicked, proxy=proxy)
            edit_proxy_btn.clicked.connect(edit_proxy_func)
            edit_proxy_btn.setToolTip("Edit Raw Data")
            self.table_proxy_basic_wdg.setCellWidget(row, 2, edit_proxy_btn)

    def update_proxy_from_raw_data(self, data_getter, proxy):
        """
        Updates a proxy description using raw string data.
        Args:
            data_getter (callable): A function used to retrieve the data string
            proxy (Proxy): A proxy object to be updated using the data
        """
        data = data_getter()
        try:
            _data_as_dict = ast.literal_eval(data)
            proxy.read_data_from_dict(_data_as_dict)
            self.refresh_current_widgets()
        except Exception as e:
            raise Exception(f'Unable to set proxy attributes from provided raw data. Issue: "{e}".')

    def update_module_from_raw_data(self, data_getter, module):
        """
        Updates a proxy description using raw string data.
        Used with "on_button_edit_module_clicked" to update modules from raw data.
        Args:
            data_getter (callable): A function used to retrieve the data string
            module (ModuleGeneric): A module object to be updated using the data
        """
        data = data_getter()
        try:
            _data_as_dict = ast.literal_eval(data)
            module.read_data_from_dict(_data_as_dict)
            self.refresh_current_widgets()
            self.call_parent_refresh()
        except Exception as e:
            raise Exception(f'Unable to set module attributes from provided raw data. Issue: "{e}".')

    def clear_proxy_parent_table(self):
        if self.table_proxy_parent_wdg:
            self.table_proxy_parent_wdg.setRowCount(0)

    def clear_proxy_basic_table(self):
        if self.table_proxy_basic_wdg:
            self.table_proxy_basic_wdg.setRowCount(0)

    def insert_item(self, row, column, table, text=None, data_object=None, icon_path="", editable=True, centered=True):
        """
        Insert an item into the table.

        Args:
            row (int): Row index.
            column (int): Column index.
            table (QTableWidget): Target table.
            text (str): Text to display in the item.
            data_object: The associated data object.
            icon_path (str): Path to the icon. (If provided, text is ignored)
            editable (bool): Whether the item is editable.
            centered (bool): Whether the text should be centered.
        """
        item = ui_qt.QtWidgets.QTableWidgetItem(text)
        self.set_table_item_proxy_object(item, data_object)

        if icon_path != "":
            icon = ui_qt.QtGui.QIcon(icon_path)
            icon_label = ui_qt.QtWidgets.QLabel()
            icon_label.setPixmap(icon.pixmap(32, 32))
            icon_label.setAlignment(ui_qt.QtLib.AlignmentFlag.AlignCenter)
            table.setCellWidget(row, column, icon_label)
            return

        if centered:
            item.setTextAlignment(ui_qt.QtLib.AlignmentFlag.AlignHCenter | ui_qt.QtLib.AlignmentFlag.AlignVCenter)

        if not editable:
            item.setFlags(ui_qt.QtLib.ItemFlag.ItemIsEnabled | ui_qt.QtLib.ItemFlag.ItemIsSelectable)

        if table:
            table.setItem(row, column, item)

    def on_table_parent_combo_box_changed(self, index, source_row, source_col):
        """
        Handle the change in the parent combo box for the proxy table.

        Args:
            index (int): Index of the selected item.
            source_row (int): Row index.
            source_col (int): Column index.
        """
        _name_cell = self.table_proxy_parent_wdg.item(source_row, 1)
        _proxy = self.get_table_item_proxy_object(_name_cell)
        _combo_box = self.table_proxy_parent_wdg.cellWidget(source_row, source_col)
        _parent_proxy = _combo_box.itemData(index)
        if _parent_proxy is None:
            _proxy.clear_parent_uuid()
            logger.debug(f"{_proxy.get_name()}: to : None")
        else:
            _proxy.set_parent_uuid(_parent_proxy.get_uuid())
            logger.debug(f"{_proxy.get_name()}: to : {_parent_proxy.get_name()}")
        self.refresh_proxy_parent_table()

    def on_parent_combo_box_changed(self, index, combobox):
        """
        Handle the change in the parent combo box for the proxy table.

        Args:
            index (int): Index of the selected item.
            combobox (QComboBox): A module parent combo box QT object.
        """
        _parent_proxy = combobox.itemData(index)
        if _parent_proxy is None:
            self.module.clear_parent_uuid()
            logger.debug(f"{self.module.get_name()}: to : None")
        else:
            self.module.set_parent_uuid(_parent_proxy.get_uuid())
            logger.debug(f"{self.module.get_name()}: to : {_parent_proxy.get_name()}")
        self.call_parent_refresh()

    def on_proxy_parent_table_cell_changed(self, row, column):
        """
        Updates the name of the proxy object in case the user writes a new name in the name cell.
        Args:
            row (int): Row where the cell changed.
            column (int): Column where the cell changed.
        """
        _source_table = self.table_proxy_parent_wdg
        _source_table.cellChanged.disconnect(self.on_proxy_parent_table_cell_changed)  # Fix recursion errors
        _name_cell = _source_table.item(row, 1)  # 1 = Name
        _proxy = self.get_table_item_proxy_object(_name_cell)
        current_name = _proxy.get_name()
        new_name = _name_cell.text()
        if new_name:
            _proxy.set_name(new_name)
            self.refresh_proxy_parent_table()
        else:
            _name_cell.setText(current_name)
        _source_table.cellChanged.connect(self.on_proxy_parent_table_cell_changed)  # Fix recursion errors

    def on_orientation_combobox_change(self, index):
        """
        Determines the module orientation method and updates the UI to allow edits.
        Args:
            index (int): Combo box index change (used to retrieve text item)
        """
        method = self.mod_orient_method.itemText(index)
        self.module.set_orientation_method(method=method.lower())
        self.mod_edit_orient_btn.setEnabled(False)
        if method.lower() == tools_rig_frm.OrientationData.Methods.automatic.lower():
            self.mod_edit_orient_btn.setEnabled(True)

    def on_orientation_edit_clicked(self):
        """
        Open edit orientation data edit view for the current module
        """
        edit_orient_window = tools_rig_orient_view.RiggerOrientView(parent=self, module=self.module)
        edit_orient_window.show()

    def on_button_edit_proxy_clicked(self, proxy):
        """
        Shows a text-editor window with the proxy converted to a dictionary (raw data)
        If the user applies the changes, and they are considered valid, the proxy is updated with it.
        Args:
            proxy (Proxy): The target proxy (proxy to be converted to dictionary)
        """
        param_win = ui_input_window_text.InputWindowText(
            parent=self,
            message=f'Editing Raw Data for the Proxy "{proxy.get_name()}"',
            window_title=f'Raw data for "{proxy.get_name()}"',
            image=ui_res_lib.Icon.rigger_dict,
            window_icon=ui_res_lib.Icon.library_parameters,
            image_scale_pct=10,
            is_python_code=True,
        )
        param_win.set_confirm_button_text("Apply")
        proxy_raw_data = proxy.get_proxy_as_dict(
            include_uuid=True, include_transform_data=True, include_offset_data=True
        )
        formatted_dict = core_iter.dict_as_formatted_str(proxy_raw_data, one_key_per_line=True)
        param_win.set_text_field_text(formatted_dict)
        confirm_button_func = partial(self.update_proxy_from_raw_data, param_win.get_text_field_text, proxy)
        param_win.confirm_button.clicked.connect(confirm_button_func)
        param_win.show()

    def on_button_edit_module_clicked(self, skip_proxies=True, *args):
        """
        Shows a text-editor window with the module converted to a dictionary (raw data)
        If the user applies the changes, and they are considered valid, the module is updated with it.
        Args:
            skip_proxies (bool, optional): If active, the "proxies" key will be ignored.
            *args: Variable-length argument list. - Here to avoid issues with the "skip_proxies" argument.
        """
        module_name = self.module.get_name()
        if not module_name:
            module_name = self.module.get_module_class_name(remove_module_prefix=True)
        param_win = ui_input_window_text.InputWindowText(
            parent=self,
            message=f'Editing Raw Data for the Module "{module_name}"',
            window_title=f'Raw data for "{module_name}"',
            image=ui_res_lib.Icon.rigger_dict,
            window_icon=ui_res_lib.Icon.library_parameters,
            image_scale_pct=10,
            is_python_code=True,
        )
        param_win.set_confirm_button_text("Apply")
        module_raw_data = self.module.get_module_as_dict(include_module_name=False, include_offset_data=True)
        if "proxies" in module_raw_data and skip_proxies:
            module_raw_data.pop("proxies")
        formatted_dict = core_iter.dict_as_formatted_str(module_raw_data, one_key_per_line=True)
        param_win.set_text_field_text(formatted_dict)
        confirm_button_func = partial(self.update_module_from_raw_data, param_win.get_text_field_text, self.module)
        param_win.confirm_button.clicked.connect(confirm_button_func)
        param_win.show()

    def on_button_add_proxy_clicked(self):
        """
        Adds a new proxy to the current module and refreshes the UI
        """
        self.module.add_new_proxy()
        self.refresh_current_widgets()

    def on_button_read_scene_data_clicked(self):
        """
        Reads proxy data from scene
        """
        logger.info(f"Data for this module from the scene")  # TODO
        self.module.read_data_from_scene()
        self.refresh_current_widgets()

    def on_button_build_mod_proxy_clicked(self):
        """
        Reads proxy data from scene
        """
        proxy_grp = tools_rig_utils.find_root_group_proxy()
        if proxy_grp:
            message_box = ui_qt.QtWidgets.QMessageBox(self)
            message_box.setWindowTitle(f"Proxy detected in the scene.")
            message_box.setText(f"A pre-existing proxy was detected in the scene. \n" f"How would you like to proceed?")

            message_box.addButton("Delete Proxy and Rebuild", ui_qt.QtLib.ButtonRoles.ActionRole)
            message_box.addButton("Cancel", ui_qt.QtLib.ButtonRoles.RejectRole)
            question_icon = ui_qt.QtGui.QIcon(ui_res_lib.Icon.ui_exclamation)
            message_box.setIconPixmap(question_icon.pixmap(64, 64))
            result = message_box.exec_()
            if result == 0:
                import maya.cmds as cmds

                cmds.delete(proxy_grp)
            else:
                return
        a_project = tools_rig_frm.RigProject()
        a_project.add_to_modules(module=self.module, set_parent_project=False)
        a_project.build_proxy()

    def on_checkbox_active_state_changed(self, state):
        """
        Uses the state of the checkbox to determine the active state of the module
        Args:
            state (bool): If True, the state of the module will be set to Active. If False, to Inactive.
        """
        self.module.set_active_state(is_active=bool(state))
        self.call_parent_refresh()

    def create_widget_parent_combobox(self, target, parent_filter=True):
        """
        Creates a populated combobox with all potential parent targets.
        An extra initial item called "No Parent" is also added for the proxies without parents.
        Current parent is pre-selected during creation.
        Args:
            target (Proxy, Module): A proxy or module object used to determine current parent and pre-select it.
            parent_filter (bool, optional): If True, it will only populate the combobox with proxies available under
                                          the parent modules.
        Returns:
            QComboBox: A pre-populated combobox with potential parents. Current parent is also pre-selected.
        """
        self.refresh_known_proxy_dict()

        combobox = ui_qt.QtWidgets.QComboBox()
        combobox.addItem("No Parent", None)

        # Get Variables
        _proxy_uuid = None
        if target and hasattr(target, "get_uuid"):  # Is proxy
            _proxy_uuid = target.get_uuid()
        _proxy_parent_uuid = target.get_parent_uuid()
        _parent_module = self.known_proxies.get(_proxy_parent_uuid, None)
        if _parent_module:
            _parent_module = _parent_module[1]  # Get second item in tuple (module)
        # Populate Combobox
        for key, (_proxy, _module) in self.known_proxies.items():
            if parent_filter and _parent_module and _parent_module != _module:
                continue
            if key == _proxy_uuid:
                continue  # Skip Itself
            description = f"{str(_proxy.get_name())}"
            module_name = _module.get_name()
            if module_name:
                description += f" : {str(module_name)}"
            # description += f' ({str(key)})'
            combobox.addItem(description, _proxy)

        # Unknown Target (Not present in any of the modules)
        if _proxy_parent_uuid and _proxy_parent_uuid in self.known_proxies:
            for index in range(combobox.count()):
                _parent_proxy = combobox.itemData(index)
                if _parent_proxy and _proxy_parent_uuid == _parent_proxy.get_uuid():
                    combobox.setCurrentIndex(index)
        elif _proxy_parent_uuid and _proxy_parent_uuid not in self.known_proxies:
            description = f"unknown : ???"
            description += f" ({str(_proxy_parent_uuid)})"
            combobox.addItem(description, None)
            combobox.setCurrentIndex(combobox.count() - 1)  # Last item, which was just added
        return combobox

    def call_parent_refresh(self):
        """
        Calls the refresh parent function. This function needs to first be set before it can be used.
        In case it has not been set, or it's missing, the operation will be ignored.
        """
        if not self.refresh_parent_func or not callable(self.refresh_parent_func):
            logger.debug(f"Unable to call refresh tree function. Function has not been set or is missing.")
            return
        self.refresh_parent_func()

    def delete_proxy(self, proxy):
        _proxy_name = proxy.get_name()
        message_box = ui_qt.QtWidgets.QMessageBox(self)
        message_box.setWindowTitle(f'Delete Proxy "{str(_proxy_name)}"?')
        message_box.setText(f'Are you sure you want to delete proxy "{str(_proxy_name)}"?')
        question_icon = ui_qt.QtGui.QIcon(ui_res_lib.Icon.ui_delete)
        message_box.setIconPixmap(question_icon.pixmap(64, 64))
        message_box.addButton(ui_qt.QtLib.StandardButton.Yes)
        message_box.addButton(ui_qt.QtLib.StandardButton.No)
        result = message_box.exec_()
        if result == ui_qt.QtLib.StandardButton.Yes:
            self.module.remove_from_proxies(proxy)
            self.refresh_known_proxy_dict()
            self.refresh_current_widgets()

    def delete_module(self):
        _module_name = self.module.get_name() or ""
        _module_class = self.module.get_module_class_name(remove_module_prefix=False)
        if _module_name:
            _module_name = f'\n"{_module_name}" ({_module_class})'
        else:
            _module_name = f"\n{_module_class}"
        message_box = ui_qt.QtWidgets.QMessageBox(self)
        message_box.setWindowTitle(f"Delete Module {str(_module_name)}?")
        message_box.setText(f"Are you sure you want to delete module {str(_module_name)}?")
        question_icon = ui_qt.QtGui.QIcon(ui_res_lib.Icon.ui_delete)
        message_box.setIconPixmap(question_icon.pixmap(64, 64))
        message_box.addButton(ui_qt.QtLib.StandardButton.Yes)
        message_box.addButton(ui_qt.QtLib.StandardButton.No)
        result = message_box.exec_()
        if result == ui_qt.QtLib.StandardButton.Yes:
            self.project.remove_from_modules(self.module)
            self.call_parent_refresh()
            self.toggle_content_visibility()

    # Setters --------------------------------------------------------------------------------------------------
    def set_module_name(self):
        """
        Set the name of the module based on the text in the name text field.
        """
        new_name = self.mod_name_field.text() or ""
        self.module.set_name(new_name)
        self.refresh_current_widgets()
        self.call_parent_refresh()

    def set_module_prefix(self):
        """
        Set the name of the module based on the text in the name text field.
        """
        new_prefix = self.mod_prefix_field.text() or ""
        self.module.set_prefix(new_prefix)
        self.refresh_current_widgets()

    def set_module_suffix(self):
        """
        Set the name of the module based on the text in the name text field.
        """
        new_suffix = self.mod_suffix_field.text() or ""
        self.module.set_suffix(new_suffix)
        self.refresh_current_widgets()

    def set_table_item_proxy_object(self, item, proxy):
        """
        Set the proxy object as data for a table item.

        Args:
            item (QTableWidgetItem): The table item.
            proxy (Proxy): The proxy object.
        """
        item.setData(self.PROXY_ROLE, proxy)

    def set_refresh_parent_func(self, func):
        """
        Set the function to be called for refreshing the parent widget.
        Args:
        func (callable): The function to be set as the refresh table function.
        """
        if not callable(func):
            logger.warning(f"Unable to parent refresh function. Provided argument is not a callable object.")
            return
        self.refresh_parent_func = func

    def toggle_content_visibility(self):
        """
        Updates the visibility of the "scroll_content_layout" to the opposite of its value.
        """
        self.scroll_content_layout.parent().setHidden(not self.scroll_content_layout.parent().isHidden())

    def set_module_serialized_value_from_field(self, *args, attr, field):
        """
        If the provided attribute name is available in the module, this functions tries to set it.
        Args:
            args (any): Used to receive the change from the incoming QtWidget
            attr (str): Name of the attribute.
            field (QtWidget): A QtWidget object to get the value from
        """
        _value = None
        if isinstance(field, ui_qt.QtWidgets.QLineEdit):
            _value = field.text()
        if isinstance(field, ui_qt_utils.QDoubleSlider):
            _value = field.double_value()
        if isinstance(field, ui_qt_utils.QIntSlider):
            _value = field.int_value()
        if isinstance(field, ui_qt.QtWidgets.QCheckBox):
            _value = field.isChecked()
        if hasattr(self.module, attr):
            setattr(self.module, attr, _value)
        else:
            logger.warning(f'Unable to set missing attribute. Attr: "{attr}". Type: "{type(self.module)}".')

    # Getters --------------------------------------------------------------------------------------------------
    def get_table_item_proxy_object(self, item):
        """
        Get the proxy object associated with a table item.

        Args:
            item (QTableWidgetItem): The table item.

        Returns:
            Proxy or None: The associated proxy object, None otherwise.
        """
        return item.data(self.PROXY_ROLE)

    def get_module_serialized_attrs(self):
        """
        Gets a dictionary containing the name and value for all class attributes except the manually serialized ones.
        Private variables starting with an underscore are ignored. e.g. "self._private" will not be returned.
        Returns:
            dict: A dictionary containing any attributes and their values.
            e.g. A class has an attribute "self.ctrl_visibility" set to True. This function will return:
            {"ctrl_visibility": True}, which can be serialized.
        """
        if not self.module:
            return {}
        _manually_serialized = tools_rig_const.RiggerConstants.CLASS_ATTR_SKIP_AUTO_SERIALIZATION
        _result = {}
        for key, value in self.module.__dict__.items():
            if key not in _manually_serialized and not key.startswith("_"):
                if core_io.is_json_serializable(data=value, allow_none=False):  # Skip proxies and other elements.
                    _result[key] = value
        return _result


class AttrWidgetCommon(AttrWidget):
    def __init__(self, parent=None, *args, **kwargs):
        """
        Initialize the AttrWidgetCommon.
        Used for modules that are missing a proper unique AttrWidget.
        The "AttrWidgetCommon" will show all proxies (with the edit options)
        And automatically list all available attributes.

        Args:
            parent (QWidget): The parent widget.
            module: The module associated with this widget.
            project: The project associated with this widget.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(parent, *args, **kwargs)

        self.add_widget_module_header()
        self.add_widget_module_prefix_suffix()
        self.add_widget_module_parent()
        self.add_widget_proxy_basic_table()
        self.add_widget_auto_serialized_fields()
        self.add_widget_action_buttons()


# -------------------------------------------------- Modules --------------------------------------------------
class AttrWidgetModuleGeneric(AttrWidget):
    def __init__(self, parent=None, *args, **kwargs):
        """
        Initialize the AttrWidgetModuleGeneric.
        Used for generic nodes with options to edit parents and proxies directly.

        Args:
            parent (QWidget): The parent widget.
            module: The module associated with this widget.
            project: The project associated with this widget.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(parent, *args, **kwargs)

        self.add_widget_module_header()
        self.add_widget_module_prefix_suffix()
        self.add_widget_module_orientation()
        self.add_widget_proxy_parent_table()
        self.add_widget_action_buttons()


class AttrWidgetModuleSpine(AttrWidget):
    def __init__(self, parent=None, *args, **kwargs):
        """
        Initialize the AttrWidgetModuleSpine.
        Used for generic nodes with options to edit parents and proxies directly.
        """
        super().__init__(parent, *args, **kwargs)

        self.add_widget_module_header()
        self.add_widget_module_prefix_suffix()
        self.add_widget_module_parent()
        self.add_widget_proxy_basic_table()
        self.add_widget_auto_serialized_fields(filter_attr=["dropoff_rate"])  # Dropoff has specific range
        self.add_module_attr_widget_double_slider(attr_name="dropoff_rate", min_double=0.1, max_double=10)
        self.add_widget_action_buttons()


class AttrWidgetModuleHead(AttrWidget):
    def __init__(self, parent=None, *args, **kwargs):
        """
        Initialize the AttrWidgetModuleHead.
        Used for generic nodes with options to edit parents and proxies directly.
        """
        super().__init__(parent, *args, **kwargs)

        self.add_widget_module_header()
        self.add_widget_module_prefix_suffix()
        self.add_widget_module_parent()
        self.add_widget_proxy_basic_table()
        self.add_widget_auto_serialized_fields(filter_attr=["dropoff_rate"])  # Dropoff has specific range
        self.add_module_attr_widget_double_slider(attr_name="dropoff_rate", min_double=0.1, max_double=10)
        self.add_widget_action_buttons()


class AttrWidgetModuleBipedArm(AttrWidget):
    def __init__(self, parent=None, *args, **kwargs):
        """
        Initialize the AttrWidgetModuleBipedArm.
        Used for generic nodes with options to edit parents and proxies directly.
        """
        super().__init__(parent, *args, **kwargs)

        self.add_widget_module_header()
        self.add_widget_module_prefix_suffix()
        self.add_widget_module_parent()
        self.add_widget_proxy_basic_table()
        self.add_widget_auto_serialized_fields(filter_attr=["rig_pose_elbow_rot"])  # Dropoff has specific range
        self.add_module_attr_widget_double_slider(
            attr_name="rig_pose_elbow_rot",
            min_double=-180,
            max_double=180,
            nice_name="Control Pose Knee Rotation",
        )
        self.add_widget_action_buttons()


class AttrWidgetModuleBipedFinger(AttrWidget):
    def __init__(self, parent=None, *args, **kwargs):
        """
        Initialize the AttrWidgetModuleBipedFinger.
        Used for generic nodes with options to edit parents and proxies directly.
        """
        super().__init__(parent, *args, **kwargs)

        self.add_widget_module_header()
        self.add_widget_module_prefix_suffix()
        self.add_widget_module_parent()
        self.add_widget_proxy_basic_table()
        # self.add_widget_auto_serialized_fields(filter_attr=[])  # Dropoff has specific range
        # _layout = ui_qt.QtWidgets.QVBoxLayout()
        # self.add_module_attr_widget_double_slider(
        #     attr_name="rig_pose_elbow_rot",
        #     min_double=-180,
        #     max_double=180,
        #     nice_name="Control Pose Knee Rotation",
        #     layout=_layout,
        # )
        textfield_names = "Name"
        finger_mapping = {
            "meta": "meta_name",
            "thumb": "thumb_name",
            "index": "index_name",
            "middle": "middle_name",
            "ring": "ring_name",
            "pinky": "pinky_name",
            "extra": "extra_name",
        }
        # Add Other Attributes
        ignore_attrs = list(finger_mapping.keys()) + list(finger_mapping.values())
        self.add_widget_auto_serialized_fields(filter_attr=ignore_attrs)
        # Activation / Name Lines
        for activation_attr, name_attr in finger_mapping.items():
            # Create and Add Layout
            _layout = ui_qt.QtWidgets.QHBoxLayout()
            _layout.setContentsMargins(0, 0, 0, 5)  # L-T-R-B
            self.content_layout.addLayout(_layout)
            # Create Activation Checkbox and Name Textfield
            _checkbox = self.add_module_attr_widget_checkbox(attr_name=activation_attr, layout=_layout)
            _textfield = self.add_module_attr_widget_text_field(
                attr_name=name_attr, layout=_layout, nice_name=textfield_names
            )
            # Create Enabled Connection
            _checkbox.stateChanged.connect(_textfield.setEnabled)

        self.add_widget_action_buttons()


# -------------------------------------------------- Project ---------------------------------------------------
class AttrWidgetProject(AttrWidget):
    def __init__(self, parent=None, project=None, refresh_parent_func=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Basic Variables
        self.project = project
        self.project_name_field = None
        self.project_prefix_field = None
        self.refresh_parent_func = None

        if refresh_parent_func:
            self.set_refresh_parent_func(refresh_parent_func)

        self.add_widget_project_header()

    # Parameter Widgets ----------------------------------------------------------------------------------------
    def add_widget_project_header(self):
        """
        Adds the header for controlling a project. With Icon, Name and modify button.
        """
        # Project Header (Icon, Name, Buttons)
        _layout = ui_qt.QtWidgets.QHBoxLayout()
        _layout.setContentsMargins(0, 0, 0, 5)  # L-T-R-B
        _layout.setAlignment(ui_qt.QtLib.AlignmentFlag.AlignTop)

        # Icon
        icon = ui_qt.QtGui.QIcon(self.project.icon)
        icon_label = ui_qt.QtWidgets.QLabel()
        icon_label.setPixmap(icon.pixmap(32, 32))
        label_tooltip = "Rig Project"
        icon_label.setToolTip(label_tooltip)
        _layout.addWidget(icon_label)

        # Name (User Custom)
        name = self.project.get_name()
        self.project_name_field = ui_qt_utils.ConfirmableQLineEdit()
        self.project_name_field.setFixedHeight(35)
        if name:
            self.project_name_field.setText(name)
        self.project_name_field.editingFinished.connect(self.set_project_name)
        _layout.addWidget(self.project_name_field)

        # Edit Button
        edit_project_btn = ui_qt.QtWidgets.QPushButton()
        edit_project_btn.setIcon(ui_qt.QtGui.QIcon(ui_res_lib.Icon.rigger_dict))
        edit_project_btn.setToolTip("Edit Raw Data")
        edit_project_btn.clicked.connect(self.on_button_edit_project_clicked)
        _layout.addWidget(edit_project_btn)
        self.content_layout.addLayout(_layout)

    def on_button_edit_project_clicked(self, skip_modules=True, *args):
        """
        Shows a text-editor window with the project converted to a dictionary (raw data)
        If the user applies the changes, and they are considered valid, the module is updated with it.
        Args:
            skip_modules (bool, optional): If active, the "modules" key will be ignored.
            *args: Variable-length argument list. - Here to avoid issues with the "skip_modules" argument.
        """
        project_name = self.project.get_name()
        param_win = ui_input_window_text.InputWindowText(
            parent=self,
            message=f'Editing Raw Data for the Project "{project_name}"',
            window_title=f'Raw data for "{project_name}"',
            image=ui_res_lib.Icon.rigger_dict,
            window_icon=ui_res_lib.Icon.library_parameters,
            image_scale_pct=10,
            is_python_code=True,
        )
        param_win.set_confirm_button_text("Apply")
        project_raw_data = self.project.get_project_as_dict()
        if "modules" in project_raw_data and skip_modules:
            project_raw_data.pop("modules")
        formatted_dict = core_iter.dict_as_formatted_str(project_raw_data, one_key_per_line=True)
        param_win.set_text_field_text(formatted_dict)
        confirm_button_func = partial(self.update_project_from_raw_data, param_win.get_text_field_text, self.project)
        param_win.confirm_button.clicked.connect(confirm_button_func)
        param_win.show()

    # Setters --------------------------------------------------------------------------------------------------
    def set_project_name(self):
        new_name = self.project_name_field.text() or ""
        self.project.set_name(new_name)
        self.call_parent_refresh()

    def update_project_from_raw_data(self, data_getter, project):
        """
        Updates a project description using raw string data.
        Used with "on_button_edit_project_clicked" to update a project from raw data.
        Args:
            data_getter (callable): A function used to retrieve the data string. e.g. Get a string from a textfield.
            project (RigProject): A rig project object to be updated using the provided data.
        """
        data = data_getter()
        try:
            _data_as_dict = ast.literal_eval(data)
            project.read_data_from_dict(module_dict=_data_as_dict, clear_modules=False)
            self.refresh_current_widgets()
            self.call_parent_refresh()
        except Exception as e:
            raise Exception(f'Unable to set project attributes from provided raw data. Issue: "{e}".')

    def refresh_current_widgets(self):
        """
        Refreshes available widgets. For example, text-fields, so they display the correct data.
        """
        if self.project_name_field:
            _name = self.project.get_name()
            if _name:
                self.project_name_field.setText(_name)


if __name__ == "__main__":
    print('Run it from "__init__.py".')
