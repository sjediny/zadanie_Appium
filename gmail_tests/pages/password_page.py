from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class PasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.password_input = (By.XPATH, "//android.widget.EditText")
        self.next_button = (By.XPATH, "//android.widget.Button[@text='Next']")
        self.show_password = (By.XPATH, "//android.widget.CheckBox[@text='Show password']")

    def visible_password_page(self):
        WebDriverWait(self.driver, 12).until(
            EC.visibility_of_element_located(self.show_password))
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.show_password))

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.next_button))
        self.driver.find_element(*self.next_button).click()