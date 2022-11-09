import pytest

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    yield driver

    driver.quit()