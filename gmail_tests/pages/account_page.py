from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.remove_button = (By.ID, "com.android.settings:id/button")

    def visible_account_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.remove_button))

    def remove_account(self):
        self.driver.find_element(*self.remove_button).click()