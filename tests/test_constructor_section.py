from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Locators


def test_of_switching_to_sauces(driver, authorization):

    sauces = driver.find_element(*Locators.SAUCES_SECTION)
    sauces.click()
    sauces_div = driver.find_element(*Locators.SAUCES_DIV)
    assert 'current' in sauces_div.get_attribute('class')


def test_of_switching_to_toppings(driver, authorization):

    toppings = driver.find_element(*Locators.TOPPINGS_SECTION)
    toppings.click()
    toppings_div = driver.find_element(*Locators.TOPPINGS_DIV)
    assert 'current' in toppings_div.get_attribute('class')


def test_of_switching_to_buns(driver, authorization):

    toppings = driver.find_element(*Locators.TOPPINGS_SECTION)
    toppings.click()
    buns = driver.find_element(*Locators.BUNS_SECTION)
    buns.click()
    buns_div = driver.find_element(*Locators.BUNS_DIV)
    assert 'current' in buns_div.get_attribute('class')
