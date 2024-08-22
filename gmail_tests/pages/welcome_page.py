from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WelcomePage:
    def __init__(self, driver):
        self.driver = driver
        self.got_it = (By.ID, "com.google.android.gm:id/welcome_tour_got_it")

    def visible_welcome(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.got_it))
    def click_gotit(self):
        self.driver.find_element(*self.got_it).click()