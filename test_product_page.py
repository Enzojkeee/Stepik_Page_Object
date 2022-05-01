from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time
import pytest


# @pytest.mark.parametrize('link_offer', ['2']) #['0','1','2','3','4','5','6',pytest.param('7', marksz    =pytest.mark.xfail),'8','9'] )
# def test_guest_can_add_product_to_basket(browser, link_offer):
#     link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_offer}"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_to_busket()
# @pytest.mark.xfail()
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_offer}"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.click_add_to_busket_button()
#     product_page.solve_quiz_and_get_code()
#     product_page.should_not_be_success_message()
#
# def test_guest_cant_see_success_message(browser, link_offer):
#     link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_offer}"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_not_be_success_message()

#
# @pytest.mark.xfail()
# def test_message_disappeared_after_adding_product_to_basket(browser, link_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_offer}"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.click_add_to_busket_button()
#     product_page.solve_quiz_and_get_code()
#     product_page.should_disappeared_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207//"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_busket_button()
    page.guest_can_go_to_busket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_no_elements_in_busket()
    basket_page.should_be_empty_basket_text()