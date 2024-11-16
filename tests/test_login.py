from base.webdriver_listener import WebDriverWrapper    # IMPORTING WEBDRIVER WRAPPER CLASS
from selenium.webdriver.common.by import By     # FOR FINIDING ELEMENTS
from page.homepage_before_login import HomePage_before_login
from page.loginpage import LoginPage
from page.homepageafterlogin import HomePageAfterLogin

"""Test case related to Login"""

class TestLogin(WebDriverWrapper):

    def test_valid_login(self):
        homepage = HomePage_before_login(self.driver)
        loginpage = LoginPage(self.driver)
        homepage_after_login = HomePageAfterLogin(self.driver)
        homepage.click_on_log_in_link()
        loginpage.enter_email_password_and_click_login("demo@shubham.com","demo@shubham.com")
        homepage_after_login.verify_user_is_login("demo@shubham.com")


    def test_invalid_login(self):
        homepage = HomePage_before_login(self.driver)
        loginpage = LoginPage(self.driver)
        homepage.click_on_log_in_link()
        loginpage.enter_email_password_and_click_login("invalid@shubham.com", "invalid@shubham.com")
        loginpage.verify_invalid_login_error_message()


    def test_login_and_logout(self):
        homepage = HomePage_before_login(self.driver)
        loginpage = LoginPage(self.driver)
        homepage.click_on_log_in_link()
        loginpage.enter_email_password_and_click_login("demo@shubham.com", "demo@shubham.com")
        self.driver.find_element(By.XPATH, "//a[text()='Log out']").is_displayed()
        self.driver.find_element(By.XPATH, "//a[text()='Log out']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Log in']").is_displayed()


