from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    FIND_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[2]/div/div[2]/form/input')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON_LINK = (By.XPATH, "//span[@class='btn-group']/a")
class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[name='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")
    REG_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REG_PASSWORD_1 = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REG_PASSWORD_2 = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REG_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BUSKET_BUTTON = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    COUNT_IN_STOCK = (By.XPATH, '//*[@id="content_inner"]/article/table/tbody/tr[6]/td')
    BOOK_NAME_IN_ALERT = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    BOOK_PRICE = (By.XPATH, '//*[@id="content_inner"]//p[@class="price_color"]')
    BOOK_PRICE_IN_BUSKET_ALERT = (By.XPATH, '//div[@class="alertinner "]/p')
    BOOK_PRICE_IN_HEADER_BUSKET = (By.XPATH, '//div[@class="row"]/div[contains(@class, "basket-mini")]')
    BENEFIT_ALERT = (By.XPATH, '//*[@id="messages"]/div[2]/div/strong')

class BasketPageLocators():
    UPDATE_BUTTON = (By.XPATH, "//span[@class='input-group-btn']/button")
    EMPTY_BUTTON_TEXT = (By.XPATH, "//div[@id='content_inner']/p")