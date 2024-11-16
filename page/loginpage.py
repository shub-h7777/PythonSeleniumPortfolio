from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver=driver

    email_id = "Email"
    password_id = "Password"
    login_button_Xpath = "//input[@value='Log in']"
    invalid_login_error_message =  "//div[@class='validation-summary-errors']/span"

    def enter_email_password_and_click_login(self, email,password):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)
        self.driver.find_element(By.ID, self.password_id).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_button_Xpath).click()

    def verify_invalid_login_error_message(self):
        error_message = self.driver.find_element(By.XPATH, self.invalid_login_error_message).text
        assert error_message == 'Login was unsuccessful. Please correct the errors and try again.'








