from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class EmailWelcomePage:
    def __init__(self, driver):
        self.driver = driver
        self.agree_button = (By.XPATH, "//android.widget.Button[@text='I agree']")

    def visible_welcome(self):
        WebDriverWait(self.driver, 12).until(
            EC.visibility_of_element_located(self.agree_button))

    def click_agree(self):
        self.driver.find_element(*self.agree_button).click()