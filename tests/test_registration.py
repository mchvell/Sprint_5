import pytest

from framework.nav_bar import NavBar
from framework.lk_auth_page import AuthPage
from framework.lk_reg_page import RegPage


@pytest.fixture(scope="function")
def open_registration_page(open_browser):
    navbar = NavBar(open_browser)
    navbar.get_lk_locator().click()

    auth_page = AuthPage(open_browser)
    auth_page.get_registration_link().click()


class TestRegistrationForm:
    def test_registration_form_name(self, open_registration_page, open_browser):
        registration_page = RegPage(open_browser)
        registration_page.fill_the_form("Антуан","mchvell@tf.ru","ForD1*")

        name = registration_page.get_attribute_value(registration_page.get_name_input(), "value")
        assert name == "Антуан"

    def test_registration_form_email(self, open_registration_page, open_browser):
        registration_page = RegPage(open_browser)
        registration_page.fill_the_form("Антуан", "mchvell@tf.ru", "ForD1*")

        email = registration_page.get_attribute_value(registration_page.get_email_input(), "value")
        assert "@" in email and "." in email

    def test_registration_form_password_lenght(self, open_registration_page, open_browser):
        registration_page = RegPage(open_browser)
        registration_page.fill_the_form("Антуан", "mchvell@tf.ru", "ForD1*")

        password = registration_page.get_attribute_value(registration_page.get_password_input(), "value")
        assert len(password) >= 6

    def test_registration_form_incorrect_pass(self, open_registration_page, open_browser):

        registration_page = RegPage(open_browser)
        registration_page.fill_the_form("Гэб", "sport@tf.ru", "100")
        registration_page.get_name_input().click()

        incorrect_password = registration_page.get_incorrect_password().text

        assert incorrect_password == "Некорректный пароль"
