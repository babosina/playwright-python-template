from python_project.helper.config import VALID_CREDENTIALS


# invalid password, valid username

# valid username, invalid password

# missing username, valid password

# missing password, valid username

def test_successful_login(setup_load_page, validation):
    login_page = setup_load_page
    login_page.login(VALID_CREDENTIALS["username"], VALID_CREDENTIALS["password"])
    validation.validate_user_logged_in()
