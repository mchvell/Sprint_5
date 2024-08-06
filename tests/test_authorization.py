from framework.MainPage import MainPageHelper
from framework.AuthPage import AuthPageHelper
from framework.NavBar import NavBarHelper
from framework.ProfilePage import ProfilePageHelper
from framework.RegPage import RegPageHelper


class TestAuth:
    def test_auth_from_constructor_page(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()
        main_page.click_on_enter_button()

        auth_page = AuthPageHelper(browser)
        auth_page.fill_auth_form(email="gubanov12qa@yandex.ru", password="fRodoAndBilbo")
        auth_page.click_enter_button()

        nav_bar = NavBarHelper(browser)
        nav_bar.switcher("lk")
        assert "/account/profile" in browser.current_url

    def test_auth_from_auth_page(self, browser):
        auth_page = AuthPageHelper(browser)
        auth_page.go_to_site()
        auth_page.fill_auth_form(email="gubanov12qa@yandex.ru", password="fRodoAndBilbo")
        auth_page.click_enter_button()

        nav_bar = NavBarHelper(browser)
        nav_bar.switcher("lk")
        assert "/account/profile" in browser.current_url

    def test_auth_from_nav_bar(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()

        nav_bar = NavBarHelper(browser)
        nav_bar.switcher("lk")
        assert "site/login" in browser.current_url

        auth_page = AuthPageHelper(browser)
        auth_page.fill_auth_form(email="gubanov12qa@yandex.ru", password="fRodoAndBilbo")
        auth_page.click_enter_button()

        nav_bar.switcher("lk")

        profile = ProfilePageHelper(browser)
        exit_button_text = profile.get_text_on_exit_button()
        assert exit_button_text == "Выход"
       
    def test_auth_from_reg_page(self, browser):
        reg_page = RegPageHelper(browser)
        reg_page.go_to_site()
        reg_page.click_on_auth_link()
        assert "site/login" in browser.current_url

        auth_page = AuthPageHelper(browser)
        auth_page.fill_auth_form(email="gubanov12qa@yandex.ru", password="fRodoAndBilbo")
        auth_page.click_enter_button()

        nav_bar = NavBarHelper(browser)
        nav_bar.switcher("lk")

        profile = ProfilePageHelper(browser)
        exit_button_text = profile.get_text_on_exit_button()
        assert exit_button_text == "Выход"
