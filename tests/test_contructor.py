from framework.main_page import MainPage


class TestConstructor:
    def test_constructor_bread_tab_preselected(self, open_browser):
        main_page_constructor = MainPage(open_browser)
        bread_header = main_page_constructor.get_bread_header().text
        assert bread_header == "Булки"

    def test_constructor_sauces_tab(self, open_browser):
        main_page_constructor = MainPage(open_browser)
        main_page_constructor.switch_tab("sauces")
        sauces_header = main_page_constructor.get_sauce_header().text
        assert sauces_header == "Соусы"

    def test_constructor_fillings_tab(self, open_browser):
        main_page_constructor = MainPage(open_browser)
        main_page_constructor.switch_tab("fillings")
        fillings_header = main_page_constructor.get_filling_header().text
        assert fillings_header == "Начинки"

