from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class PopUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.close = (By.ID, "com.google.android.gm:id/dismiss_button")

    def visible_pop_up(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.close))

    def close_pop_up(self):
            self.driver.find_element(*self.close).click()