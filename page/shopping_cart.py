from selenium.webdriver.common.by import By


class ShoppingCart:

    def __init__(self, driver):
        self.driver = driver

    """ Elements """
    checkbox_for_deleting_cart = "removefromcart"  # Name
    update_shopping_cart_button = "updatecart"  # Name
    empty_shopping_cart_text = "//div[contains(text(),'Your Shopping Cart is empty!')]"
    apply_coupun = "discountcouponcode"


    # methods
    def click_on_delete_cart_checkbox(self):
        self.driver.find_element(By.NAME, self.checkbox_for_deleting_cart).click()

    def click_on_update_shopping_cart_button(self):
        self.driver.find_element(By.NAME, self.update_shopping_cart_button).click()

    def get_empty_shopping_cart_text(self):
        self.driver.find_element(By.XPATH, self.empty_shopping_cart_text)

    def send_coupon_apply_coupon_textbox(self, coupon):
        self.driver.find_element(By.NAME, self.apply_coupun).sendkeys(coupon)
