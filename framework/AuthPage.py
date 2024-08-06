from framework.BasePage import BasePage
from selenium.webdriver.common.by import By


class AuthLocators:
    INPUTS = {
        "email": (By.XPATH, "//input[@name='name']"),
        "password": (By.XPATH, "//input[@type='password']")
    }

    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")

    LINKS = {
        "registration": (By.XPATH, "//a[text()='Зарегистрироваться']"),
        "reset_password": (By.XPATH, "//a[text()='Восстановить пароль']")
    }


class AuthPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://stellarburgers.nomoreparties.site/login"

    def fill_auth_form(self, **kwargs):
        for field, value in kwargs.items():
            locator = AuthLocators.INPUTS.get(field)
            if locator:
                self.find_element(locator, 10).send_keys(value)
            else:
                raise ValueError(f"Неизвестное поле {field}")

    def click_enter_button(self):
        self.find_element(AuthLocators.ENTER_BUTTON, 10).click()

    def click_link(self, link_name):
        link_locator = AuthLocators.LINKS.get(link_name)
        if link_locator:
            self.find_element(link_locator, 10).click()
        else:
            raise ValueError(f"Неизвестная ссылка {link_name}")


