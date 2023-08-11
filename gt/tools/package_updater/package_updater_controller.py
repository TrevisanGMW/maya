"""
Curve Library Controller

This module contains the CurveLibraryController class responsible for managing interactions between the
CurveLibraryModel and the user interface.
"""
from gt.utils.iterable_utils import get_next_dict_item
from gt.utils.prefs_utils import PackageCache
from gt.ui import resource_library
import threading
import logging

# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class PackageUpdaterController:
    def __init__(self, model, view):
        """
        Initialize the PackageUpdaterController object.

        Args:
            model: The CurveLibraryModel object used for data manipulation.
            view: The view object to interact with the user interface.
        """
        self.model = model
        self.view = view
        self.view.controller = self
        # Clear View
        self.set_view_to_waiting()
        # Connections
        self.view.interval_btn.clicked.connect(self.update_view_interval_button)
        self.view.refresh_btn.clicked.connect(self.refresh_updater_data_threaded_maya)
        self.view.auto_check_btn.clicked.connect(self.cycle_auto_check)
        self.view.update_btn.clicked.connect(self.update_package_threaded_maya)
        # Initial Checks:
        if not model.has_requested_online_data():
            self.refresh_updater_data_threaded_maya()

    def set_view_to_waiting(self):
        """ Clear view values showing that it's waiting for a refresh """
        self.view.change_update_button_state(state=False)
        self.view.update_installed_version(version=f'v?.?.?')
        self.view.update_latest_release(version=f'v?.?.?')
        self.view.update_status(status="Unknown")
        self.view.update_web_response(response="Requesting...")
        self.view.clear_changelog_box()

    def refresh_view_values(self):
        """ Updates the view with values found in the model """
        auto_check = self.model.get_auto_check()
        self.view.update_auto_check_status_btn(is_active=auto_check)
        interval_days = self.model.get_interval_days()
        self.update_view_interval_button(new_interval=interval_days, cycle=False)
        if self.model.is_update_needed():
            self.view.change_update_button_state(state=True)
        else:
            self.view.change_update_button_state(state=False)
        installed_version = self.model.get_installed_version()
        self.view.update_installed_version(version=f'v{installed_version}')
        latest_github_version = self.model.get_latest_github_version()
        self.view.update_latest_release(version=f'v{latest_github_version}')
        status_description = self.model.get_status_description()
        self.view.update_status(status=status_description)
        web_response = self.model.get_web_response_reason()
        self.view.update_web_response(response=str(web_response))
        self.update_auto_check()
        self.view.change_update_button_state(state=self.model.is_update_needed())
        self.populate_changelog_box()

    def populate_changelog_box(self):
        """ Populates the changelog box with changelog data """
        self.view.clear_changelog_box()
        changelog = self.model.get_releases_changelog()
        for tag_name, description in changelog.items():
            self.view.add_text_to_changelog(text=tag_name,
                                            text_color_hex=resource_library.Color.Hex.white)
            self.view.add_text_to_changelog(text=description.replace("\r\n", "\n"),
                                            text_color_hex=resource_library.Color.Hex.grey_lighter)

    def update_view_interval_button(self, new_interval=None, cycle=True):
        """
        Updates the interval button text.
        Args:
            new_interval (int, optional): If provided, this value will be used as the new interval.
                                          Note: It will be converted to string and "days" will be added to the end.
            cycle (bool, optional): If active, it will cycle through a pre-determined list of available periods.
        """
        current_interval = new_interval
        if not new_interval:
            current_interval = self.model.get_interval_days()

        interval_list = {1: "1 day",
                         5: "5 days",
                         15: "15 days",
                         30: "1 month",
                         91: '3 months',
                         182: '6 months',
                         365: '1 year'}

        if cycle and current_interval in interval_list:
            current_interval = get_next_dict_item(interval_list, current_interval, cycle=True)[0]
        elif cycle:
            current_interval = 1

        # Determine Button String
        if current_interval in interval_list:
            time_period = interval_list.get(current_interval)
        else:
            time_period = f'{current_interval} days'
        self.view.update_interval_button(time_period=time_period)
        self.model.set_interval_days(interval_days=current_interval)
        self.model.save_preferences()

    def update_auto_check(self):
        """
        Update the auto check to the value stored in the model
        """
        state = self.model.get_auto_check()
        self.view.update_auto_check_status_btn(is_active=state)
        self.view.change_interval_button_state(state=state)

    def cycle_auto_check(self):
        """
        Update the auto check button by cycling through Activated/Deactivated.
        Also updates to enabled state of the interval button as an interval is only necessary when activated.
        """
        state = self.model.get_auto_check()
        self.view.update_auto_check_status_btn(is_active=not state)
        self.view.change_interval_button_state(state=not state)
        self.model.set_auto_check(auto_check=not state)
        self.model.save_preferences()

    def update_package_threaded_maya(self):
        """
        Updates package to the latest version found on GitHub
        """
        cache = PackageCache()
        kwargs = {"cache": cache, "force_update": False}

        def _maya_update_latest_package():
            """ Internal function used to update package using threads in Maya """
            from maya import utils
            utils.executeDeferred(self.model.update_package, **kwargs)

        try:
            thread = threading.Thread(None, target=_maya_update_latest_package)
            thread.start()
            cache.clear_cache()
        except Exception as e:
            logger.warning(f'Unable to update package. Issue: {e}')
        finally:
            cache.clear_cache()

    def refresh_updater_data(self):
        """
        Checks for updates and refreshes the updater UI to reflect retrieved data
        """
        self.model.check_for_updates()
        self.refresh_view_values()

    def refresh_updater_data_threaded_maya(self):
        """
        Threaded version of the function "refresh_updater_data" maya to run in Maya
        Checks for updates and refreshes the updater UI to reflect retrieved data
        """
        def _maya_retrieve_update_data():
            """ Internal function used to check for updates using threads in Maya """
            from maya import utils
            utils.executeDeferred(self.refresh_updater_data)
        try:
            thread = threading.Thread(None, target=_maya_retrieve_update_data)
            thread.start()
        except Exception as e:
            logger.warning(f'Unable to refresh updater. Issue: {e}')


if __name__ == "__main__":
    print('Run it from "__init__.py".')

