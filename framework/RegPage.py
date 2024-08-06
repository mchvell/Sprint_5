from framework.BasePage import BasePage
from selenium.webdriver.common.by import By


class RegLocators:
    INPUTS = {
        "name": (By.XPATH, "//input[@name='name']"),
        "email": (By.XPATH, "//label[text()='Email']/following-sibling::input"),
        "password": (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    }

    END_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")

    AUTH_LINK = (By.XPATH, "//a[text()='Войти']")


class RegPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://stellarburgers.nomoreparties.site/register"

    def fill_reg_form(self, **kwargs):
        for field, value in kwargs.items():
            locator = RegLocators.INPUTS.get(field)
            if locator:
                self.find_element(locator, 10).send_keys(value)
            else:
                raise ValueError(f"Неизвестное поле {field}")

    def submit_form(self):
        return self.find_element(RegLocators.END_REGISTRATION_BUTTON, 10).click()

    def get_input_value(self, input_value):
        locator = RegLocators.INPUTS.get(input_value)
        if locator:
            element = self.find_element(locator, 10)
            return element.get_attribute('value')
        else:
            raise ValueError(f"Неизвестное поле {input_value}")

    def click_on_input(self, input):
        locator = RegLocators.INPUTS.get(input)
        if locator:
            self.find_element(locator, 10).click()
        else:
            raise ValueError(f"Неизвестное поле {input}")

    def click_on_auth_link(self):
        return self.find_element(RegLocators.AUTH_LINK, 10).click()

    def get_incorrect_password_text(self):
        return self.find_element(RegLocators.INCORRECT_PASSWORD, 10).text
