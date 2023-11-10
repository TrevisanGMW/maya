"""
Auto Rigger Attr Widgets
"""
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QHBoxLayout, QGridLayout, \
    QSizePolicy, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView
import gt.ui.resource_library as resource_library
from PySide2.QtGui import QIcon, QPixmap


class ModuleAttrWidget(QWidget):
    PROXY_ROLE = QtCore.Qt.UserRole
    PARENT_ROLE = QtCore.Qt.UserRole + 1

    def __init__(self, parent=None, module=None, project=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.project = project
        self.module = module
        self.known_proxy = {}

        # Module Header (Icon, Type, Name, Buttons) ----------------------------------------------
        header_layout = QHBoxLayout()
        header_layout.setAlignment(Qt.AlignTop)

        # Icon
        icon = QIcon(module.icon)
        icon_label = QLabel()
        icon_label.setPixmap(icon.pixmap(32, 32))
        header_layout.addWidget(icon_label)

        # Type (Module Class)
        module_type = module.get_module_class_name(remove_module_prefix=True)
        header_layout.addWidget(QLabel(f"{module_type}"))

        # Name (User Custom)
        name = module.get_name()
        self.name_text_field = QLineEdit()
        if name:
            self.name_text_field.setText(name)
        self.name_text_field.textChanged.connect(self.set_module_name)
        header_layout.addWidget(self.name_text_field)

        # Delete Button
        self.delete_btn = QPushButton()
        self.delete_btn.setIcon(QIcon(resource_library.Icon.dev_trash))
        header_layout.addWidget(self.delete_btn)

        # Help Button
        self.help_btn = QPushButton()
        self.help_btn.setIcon(QIcon(resource_library.Icon.root_help))
        header_layout.addWidget(self.help_btn)

        # Other Options --------------------------------------------------------------------------
        proxy_table = QVBoxLayout()

        attr_layout = QGridLayout()
        attr_layout.setAlignment(Qt.AlignTop)

        prefix_label = QLabel("Prefix:")
        self.prefix_text_field = QLineEdit()
        attr_layout.addWidget(prefix_label, 0, 0)
        attr_layout.addWidget(self.prefix_text_field, 0, 1)

        parent_label = QLabel("Parent:")
        self.parent_text_field = QLineEdit()
        self.parent_btn = QPushButton("Get Selection")
        attr_layout.addWidget(parent_label, 1, 0)
        attr_layout.addWidget(self.parent_text_field, 1, 1)
        attr_layout.addWidget(self.parent_btn, 1, 2)

        self.table_wdg = QTableWidget()
        self.table_wdg.setRowCount(0)
        self.table_wdg.setColumnCount(4)  # Icon, Name, Parent, Get, More
        self.table_wdg.setHorizontalHeaderLabels(["", "Name", "Parent", ""])
        header_view = self.table_wdg.horizontalHeader()
        header_view.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header_view.setSectionResizeMode(1, QHeaderView.Interactive)
        header_view.setSectionResizeMode(2, QHeaderView.Stretch)
        header_view.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        proxy_table.addWidget(self.table_wdg)
        self.table_wdg.setColumnWidth(1, 110)
        self.refresh_table()

        # Create Layout
        scroll_content_layout = QVBoxLayout(self)
        scroll_content_layout.setAlignment(Qt.AlignTop)
        scroll_content_layout.addLayout(header_layout)
        scroll_content_layout.addLayout(attr_layout)
        scroll_content_layout.addLayout(proxy_table)

    def refresh_table(self):
        for row, proxy in enumerate(self.module.get_proxies()):
            self.table_wdg.insertRow(row)
            # Icon ---------------------------------------------------------------------------
            self.insert_item(row=row,
                             column=0,
                             icon_path=resource_library.Icon.dev_git_fork,
                             editable=False,
                             centered=True)

            # Name ---------------------------------------------------------------------------
            self.insert_item(row=row,
                             column=1,
                             text=proxy.get_name(),
                             data_object=proxy)

            # Parent Combobox ----------------------------------------------------------------
            _row = row
            combo_box = self.create_parent_combobox()
            combo_func = lambda state, row=_row, col=2: self.on_parent_combo_box_changed(row, col)
            combo_box.currentIndexChanged.connect(combo_func)

            # Proxy Setup --------------------------------------------------------------------
            self.insert_item(row=row,
                             column=2,
                             data_object=proxy)

            # Add to Table -------------------------------------------------------------------
            self.table_wdg.setCellWidget(row, 2, combo_box)

    def insert_item(self, row, column, text=None, data_object=None,
                    icon_path='', editable=True, centered=True):
        item = QtWidgets.QTableWidgetItem(text)
        self.set_table_item_proxy_object(item, data_object)

        if icon_path != '':
            icon = QIcon(icon_path)
            icon_label = QLabel()
            icon_label.setPixmap(icon.pixmap(32, 32))
            icon_label.setAlignment(Qt.AlignCenter)
            self.table_wdg.setCellWidget(row, column, icon_label)
            return

        if centered:
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        if not editable:
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)

        self.table_wdg.setItem(row, column, item)

    def on_parent_combo_box_changed(self, row, col):
        _name_cell = self.table_wdg.item(row, 1)
        _proxy = self.get_table_item_proxy_object(_name_cell)
        _combo_box = self.table_wdg.cellWidget(row, col)
        _parent_proxy = _combo_box.itemData(_combo_box.currentIndex())
        _proxy.set_parent_uuid(_parent_proxy.get_uuid())

    @staticmethod
    def set_item_text(item, text):
        item.setText(text)

    @staticmethod
    def get_item_text(item):
        return item.text()

    def set_table_item_proxy_object(self, item, proxy):
        item.setData(self.PROXY_ROLE, proxy)

    def get_table_item_proxy_object(self, item):
        return item.data(self.PROXY_ROLE)

    def refresh_known_proxy_dict(self):
        for module in self.project.get_modules():
            for proxy in module.get_proxies():
                self.known_proxy[proxy.get_uuid()] = (proxy, module)

    def create_parent_combobox(self):
        self.refresh_known_proxy_dict()
        combo_box = QComboBox()

        for key, (proxy, module) in self.known_proxy.items():
            description = f'{str(proxy.get_name())}'
            module_name = module.get_name()
            if module_name:
                description += f' : {str(module_name)}'
            description += f' ({str(key)})'
            combo_box.addItem(description, proxy)

        # combo_box.currentIndexChanged.connect(self.on_combo_box_changed)
        # self.set_combobox_proxy_object(combo_box, proxy)
        # combo_box.addItems(self.get_formatted_known_proxy_list())

        return combo_box

    def set_module_name(self):
        new_name = self.name_text_field.text() or ""
        self.module.set_name(new_name)



