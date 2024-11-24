from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver=driver

    email_id = "Email"      #id
    password_id = "Password"        #id
    login_button_Xpath = "//input[@value='Log in']"     #xpath
    invalid_login_error_message_common =  "//div[@class='validation-summary-errors']/span"     #xpath
    invalid_email_error_message = "//li[contains(text(), 'No customer account found')]"
    invalid_password_error_message = "//li[contains(text(),'The credentials provided are incorrect')]"
    logout = "//a[text()='Log out']"
    login = "//a[text()='Log in']"

    def enter_email_password_and_click_login(self, email,password):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)
        self.driver.find_element(By.ID, self.password_id).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_button_Xpath).click()

    def verify_invalid_login_error_message(self, error_message):
        error_message = self.driver.find_element(By.XPATH, self.invalid_login_error_message_common).text
        assert error_message == error_message

    def logout_and_verify_login_link_is_visible(self):
        self.driver.find_element(By.XPATH, self.logout).is_displayed()
        self.driver.find_element(By.XPATH, self.logout).click()
        self.driver.find_element(By.XPATH, self.login).is_displayed()










