from .base_page import BasePage
from .locators import ProductPageLocators
import re
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class ProductPage(BasePage):

    def add_to_busket(self): # Функция добавления в корзину
        self.should_be_at_stock()
        self.should_be_add_to_busket_button()
        add_to_busket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BUTTON)
        add_to_busket_button.click()
        self.solve_quiz_and_get_code()
        time.sleep(3)
        self.check_price_in_busket()
        self.check_book_name_in_alert()

    def should_be_add_to_busket_button(self): # Кнопка добавить в корзину должна присутствовать на странице
        assert self.element_is_present(*ProductPageLocators.ADD_TO_BUSKET_BUTTON), "Button_Add_to_Busket is not presented"

    def should_be_at_stock(self): # Проверка наличия товара на складе
        count_in_stock_string = self.browser.find_element(*ProductPageLocators.COUNT_IN_STOCK).text
        count_in_stock=[int(i) for i in re.findall(r'-?\d+\d', count_in_stock_string)]
        assert count_in_stock[0] > 0, "Item is out of stock"

    def check_price_in_busket(self): # Проверка цены на товар в уведомлении и хэдере
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price_in_busket_header = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_HEADER_BUSKET)
        book_price_busket_notification = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BUSKET_ALERT)
        assert book_price.text in book_price_busket_notification.text, "Price in alert is not same as book price"
        assert book_price.text in book_price_in_busket_header.text, "Price of header busket is not same as book price"

    def check_book_name_in_alert(self): # Проверка названия книги в уведомлении
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_in_alert = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_ALERT)
        assert book_name.text in book_name_in_alert.text, "Alert book name is not same as bought book name"


    def solve_quiz_and_get_code(self): # Решение задачи в alert
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")