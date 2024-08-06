from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def exit_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Выход']")))
