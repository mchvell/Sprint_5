from framework.BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPageLocators:
    TABS = {
        "bread": (By.XPATH, "//span[text()='Булки']"),
        "sauce": (By.XPATH, "//span[text()='Соусы']"),
        "topping": (By.XPATH, "//span[text()='Начинки']")
    }

    TABS_HEADERS = {
        "bread": (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Булки']"),
        "sauce": (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Соусы']"),
        "topping": (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Начинки']")
    }

    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")


class MainPageHelper(BasePage):
    def click_on_enter_button(self):
        return self.find_element(MainPageLocators.ENTER_BUTTON, 10).click()

    def set_tab(self, tab):
        tab_locator = MainPageLocators.TABS.get(tab)
        if tab_locator:
            self.find_element(tab_locator, 10).click()
        else:
            raise ValueError(f"Неизвестная таба {tab}")

    def get_tab_header_text(self, tab):
        header_locator = MainPageLocators.TABS_HEADERS.get(tab)
        if header_locator:
            header_element = self.find_element(header_locator, 10)
            return header_element.text
        else:
            raise ValueError(f"Неизвестная таба {tab}")

