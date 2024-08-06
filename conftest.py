import pytest
from framework.webdriver_manager import WebDriverManager


@pytest.fixture(scope="function")
def open_browser():
    web_driver_manager = WebDriverManager()
    web_driver_manager.driver.get("https://stellarburgers.nomoreparties.site")
    yield web_driver_manager.driver
    web_driver_manager.quit()
