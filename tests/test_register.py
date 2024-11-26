import time

import pytest
from base.webdriver_listener import WebDriverWrapper
from utilities import data_source
from page.registerpage import RegisterPage
from page.homepage_before_login import HomePage_before_login

class TestRegister(WebDriverWrapper):

    @pytest.mark.parametrize(
        "gender, firstname, lastname, email, password, confirm_password,firstname_error, lastname_error, email_error, password_error, confirm_password_error",
        data_source.test_invalid2_register_data
    )
    def test_invalid_register(self, gender, firstname, lastname, email, password, confirm_password, firstname_error, lastname_error, email_error, password_error, confirm_password_error):
        register_page = RegisterPage(self.driver)
        homepage = HomePage_before_login(self.driver)
        homepage.click_on_register_link()
        register_page.register_new_account(gender, firstname, lastname, email, password, confirm_password)
        register_page.verify_error_on_register_screen(firstname_error, lastname_error, email_error, password_error,confirm_password_error)