from framework.RegPage import RegPageHelper, RegLocators


class TestRegistration:
    def test_registration_form_name(self, browser):
        reg_page = RegPageHelper(browser)
        reg_page.go_to_site()

        reg_page.fill_reg_form(name="Антуан")
        name_input = reg_page.get_input_value("name")

        assert name_input == "Антуан"

    def test_registration_form_email(self, browser):
        reg_page = RegPageHelper(browser)
        reg_page.go_to_site()

        reg_page.fill_reg_form(email="exupirie@qa.com")
        email_input = reg_page.get_input_value("email")

        assert "@" in email_input and "." in email_input

    def test_registration_form_password_length(self, browser):
        reg_page = RegPageHelper(browser)
        reg_page.go_to_site()

        reg_page.fill_reg_form(password="ForD1*")
        length_password = len(reg_page.get_input_value("password"))
        assert length_password >= 6

    def test_registration_form_incorrect_pass(self, browser):
        reg_page = RegPageHelper(browser)
        reg_page.go_to_site()

        reg_page.fill_reg_form(password="Fo")
        reg_page.click_on_input("name")
        incorrect_password = reg_page.get_incorrect_password_text()
        assert incorrect_password == "Некорректный пароль"
