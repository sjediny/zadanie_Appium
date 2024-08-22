from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class AccountsPage:
    def __init__(self, driver):
        self.driver = driver
        self.change_button = (By.ID, "com.android.settings:id/change_button")

    def visible_accounts_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.change_button))

    def navigate_to_account(self,email):
        xpath_expression = f"//*[contains(@text, '{email}')]"
        self.driver.find_element(By.XPATH, xpath_expression).click()