from base.webdriver_listener import WebDriverWrapper    # IMPORTING WEBDRIVER WRAPPER CLASS
from page.homepage_before_login import HomePage_before_login
from page.loginpage import LoginPage
from page.homepageafterlogin import HomePageAfterLogin
import pytest
from utilities import data_source

"""Test case related to Login"""

class TestLogin(WebDriverWrapper):

    """
    @pytest.mark.parametrize will help to run same method but will different inputs
    """
    @pytest.mark.parametrize(
        "username,password",data_source.test_valid_login_data
    )
    def test_valid_login(self, username, password):
        homepage = HomePage_before_login(self.driver)
        loginpage = LoginPage(self.driver)
        homepage_after_login = HomePageAfterLogin(self.driver)
        homepage.click_on_log_in_link()
        loginpage.enter_email_password_and_click_login(username,password)
        homepage_after_login.verify_user_is_login(username)

    @pytest.mark.parametrize(
        "username,password, error_message", data_source.test_invalid_login_data
    )
    def test_invalid_login(self, username, password, error_message):
        homepage = HomePage_before_login(self.driver)
        loginpage = LoginPage(self.driver)
        homepage.click_on_log_in_link()
        loginpage.enter_email_password_and_click_login(username, password)
        loginpage.verify_invalid_login_error_message(error_message)

    @pytest.mark.parametrize(
        "username,password", data_source.test_valid_login_data
    )
    def test_login_and_logout(self, username, password):
        homepage = HomePage_before_login(self.driver)
        loginpage = LoginPage(self.driver)
        homepage.click_on_log_in_link()
        loginpage.enter_email_password_and_click_login(username, password)
        loginpage.logout_and_verify_login_link_is_visible()


