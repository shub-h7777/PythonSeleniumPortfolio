from selenium.webdriver.common.by import By


class HomePage_before_login:

    def __init__(self, driver):
        self.driver = driver

    log_in = "//a[text()='Log in']"         #Xpath
    register = "//a[text()='Register']"     #Xpath


    def click_on_log_in_link(self):
        self.driver.find_element(By.XPATH, self.log_in).click()

    def click_on_register_link(self):
        self.driver.find_element(By.XPATH, self.register).click()
