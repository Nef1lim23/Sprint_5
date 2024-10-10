import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
from helper import DataGeneration


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def authorization(driver):

    wait = WebDriverWait(driver, 5)

    email_for_authorization = DataGeneration.email_for_authorization()
    password_for_authorization = DataGeneration.password_for_authorization()

    driver.get('https://stellarburgers.nomoreparties.site/login')
    wait.until(EC.visibility_of_element_located(locators.EMAIL_INPUT_XPATH))

    driver.find_element(*locators.EMAIL_INPUT_XPATH).send_keys(email_for_authorization)
    driver.find_element(*locators.PASSWORD_INPUT_XPATH).send_keys(password_for_authorization)
    driver.find_element(*locators.LOGIN_BUTTON_XPATH).click()

    wait.until(EC.visibility_of_element_located(locators.CONFIRM_ORDER_BUTTON_XPATH))

    yield driver
