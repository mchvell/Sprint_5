from framework.MainPage import MainPageHelper
from framework.NavBar import NavBarHelper


class TestNavBar:
    def test_open_constructor(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()

        nav_bar = NavBarHelper(browser)
        nav_bar.switcher("constructor")
        constructor_tab = main_page.get_tab_header_text("bread")
        assert constructor_tab == "Булки"

    def test_click_on_logo(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()

        nav_bar = NavBarHelper(browser)
        nav_bar.switcher("main")
        constructor_tab = main_page.get_tab_header_text("bread")
        assert constructor_tab == "Булки"

    def test_click_on_order_feed(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()

        nav_bar = NavBarHelper(browser)
        nav_bar.switcher("order_feed")
        url = browser.current_url
        assert "/feed" in url

    def test_click_on_lk(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()

        nav_bar = NavBarHelper(browser)
        nav_bar.switcher("lk")

        url = browser.current_url
        assert "/login" in url
