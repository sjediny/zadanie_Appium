from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_address = (By.XPATH, "//android.widget.EditText[@resource-id='identifierId']")
        self.next_button = (By.XPATH, "//android.widget.Button[@text='Next']")

    def visible_login(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.email_address))
    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.email_address))
        self.driver.find_element(*self.email_address).send_keys(email)

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.next_button))
        self.driver.find_element(*self.next_button).click()