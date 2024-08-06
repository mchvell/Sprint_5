from time import sleep

from framework.nav_bar import NavBar
from framework.lk_auth_page import AuthPage
from framework.profile_page import ProfilePage
from framework.lk_reg_page import RegPage
from framework.reset_password_page import ResetPasswordPage
from framework.main_page import MainPage


class TestAuthorization:
    def test_enter_from_navbar(self, open_browser):
        navbar = NavBar(open_browser)
        navbar.switch_tab("lk")

        user = AuthPage(open_browser)
        user.get_authorization("gubanov12qa@yandex.ru","fRodoAndBilbo")

        navbar.switch_tab("lk")
        profile_page = ProfilePage(open_browser)
        text = profile_page.exit_button().text
        assert text == "Выход"

    # глупый тест
    def test_enter_from_reg_page(self, open_browser):
        navbar = NavBar(open_browser)
        navbar.switch_tab("lk")
        # navbar.get_lk_locator().click()

        user = AuthPage(open_browser)
        user.get_registration_link().click()

        registration_page = RegPage(open_browser)
        registration_page.get_enter_link().click()

        user = AuthPage(open_browser)
        user.get_authorization("gubanov12qa@yandex.ru", "fRodoAndBilbo")
        sleep(5)

        navbar.switch_tab("lk")
        profile_page = ProfilePage(open_browser)
        text = profile_page.exit_button().text
        assert text == "Выход"

    # еще один глупый тест
    def test_enter_from_reset_password_page(self, open_browser):
        navbar = NavBar(open_browser)
        navbar.switch_tab("lk")

        user = AuthPage(open_browser)
        user.get_reset_password_link().click()

        reset_password_page = ResetPasswordPage(open_browser)
        reset_password_page.get_enter_link().click()

        user.get_authorization("gubanov12qa@yandex.ru", "fRodoAndBilbo")

        navbar.switch_tab("lk")
        profile_page = ProfilePage(open_browser)
        text = profile_page.exit_button().text
        assert text == "Выход"

    def test_enter_from_main_page(self, open_browser):
        navbar = NavBar(open_browser)
        navbar.switch_tab("logo")

        main_page = MainPage(open_browser)
        main_page.enter_button().click()

        user = AuthPage(open_browser)
        user.get_authorization("gubanov12qa@yandex.ru", "fRodoAndBilbo")
        sleep(5)

        navbar.switch_tab("lk")
        profile_page = ProfilePage(open_browser)
        text = profile_page.exit_button().text
        assert text == "Выход"






