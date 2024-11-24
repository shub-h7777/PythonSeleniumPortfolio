from base.webdriver_listener import WebDriverWrapper  # IMPORTING WEBDRIVER WRAPPER CLASS
from page.homepage_before_login import HomePage_before_login
from page.loginpage import LoginPage
from page.homepageafterlogin import HomePageAfterLogin


class TestDropDownFunctionality(WebDriverWrapper):

    def test_display_dropdown_Apparel_and_shops(self):
        computingandinternet = HomePageAfterLogin(self.driver)
        homepage = HomePage_before_login(self.driver)
        loginpage = LoginPage(self.driver)
        homepage_after_login = HomePageAfterLogin(self.driver)

        # item count value
        item_count = 12

        # login in the application
        homepage.click_on_log_in_link()
        loginpage.enter_email_password_and_click_login("demo@shubham.com", "demo@shubham.com")
        homepage_after_login.verify_user_is_login("demo@shubham.com")

        # Verify user is login
        computingandinternet.verify_user_is_login("demo@shubham.com")

        # add to cart computing and internet button.
        computingandinternet.click_on_category("Apparel and Shoes")

        # select dropdown value as variable count
        homepage_after_login.set_dropdown_on_display_dropdown(str(item_count))

        # verify the item count is same as dropdown value.
        homepage_after_login.verify_total_item_count(str(item_count))
