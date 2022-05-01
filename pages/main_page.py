from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage()

    def should_be_login_link(self):
        assert self.element_is_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_find_button(self):
        assert self.element_is_present(*MainPageLocators.FIND_BUTTON), "Find button is not on page"
