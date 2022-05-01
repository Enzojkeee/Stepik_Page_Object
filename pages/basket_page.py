from .base_page import BasePage
from .locators import BasketPageLocators
class BasketPage(BasePage):

    def should_no_elements_in_busket(self): # Проверка наличия покупок в корзине
        assert self.is_not_element_present(*BasketPageLocators.UPDATE_BUTTON)

    def should_be_empty_basket_text(self): # Проверка наличия уведомления: "Корзиина пуста"
        assert self.element_is_present(*BasketPageLocators.EMPTY_BUTTON_TEXT)