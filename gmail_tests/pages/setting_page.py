from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SettingPage:
    def __init__(self, driver):
        self.driver = driver
        self.accounts = (By.XPATH, "//android.widget.TextView[@resource-id='android:id/title' and @text='Passwords, passkeys & accounts']")
    def visible_setting_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.accounts))

    def navigate_to_accounts(self):
        self.driver.find_element(*self.accounts).click()
