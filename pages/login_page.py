from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BasePage


class LoginPage(BasePage):

    url = 'https://www.21vek.by/'
    # Locators

    ACCOUNT_SELECTOR_BUTTON_SELECTOR = "//span[text()='Аккаунт']"
    LOGIN_SELECTOR_BUTTON_SELECTOR = "//button[@data-testid='loginButton']"
    LOGIN_FIELD_SELECTOR = "//input[@id='login-email']"
    PASSWORD_FIELD_SELECTOR = "//input[@id='login-password']"
    ENTER_BUTTON_SELECTOR = "//button[@data-testid='loginSubmit']"

    def open_login_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def press_account_button(self):
        self.get_element(self.ACCOUNT_SELECTOR_BUTTON_SELECTOR).click()
        print("Press account button")
        self.get_element(self.LOGIN_SELECTOR_BUTTON_SELECTOR).click()
        print("Press login button")

    def fill_field_login(self, login):
        self.get_element(self.LOGIN_FIELD_SELECTOR).send_keys(login)
        print("Fill user email field")

    def fill_field_password(self, password):
        self.get_element(self.PASSWORD_FIELD_SELECTOR).send_keys(password)
        print("Fill user password field")

    def press_enter_button(self):
        self.get_element(self.ENTER_BUTTON_SELECTOR).click()
        print("Press enter button")