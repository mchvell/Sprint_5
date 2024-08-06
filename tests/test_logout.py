import pytest

from framework.AuthPage import AuthPageHelper
from framework.NavBar import NavBarHelper
from framework.ProfilePage import ProfilePageHelper


@pytest.fixture(scope="session")
def authorization(browser):
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_site()
    auth_page.fill_auth_form(
        email="gubanov12qa@yandex.ru",
        password="fRodoAndBilbo"
    )
    auth_page.click_enter_button()


class TestLogOut:
    def test_logout(self, browser, authorization):
        nav_bar = NavBarHelper(browser)
        nav_bar.switcher("lk")

        profile_page = ProfilePageHelper(browser)

        exit_button_text = profile_page.get_text_on_exit_button()
        assert exit_button_text == "Выход"

        profile_page.click_on_exit_button()
        url = browser.current_url
        assert "/login" in url
