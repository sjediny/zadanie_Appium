from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class AddressesListPage:
    def __init__(self, driver):
        self.driver = driver
        self.new_email_address = (By.ID, "com.google.android.gm:id/setup_addresses_add_another")
        self.account_email = (By.ID, "com.google.android.gm:id/account_address")
        self.account_name = (By.ID, "com.google.android.gm:id/account_display_name")
        self.navigatetion_to_inbox = (By.ID, "com.google.android.gm:id/action_done")

    def click_new_email_address(self):
        self.driver.find_element(*self.new_email_address).click()

    def visible_adresses_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.new_email_address))

    def is_account_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.account_email))
            return True
        except NoSuchElementException:
            return False

    def get_account_name(self):
        return self.driver.find_element(*self.account_name).text


    def get_acount_email(self):
        return self.driver.find_element(*self.account_email).text

    def navite_to_inbox(self):
        self.driver.find_element(*self.navigatetion_to_inbox).click()
