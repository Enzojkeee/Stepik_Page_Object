from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[name='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")
    REG_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REG_PASSWORD_1 = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REG_PASSWORD_2 = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REG_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