class ProjectAttrWidget(QWidget):
    def __init__(self, parent=None, project=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.project = project

        # Project Header (Icon, Type, Name, Buttons) ----------------------------------------------
        header_layout = QHBoxLayout()

        # Icon
        icon = QIcon(project.icon)
        icon_label = QLabel()
        icon_label.setPixmap(icon.pixmap(32, 32))
        header_layout.addWidget(icon_label)

        # Type (Project)
        header_layout.addWidget(QLabel("RigProject"))
        header_layout.setAlignment(Qt.AlignTop)

        # Name (User Custom)
        name = project.get_name()
        self.name_text_field = QLineEdit()
        if name:
            self.name_text_field.setText(name)
        self.name_text_field.textChanged.connect(self.set_module_name)
        header_layout.addWidget(self.name_text_field)

        # Help Button
        self.help_btn = QPushButton()
        self.help_btn.setIcon(QIcon(resource_library.Icon.root_help))
        header_layout.addWidget(self.help_btn)

        # Create Layout
        scroll_content_layout = QVBoxLayout(self)
        scroll_content_layout.addLayout(header_layout)

    def set_module_name(self):
        new_name = self.name_text_field.text() or ""
        self.project.set_name(new_name)


if __name__ == "__main__":
    print('Run it from "__init__.py".')
