import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Firefox(GeckoDriverManager().install())

driver=webdriver.Firefox()


driver.get("https://demowebshop.tricentis.com/")

time.sleep(5)
driver.quit()
