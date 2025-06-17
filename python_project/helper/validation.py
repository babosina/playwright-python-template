from playwright.sync_api import expect

from python_project.helper.utils import log_message, LogLevel, take_screenshot
from python_project.page_objects.base_page import BasePage


class AppValidations(BasePage):
    def __init__(self, get_all_pages):
        self.login_page, self.main_page = get_all_pages
        super().__init__(self.login_page)

    def validate_user_logged_in(self):
        login_button = self.login_page.login_button
        try:
            expect(login_button).not_to_be_visible(), "failed to login"
        except Exception as e:
            log_message(self.logger, "Login failed", LogLevel.ERROR)
            take_screenshot(self.page, "login_failed")
            raise Exception("Login failed, login button still visible") from e

    def validate_login_failed(self, expected_error_message: str):
        alert_message = self.login_page.alert_message
        login_button = self.login_page.login_button
        try:
            expect(alert_message).to_be_visible(), "successful login"
            expect(alert_message).to_have_text(expected_error_message)
            expect(login_button).to_be_visible(), "Login button should be hidden, but is visible"
        except Exception as e:
            log_message(self.logger, "Login button should be hidden, but is visible", LogLevel.CRITICAL)
            take_screenshot(self.page, "login_successful")
            raise Exception("Login successful, login button still visible") from e
