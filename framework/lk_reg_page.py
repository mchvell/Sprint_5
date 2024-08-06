from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_name_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name']")))

    def get_email_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Email']/following-sibling::input")))

    def get_password_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Пароль']/following-sibling::input")))

    def get_registration_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Зарегистрироваться']")))

    def get_incorrect_password(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Некорректный пароль']")))

    def get_enter_link(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']")))

    def fill_the_form(self, name, email, password):
        self.get_name_input().send_keys(name)
        self.get_email_input().send_keys(email)
        self.get_password_input().send_keys(password)

    def submit_form(self):
        self.get_registration_button().click()

    @staticmethod
    def get_attribute_value(element, attribute):
        return element.get_attribute(attribute)
