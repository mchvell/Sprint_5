import pytest
from time import sleep

from framework.main_page import MainPage
from framework.profile_page import ProfilePage
from framework.lk_auth_page import AuthPage
from framework.nav_bar import NavBar


@pytest.fixture(scope="function")
def authorization(open_browser):
    main_page = MainPage(open_browser)
    main_page.enter_button().click()

    auth_page = AuthPage(open_browser)
    auth_page.get_authorization("gubanov12qa@yandex.ru", "fRodoAndBilbo")


class TestExitProfile:
    def test_exit_profile(self, open_browser, authorization):
        nav_bar = NavBar(open_browser)

        nav_bar.switch_tab("lk")
        assert "/account/profile" in open_browser.current_url

        profile = ProfilePage(open_browser)
        exit_button = profile.exit_button()
        assert exit_button.text == "Выход"

        exit_button.click()
        auth = AuthPage(open_browser)
        enter_button = auth.get_enter_button().text
        assert enter_button == "Войти"
