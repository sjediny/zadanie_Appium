from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

class NotificationBarPage:
    def __init__(self, driver):
        self.driver = driver
        self.setting_button = (By.ID, "Settings")

    def pull_down_notification_bar(self):
        screen_size = self.driver.get_window_size()
        start_x = screen_size['width'] / 2
        start_y = 0
        end_y = screen_size['height']

        action = TouchAction(self.driver)
        action.long_press(None, start_x, start_y).move_to(None, start_x, end_y).release().perform()

def navigate_to_setting(self):
        # Wait for the settings button to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.setting_button)
        )
        # Click the settings button
        self.driver.find_element(*self.setting_button).click()