from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class GoogleServicesPage:
    def __init__(self, driver):
        self.driver = driver
        self.accetp = (By.ID, "//android.widget.Button[@text='ACCEPT']")

    def visible_google_sercvices(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.accetp))

    def click_accetp(self):
        self.driver.find_element(*self.accetp).click()