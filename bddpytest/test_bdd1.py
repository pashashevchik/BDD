import pytest

from pytest_bdd import scenario, scenarios, given, when, then
from pages.login_page import LoginPage
from base.base_class import BasePage
from pathlib import Path

featureFileDir = "myfeatures"
featureFile = 'login_valid_data.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


@scenario(FEATURE_FILE, "Authorization with valid data")
def test_valid_login():
    pass


@given("I visit the login page")
def visit_login_page(driver):
    LoginPage(driver).open_login_page()


@given("I press account button")
def press_account_button(driver):
    LoginPage(driver).press_account_button()


@when("I login with valid data")
def fill_field_data(driver):
    LoginPage(driver).fill_field_login("pshevchik44@mail.ru")
    LoginPage(driver).fill_field_password("CG6BBBI4")
    LoginPage(driver).press_enter_button()


@then("I should be on the main page")
def main_page(driver):
    assert '21vek' in driver.current_url




