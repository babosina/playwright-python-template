import pytest

from venv import logger
from pytest_playwright.pytest_playwright import playwright

from python_project.helper.config import URL
from python_project.helper.utils import log_message, LogLevel
from python_project.page_objects.login_page import LoginPage


@pytest.fixture
def setup_playwright(playwright, request):
    headed = request.config.getoption("--headless", default=False)
    browser = playwright.chromium.launch(headless=not headed)
    page = browser.new_page()
    try:
        yield page
    finally:
        log_message(logger, "Closing the browser", LogLevel.INFO)
        browser.close()


@pytest.fixture
def setup_load_page(setup_playwright):
    login_page = LoginPage(setup_playwright)
    login_page.navigate_to(URL)
    log_message(logger, f"Navigating to URL {URL}", LogLevel.INFO)
    yield login_page
