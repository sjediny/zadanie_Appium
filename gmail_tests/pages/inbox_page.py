from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class InboxPage:
    def __init__(self, driver):
        self.driver = driver
        self.inbox = (By.ID, "com.google.android.gm:id/inbox_view")

    def is_inbox_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.inbox))
            return True
        except NoSuchElementException:
            return False