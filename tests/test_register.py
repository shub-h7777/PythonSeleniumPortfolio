import time
import pytest
from base.webdriver_listener import WebDriverWrapper
from utilities import data_source
from page.registerpage import RegisterPage
from page.homepage_before_login import HomePage_before_login
import random
from page.homepageafterlogin import HomePageAfterLogin

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

    @pytest.mark.parametrize(
        "gender, firstname, lastname, password, confirm_password",
        data_source.test_valid_register_data
    )
    def test_valid_register(self, gender, firstname, lastname, password, confirm_password):

        #create ranndom email
        random_int = random.randint(1, 10000000)
        email = "demo"+str(random_int)+"@demo.com"

        #create object
        register_page = RegisterPage(self.driver)
        homepage = HomePage_before_login(self.driver)
        homepage_after_login = HomePageAfterLogin(self.driver)

        homepage.click_on_register_link()
        register_page.register_new_account(gender, firstname, lastname, email, password, confirm_password)
        register_page.verify_registration_success_message()
        homepage_after_login.verify_username(email)