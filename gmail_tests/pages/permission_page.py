from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class PermissionPage:
    def __init__(self, driver):
        self.driver = driver
        self.permission_deny = (By.ID, "com.android.permissioncontroller:id/permission_deny_button")
        self.permission_allow = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")

    def visible_permission(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.permission_deny))
    def click_permission_decision(self,decision):
        if decision == 'denied':
            self.driver.find_element(*self.permission_deny).click()
        elif decision == 'allowed':
            self.driver.find_element(*self.permission_allow).click()