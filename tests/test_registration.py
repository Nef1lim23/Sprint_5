from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import Locators
import helper


def test_registration(driver):

    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*Locators.NAME_INPUT_XPATH).send_keys(helper.generate_random_name(2, 12))
    driver.find_element(*Locators.EMAIL_REGISTRATION_XPATH).send_keys(helper.generate_random_email(3, 10))
    driver.find_element(*Locators.PASSWORD_INPUT_REGISTRATION_XPATH).send_keys(helper.generate_random_password(6, 12))
    driver.find_element(*Locators.BUTTON_REGISTRATION_XPATH).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON_XPATH))

    assert driver.find_element(*Locators.LOGIN_BUTTON_XPATH).text == 'Войти'

    driver.quit()


def test_registration_invalid_password(driver):

    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*Locators.NAME_INPUT_XPATH).send_keys(helper.generate_random_name(2, 12))
    driver.find_element(*Locators.EMAIL_REGISTRATION_XPATH).send_keys(helper.generate_random_email(3, 10))
    driver.find_element(*Locators.PASSWORD_INPUT_REGISTRATION_XPATH).send_keys(helper.generate_random_password(1, 3))
    driver.find_element(*Locators.BUTTON_REGISTRATION_XPATH).click()

    assert driver.find_element(*Locators.MASSAGE_IS_AN_INCORRECT_PASSWORD).text == 'Некорректный пароль'

    driver.quit()

