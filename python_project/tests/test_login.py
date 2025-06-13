# open browser
# enter username and password
# click login button
# check if login is successful
# how to check if the login is successful?
# verify negative test cases

from python_project.helper.config import VALID_CREDENTIALS


# invalid password, valid username

# valid username, invalid password

# missing username, valid password

# missing password, valid username

def test_successful_login(setup_load_page):
    login_page = setup_load_page
    login_page.login(VALID_CREDENTIALS["username"], VALID_CREDENTIALS["password"])
