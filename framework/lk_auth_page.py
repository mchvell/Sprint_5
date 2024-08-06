from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_email_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name']")))

    def get_password_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))

    def get_enter_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']")))

    def get_registration_link(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Зарегистрироваться']")))

    def get_reset_password_link(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Восстановить пароль']")))

    def get_authorization(self, email, password):
        self.get_email_input().send_keys(email)
        self.get_password_input().send_keys(password)
        self.get_enter_button().click()

    def registration_link(self):
        self.get_registration_link()