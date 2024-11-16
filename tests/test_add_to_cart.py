import time

from base.webdriver_listener import WebDriverWrapper  # IMPORTING WEBDRIVER WRAPPER CLASS
from page.homepage_before_login import HomePage_before_login
from page.loginpage import LoginPage
from page.homepageafterlogin import HomePageAfterLogin
from page.shopping_cart import ShoppingCart


class Test_Add_To_Cart(WebDriverWrapper):

    def test_add_book_to_cart_and_update(self):
        computingandinternet = HomePageAfterLogin(self.driver)
        shoppingCart = ShoppingCart(self.driver)
        homepage = HomePage_before_login(self.driver)
        loginpage = LoginPage(self.driver)
        homepage_after_login = HomePageAfterLogin(self.driver)

        # login in the application
        homepage.click_on_log_in_link()
        loginpage.enter_email_password_and_click_login("demo@shubham.com", "demo@shubham.com")
        homepage_after_login.verify_user_is_login("demo@shubham.com")

        # Verify user is login
        computingandinternet.verify_user_is_login("demo@shubham.com")

        # add to cart computing and internet button.
        computingandinternet.click_on_category("Books")
        computingandinternet.add_to_cart_computing_and_internet()

        # click on shopping cart hyperlink
        homepage_after_login.click_on_shopping_cart_button()

        # delete the cart items
        shoppingCart.click_on_delete_cart_checkbox()
        shoppingCart.click_on_update_shopping_cart_button()

        # verify shopping Cart text
        shoppingCart.get_empty_shopping_cart_text()
