from base import webdriver_listener

class login_page(webdriver_listener):
    def __init__(self, driver):
        super().__init__(driver)

    # def open_login_page(self):