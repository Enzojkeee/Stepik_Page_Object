from .pages.product_page import ProductPage
import time


def test_can_add_to_busket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_busket()
    time.sleep(3)