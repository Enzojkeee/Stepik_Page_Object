from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()       # открываем страницу
    page.should_be_find_button() # Проверка кнопки Найти
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_busket_button()
    page.guest_can_go_to_busket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_no_elements_in_busket()
    basket_page.should_be_empty_basket_text()





