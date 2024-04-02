import time

import pytest
from assertpy import assert_that   # FOR VALIDATION
from selenium.webdriver.common.by import By     # FOR FINIDING ELEMENTS

"""USING LOCAL REPO RESOURCCE"""

from base.webdriver_listener import WebDriverWrapper    # IMPORTING WEBDRIVER WRAPPER CLASS
from utilities import read_utils

"""Test case related to Login"""

class TestLogin(WebDriverWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.XPATH,"//a[text()='Log in']").click()
        self.driver.find_element(By.ID, "Email").send_keys("demo@shubham.com")
        self.driver.find_element(By.ID, "Password").send_keys("demo@shubham.com")
        self.driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Log out']").is_displayed()

    def test_invalid_login(self):
        self.driver.find_element(By.XPATH, "//a[text()='Log in']").click()
        self.driver.find_element(By.ID, "Email").send_keys("invalid@shubham.com")
        self.driver.find_element(By.ID, "Password").send_keys("invalid@shubham.com")
        self.driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        error_message=self.driver.find_element(By.XPATH, "//div[@class='validation-summary-errors']/span").text
        assert error_message == 'Login was unsuccessful. Please correct the errors and try again.'

    def test_login_and_logout(self):
        self.driver.find_element(By.XPATH, "//a[text()='Log in']").click()
        self.driver.find_element(By.ID, "Email").send_keys("demo@shubham.com")
        self.driver.find_element(By.ID, "Password").send_keys("demo@shubham.com")
        self.driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Log out']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Log in']").is_displayed()