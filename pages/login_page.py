from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = "accounts/login/"
        assert login_url in self.url, "URL is correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.element_is_present(*LoginPageLocators.LOGIN_EMAIL), "Email field is present"
        assert self.element_is_present(*LoginPageLocators.LOGIN_PASSWORD), "Password field is present"
        assert  self.element_is_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is present"
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.element_is_present(*LoginPageLocators.REG_EMAIL), "Email field is present"
        assert self.element_is_present(*LoginPageLocators.REG_PASSWORD_1), "Password_1 field of registration form is present"
        assert self.element_is_present(*LoginPageLocators.REG_PASSWORD_2), "Password_2 field of registration form is present"
        assert self.element_is_present(*LoginPageLocators.REG_BUTTON), "Registration button is present"