import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Locators


@pytest.fixture()
def email_for_authorization():
    email = 'korneev_14@gmail.ru'
    return email


@pytest.fixture()
def password_for_authorization():
    password = '123123'
    return password


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture()
def authorization(driver, email_for_authorization, password_for_authorization):

    driver.implicitly_wait(10)
    driver.get('https://stellarburgers.nomoreparties.site/login')

    driver.find_element(*Locators.EMAIL_INPUT_XPATH).send_keys(email_for_authorization)
    driver.find_element(*Locators.PASSWORD_INPUT_XPATH).send_keys(password_for_authorization)
    driver.find_element(*Locators.LOGIN_BUTTON_XPATH).click()

    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located(Locators.CONFIRM_ORDER_BUTTON_XPATH))

    yield driver

    driver.quit()

