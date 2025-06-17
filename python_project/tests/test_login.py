import pytest

from python_project.helper.config import VALID_CREDENTIALS


def test_successful_login(setup_load_page, validation):
    login_page = setup_load_page
    login_page.login(VALID_CREDENTIALS["username"], VALID_CREDENTIALS["password"])
    validation.validate_user_logged_in()


@pytest.mark.parametrize("username, password, error_message", [
    ("wrong_username", "SuperSecretPassword!", "Your username is invalid!1234"),
    ("practice", "wrong_password", "Your password is invalid!"),
    ("", "SuperSecretPassword!", "Your username is invalid!"),
    ("practice", "", "Your password is invalid!")
])
def test_invalid_login(setup_load_page, validation, username, password, error_message):
    login_page = setup_load_page
    login_page.login(username, password)
    validation.validate_login_failed(expected_error_message=error_message)
