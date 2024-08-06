from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_bread_tab(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Булки']")))

    def get_bread_header(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Булки']")))

    def get_sauce_tab(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']")))

    def get_sauce_header(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Соусы']")))

    def get_filling_tab(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Начинки']")))

    def get_filling_header(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Начинки']")))

    def enter_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']")))

    def switch_tab(self, tab):
        if tab == "breads":
            self.get_bread_tab().click()
        elif tab == "sauces":
            self.get_sauce_tab().click()
        elif tab == "fillings":
            self.get_filling_tab().click()
        else:
            raise ValueError(f"Неизвестная таба: {tab}")