from framework.MainPage import MainPageHelper


class TestConstructor:
    def test_tab_switcher_bread(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()
        tab_header = main_page.get_tab_header_text("bread")
        assert tab_header == "Булки"

    def test_tab_switcher_sauces(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()
        main_page.set_tab("sauce")
        tab_header = main_page.get_tab_header_text("sauce")
        assert tab_header == "Соусы"

    def test_tab_switcher_toppings(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()
        main_page.set_tab("topping")
        tab_header = main_page.get_tab_header_text("topping")
        assert tab_header == "Начинки"
