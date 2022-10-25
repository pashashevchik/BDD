import time

import pytest
from selenium import webdriver
from pytest_bdd import scenario, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def browser():
    dr = webdriver.Chrome(ChromeDriverManager().install())

    yield dr

    dr.quit()


@scenario("login_valid_data.feature", "Valid login")
def test_valid_login():
    pass


@given("I visit the login page")
def visit_main_page(browser):
    browser.get("https://www.21vek.by/")
    browser.maximize_window()


@given("I press account button")
def press_account_button(browser):
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Аккаунт']"))).click()
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='loginButton']"))).click()


@when("I login with valid data")
def login_valid(browser):
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, 'login-email'))).send_keys("pshevchik44@mail.ru")
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, 'login-password'))).send_keys("CG6BBBI4")
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='loginSubmit']"))).click()


@then("I should be on the main page")
def on_mane_page(browser):
    assert '21vek' in browser.current_url




