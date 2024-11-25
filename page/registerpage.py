from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from enum import Enum
from assertpy import assert_that

class GenderRadioButton(Enum):
    male = "male"
    female = "female"
class RegisterPage:

    def __init__(self,driver):
        self.driver=driver

    email = "Email"      #id
    password = "Password"        #id
    male_radio_button = "gender-male"       #id
    female_radio_button = "gender-female"    #id
    firstname_textbox = "FirstName"         #id
    lastname_textbox = "LastName"           #id
    confirm_Password_textbox = "ConfirmPassword"    #id
    register_button = "register-button"     #id
    registration_completed_text = "//div[contains(text(),'Your registration completed')]"   #Xpath

    first_name_validation = "//span[@for='FirstName']"  #Xpath
    last_name_validation = "//span[@for='LastName']"    #Xpath
    email_validation = "//span[@for='Email']"           #Xpath
    password_validation = "//span[@for='Password']"     #Xpath
    confirm_password_validation = "//span[@for='ConfirmPassword']"  #Xpath



    def register_new_account(self, gender, firstname, lastname, email, password, confirm_password):
        if gender == GenderRadioButton.male:
            self.driver.find_element(By.ID, self.male_radio_button).click()
        elif gender == GenderRadioButton.female:
            self.driver.find_element(By.ID, self.female_radio_button).click()
        self.driver.find_element(By.ID, self.firstname_textbox).send_keys(firstname)
        self.driver.find_element(By.ID, self.lastname_textbox).send_keys(lastname)
        self.driver.find_element(By.ID, self.email).send_keys(email)
        self.driver.find_element(By.ID, self.password).send_keys(password)
        self.driver.find_element(By.ID, self.confirm_Password_textbox).send_keys(confirm_password)
        self.driver.find_element(By.ID, self.register_button).click()

    def verify_error_on_register_screen(self, firstname_error, lastname_error, email_error, password_error, confirm_password_error):
        try:
            element = self.driver.find_element(By.XPATH, self.first_name_validation).text
            assert_that(element).is_equal_to(firstname_error)
        except NoSuchElementException:
            element = None
        # assert_that(self.driver.find_element(By.XPATH, self.last_name_validation).text).is_equal_to(lastname_error)
        # assert_that(self.driver.find_element(By.XPATH, self.email_validation).text).is_equal_to(email_error)
        # assert_that(self.driver.find_element(By.XPATH, self.password_validation).text).is_equal_to(password_error)
        # assert_that(self.driver.find_element(By.XPATH, self.confirm_password_validation).text).is_equal_to(confirm_password_error)


