from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select    # for dropdown selection


class HomePageAfterLogin:

    def __init__(self, driver):
        self.driver = driver

    """ Elements Xpath """
    account_email_xpath = "(//a[@class= 'account'])[1]"
    book_hyperlink_xpath = "(//a[normalize-space()='Books'])[1]"
    apparel_and_shoes_hyperlink_xpath = "(//a[normalize-space()='Apparel & Shoes'])[1]"
    computing_and_internet_book_xpath = "(//input[@value= 'Add to cart'])[1]"
    shopping_cart = "//span[contains(text(),'Shopping cart')]"
    display_dropdown = "products-pagesize"      #id
    sort_by_dropdown = "products-orderby"        #id
    dropdown_value = "//select[@id='products-pagesize']/option[@selected='selected']"      #xpath

    def verify_user_is_login(self, expected_email):
        actual_email= self.driver.find_element(By.XPATH,self.account_email_xpath).text
        assert expected_email == actual_email

    """to click on category, like books, computer, Electronics and etc..."""
    def click_on_category(self, category_name):

        if (category_name == "Books"):
            self.driver.find_element(By.XPATH, self.book_hyperlink_xpath).click()
        elif (category_name == "Apparel and Shoes"):
            self.driver.find_element(By.XPATH, self.apparel_and_shoes_hyperlink_xpath).click()

    def add_to_cart_computing_and_internet(self):
        self.driver.find_element(By.XPATH, self.computing_and_internet_book_xpath).click()

    def click_on_shopping_cart_button(self):
        self.driver.find_element(By.XPATH, self.shopping_cart).click()

    """drop down can be handled by 3 ways.
    1.select_by_value()
    2.select_by_index()
    3.select_by_visible_text
    """
    def set_dropdown_on_display_dropdown(self, value):
        # self.driver.find_element(By.ID, self.display_dropdown).click().select_by_index(1)
        # self.driver.find_element(By.ID, self.display_dropdown).select_by_visible_text(value)

        element = self.driver.find_element(By.ID, self.display_dropdown)
        dropdown = Select(element)
        dropdown.select_by_visible_text(value)

    def verify_total_item_count(self, expected_value):
        actual_value = self.driver.find_element(By.XPATH, self.dropdown_value).text
        assert actual_value == expected_value
        return True











