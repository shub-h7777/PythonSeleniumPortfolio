from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self,driver):
        self.driver=driver

    email = "Email"      #id
    password = "Password"        #id
    login_button = "//input[@value='Log in']"     #xpath
    invalid_login_error_message_common =  "//div[@class='validation-summary-errors']/span"     #xpath
    invalid_email_error_message = "//li[contains(text(), 'No customer account found')]"     #xpath
    invalid_password_error_message = "//li[contains(text(),'The credentials provided are incorrect')]"      #xpath
    logout = "//a[text()='Log out']"
    login = "//a[text()='Log in']"

    def enter_email_password_and_click_login(self, email,password):
        self.driver.find_element(By.ID, self.email).send_keys(email)
        self.driver.find_element(By.ID, self.password).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_button).click()

    def verify_invalid_login_error_message(self, error_message):
        error_message = self.driver.find_element(By.XPATH, self.invalid_login_error_message_common).text
        assert error_message == error_message

    def logout_and_verify_login_link_is_visible(self):
        self.driver.find_element(By.XPATH, self.logout).is_displayed()
        self.driver.find_element(By.XPATH, self.logout).click()
        self.driver.find_element(By.XPATH, self.login).is_displayed()
        
        









