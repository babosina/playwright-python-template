# use a Factory pattern

from playwright.sync_api import Page

from python_project.helper.utils import log_message, LogLevel, take_screenshot
from python_project.page_objects.base_page import BasePage
from python_project.page_objects.main_page import MainPage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_field = self.page.locator("#username")
        self.password_field = self.page.locator("#password")
        self.login_button = self.page.get_by_role("button", name="Login")
        self.alert_message = self.page.locator("#flash")

    def login(self, username: str, password: str):
        log_message(self.logger, "Perform Login", level=LogLevel.INFO)
        self.type_text(self.username_field, username)
        self.type_text(self.password_field, password)
        self.click_element(self.login_button)

        if self.login_button.is_visible():
            log_message(self.logger, "Login Failed", LogLevel.ERROR)
            take_screenshot(self.page, "login_failed")
            return None

        return MainPage(self.page)

    def get_alert_message(self, error_message: str):
        return self.alert_message.locator(f"//div/*[contains(text(), '{error_message}')]")
