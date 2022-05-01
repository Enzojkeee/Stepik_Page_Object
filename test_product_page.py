from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_busket()
    time.sleep(3)