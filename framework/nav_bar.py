from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavBar:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_constructor(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Конструктор']")))

    def get_order_feed(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Лента Заказов']")))

    def get_logo(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")))

    def get_lk_locator(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']")))

    def switch_tab(self, tab):
        if tab == "constructor":
            self.get_constructor().click()
        elif tab == "order_feed":
            self.get_order_feed().click()
        elif tab == "logo":
            self.get_logo().click()
        elif tab == "lk":
            self.get_lk_locator().click()
        else:
            raise ValueError(f"Неизвестная таба: {tab}")
