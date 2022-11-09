from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    # Method get element

    def get_element(self, selector, locator=By.XPATH, timeout=30, select_method="clickable"):
        """ Gets the element  """

        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((locator, selector)))
        wait_driver = WebDriverWait(self.driver, timeout)
        if select_method == "clickable":
            return wait_driver.until(EC.element_to_be_clickable((locator, selector)))
        elif select_method == "selected":
            return wait_driver.until(EC.element_to_be_clickable((locator, selector)))
        elif select_method == "visibility_located":
            return wait_driver.until(EC.visibility_of_element_located((locator, selector)))
        elif select_method == "presence_element":
            return wait_driver.until(EC.presence_of_element_located((locator, selector)))

    def get_current_url(self):
        """ Get current page address """

        url = self.driver.current_url
        print("Current url " + url)