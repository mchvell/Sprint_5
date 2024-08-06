from framework.BasePage import BasePage
from selenium.webdriver.common.by import By


class NavBarLocators:
    NAVBAR_TABS = {
        "constructor": (By.XPATH, "//p[text()='Конструктор']"),
        "order_feed": (By.XPATH, "//p[text()='Лента Заказов']"),
        "main": (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']"),
        "lk": (By.XPATH, "//p[text()='Личный Кабинет']")
    }


class NavBarHelper(BasePage):
    def switcher(self, nav_tab):
        nav_bar_locator = NavBarLocators.NAVBAR_TABS.get(nav_tab)
        if nav_bar_locator:
            self.find_element(nav_bar_locator, 10).click()
        else:
            raise ValueError(f"Неизвестная таба {nav_tab}")
