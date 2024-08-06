from framework.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProfilePageLocators:
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")


class ProfilePageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://stellarburgers.nomoreparties.site/account/profile"

    def get_text_on_exit_button(self):
        return self.find_element(ProfilePageLocators.EXIT_BUTTON, 10).text

    def click_on_exit_button(self):
        return self.find_element(ProfilePageLocators.EXIT_BUTTON, 10).click()

