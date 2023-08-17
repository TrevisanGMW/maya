"""
Curve Library Controller

This module contains the CurveLibraryController class responsible for managing interactions between the
CurveLibraryModel and the user interface.
"""
from PySide2.QtWidgets import QInputDialog
import logging

# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CurveLibraryController:
    def __init__(self, model, view):
        """
        Initialize the CurveLibraryController object.

        Args:
            model: The CurveLibraryModel object used for data manipulation.
            view: The view object to interact with the user interface.
        """
        self.model = model
        self.view = view
        self.view.controller = self
        # Connections
        self.view.build_button.clicked.connect(self.build_view_selected_curve)
        self.view.item_list.itemSelectionChanged.connect(self.on_item_selection_changed)
        self.view.search_edit.textChanged.connect(self.filter_list)
        self.populate_curve_library()
        self.view.show()

    def on_item_selection_changed(self):
        """
        Update the preview image in the view when the selected item in the list changes.
        """
        selected_item = self.view.item_list.currentItem().text()
        new_preview_image = self.model.get_preview_image(object_name=selected_item)
        if new_preview_image:
            self.view.update_preview_image(new_image_path=new_preview_image)

    def filter_list(self):
        """
        Filter the curve library list based on the search text entered by the user.
        """
        search_text = self.view.search_edit.text().lower()
        self.view.item_list.clear()
        curve_names = self.model.get_base_curve_names()
        filtered_items = [item for item in curve_names if search_text in item.lower()]
        self.view.item_list.addItems(filtered_items)
        self.view.item_list.setCurrentRow(0)  # Select index 0
        if not filtered_items:
            self.view.update_preview_image()

    def build_view_selected_curve(self):
        """
        Build the selected curve from the curve library in the model.
        """
        selected_curve_name = self.view.item_list.currentItem().text()
        self.model.build_curve(curve_name=selected_curve_name)

    def add_item_view(self):
        """
        Prompt the user for an item name and add it to the model.
        """
        item_text, ok = QInputDialog.getText(self.view, "Enter item name", "Item name:")
        if ok:
            self.model.add_item(item_text)
            self.populate_curve_library()

    def remove_item_view(self):
        """
        Remove the selected item from the model based on the user's selection in the view.
        """
        selected_item = self.view.item_list.currentRow()
        if selected_item >= 0:
            self.model.remove_item(selected_item)
            self.populate_curve_library()

    def populate_curve_library(self):
        """
        Update the view with the current list of items from the model.
        """
        self.view.update_view_library(self.model.get_base_curve_names())
        self.view.item_list.setCurrentRow(0)  # Select index 0


if __name__ == "__main__":
    print('Run it from "__init__.py".')
