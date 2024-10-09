from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Locators


def test_authorization_through_personal_account_true(driver, email_for_authorization, password_for_authorization):

    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SUBMIT_LOGIN_BUTTON_XPATH))

    driver.find_element(*Locators.PERSONAL_CABINET_BUTTON_XPATH).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ENTRY_FORM_XPATH))

    driver.find_element(*Locators.EMAIL_INPUT_XPATH).send_keys(email_for_authorization)
    driver.find_element(*Locators.PASSWORD_INPUT_XPATH).send_keys(password_for_authorization)
    driver.find_element(*Locators.LOGIN_BUTTON_XPATH).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON_TEXT_XPATH))

    assert driver.find_element(*Locators.ORDER_BUTTON_TEXT_XPATH).text == 'Оформить заказ'

    driver.quit()


def test_authorization_through_home_page_true(driver, email_for_authorization, password_for_authorization):

    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SUBMIT_LOGIN_BUTTON_XPATH))

    driver.find_element(*Locators.SUBMIT_LOGIN_BUTTON_XPATH).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ENTRY_FORM_XPATH))

    driver.find_element(*Locators.EMAIL_INPUT_XPATH).send_keys(email_for_authorization)
    driver.find_element(*Locators.PASSWORD_INPUT_XPATH).send_keys(password_for_authorization)
    driver.find_element(*Locators.LOGIN_BUTTON_XPATH).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON_TEXT_XPATH))

    assert driver.find_element(*Locators.ORDER_BUTTON_TEXT_XPATH).text == 'Оформить заказ'

    driver.quit()


def test_authorization_through_registration_form(driver, email_for_authorization, password_for_authorization):

    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Locators.OPEN_LOGIN_PAGE_LINK_XPATH).click()

    driver.find_element(*Locators.EMAIL_INPUT_XPATH).send_keys(email_for_authorization)
    driver.find_element(*Locators.PASSWORD_INPUT_XPATH).send_keys(password_for_authorization)
    driver.find_element(*Locators.LOGIN_BUTTON_XPATH).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON_TEXT_XPATH))

    assert driver.find_element(*Locators.ORDER_BUTTON_TEXT_XPATH).text == 'Оформить заказ'

    driver.quit()


def test_authorization_through_password_recovery_form(driver, email_for_authorization, password_for_authorization):

    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*Locators.PASSWORD_RECOVERY_XPATH).click()

    wait = WebDriverWait(driver, 3)
    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/forgot-password"))

    driver.find_element(*Locators.OPEN_LOGIN_PAGE_LINK_XPATH).click()

    driver.find_element(*Locators.EMAIL_INPUT_XPATH).send_keys(email_for_authorization)
    driver.find_element(*Locators.PASSWORD_INPUT_XPATH).send_keys(password_for_authorization)
    driver.find_element(*Locators.LOGIN_BUTTON_XPATH).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON_TEXT_XPATH))

    assert driver.find_element(*Locators.ORDER_BUTTON_TEXT_XPATH).text == 'Оформить заказ'

