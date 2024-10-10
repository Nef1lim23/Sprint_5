from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators


class TestConstructorSection:
    def test_of_switching_to_sauces(self, driver, authorization):
        sauces = driver.find_element(*locators.SAUCES_SECTION)
        sauces.click()
        sauces_div = driver.find_element(*locators.SAUCES_DIV)
        assert 'current' in sauces_div.get_attribute('class')

    def test_of_switching_to_toppings(self, driver, authorization):
        toppings = driver.find_element(*locators.TOPPINGS_SECTION)
        toppings.click()
        toppings_div = driver.find_element(*locators.TOPPINGS_DIV)
        assert 'current' in toppings_div.get_attribute('class')

    def test_of_switching_to_buns(self, driver, authorization):
        toppings = driver.find_element(*locators.TOPPINGS_SECTION)
        toppings.click()
        buns = driver.find_element(*locators.BUNS_SECTION)
        buns.click()
        buns_div = driver.find_element(*locators.BUNS_DIV)
        assert 'current' in buns_div.get_attribute('class')
