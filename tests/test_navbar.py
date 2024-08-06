from framework.nav_bar import NavBar
from framework.main_page import MainPage
from framework.lk_auth_page import AuthPage


class TestNavBar:
    def test_nav_bar_main_page(self, open_browser):
        navbar = NavBar(open_browser)
        navbar.switch_tab("constructor")

        main_page = MainPage(open_browser)
        enter_button = main_page.enter_button().text
        assert enter_button == enter_button

    def test_nav_bar_lk(self, open_browser):
        navbar = NavBar(open_browser)
        navbar.switch_tab("lk")

        lk = AuthPage(open_browser)
        reset_password = lk.get_reset_password_link().text
        assert reset_password == "Восстановить пароль"
