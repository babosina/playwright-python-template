import pytest

from venv import logger
from pytest_playwright.pytest_playwright import playwright

from python_project.helper.config import URL
from python_project.helper.utils import log_message, LogLevel
from python_project.helper.validation import AppValidations
from python_project.page_objects.login_page import LoginPage
from python_project.page_objects.main_page import MainPage


@pytest.fixture
def setup_playwright(playwright, request):
    headed = request.config.getoption("--headed", default=False)
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

@pytest.fixture
def get_all_pages(setup_playwright):
    login_page = LoginPage(setup_playwright)
    main_page = MainPage(setup_playwright)
    yield login_page, main_page

@pytest.fixture
def validation(get_all_pages):
    yield AppValidations(get_all_pages)