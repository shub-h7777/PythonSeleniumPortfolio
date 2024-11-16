import pytest
from selenium import webdriver
from utilities import read_utils  # from project directory to get the read the browser config
from webdriver_manager.chrome import ChromeDriverManager

"""Browser configuration"""


class WebDriverWrapper:
    driver = None

    """ Fixture is same as Setup and Teardown in the N-unit framework it is used for launching and closing any web app """

    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        browser_name = read_utils.get_value_from_json("../test_data/data.json", "browser")

        if browser_name == "edge":
            self.driver = webdriver.Edge()
        elif browser_name == "ff":
            self.driver = webdriver.Firefox()
        elif browser_name == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://demowebshop.tricentis.com/")
        yield
        self.driver.quit()
