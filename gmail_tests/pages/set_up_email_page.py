from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SetUpEmailPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_clients = (By.XPATH, ("//android.widget.LinearLayout[@resource-id='com.google.android.gm:id/account_setup_item']"))

    def visible_set_up_email(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_clients))

    def click_google(self):
        self.driver.find_elements(*self.email_clients)[0].click()