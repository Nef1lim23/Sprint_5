from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
from helper import DataGeneration


class TestAuthorization:
    def test_authorization_through_personal_account_true(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locators.SUBMIT_LOGIN_BUTTON_XPATH))

        driver.find_element(*locators.PERSONAL_CABINET_BUTTON_XPATH).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.ENTRY_FORM_XPATH))

        driver.find_element(*locators.EMAIL_INPUT_XPATH).send_keys(DataGeneration.email_for_authorization())
        driver.find_element(*locators.PASSWORD_INPUT_XPATH).send_keys(DataGeneration.password_for_authorization())
        driver.find_element(*locators.LOGIN_BUTTON_XPATH).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.ORDER_BUTTON_TEXT_XPATH))

        assert driver.find_element(*locators.ORDER_BUTTON_TEXT_XPATH).text == 'Оформить заказ'

    def test_authorization_through_home_page_true(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locators.SUBMIT_LOGIN_BUTTON_XPATH))

        driver.find_element(*locators.SUBMIT_LOGIN_BUTTON_XPATH).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.ENTRY_FORM_XPATH))

        driver.find_element(*locators.EMAIL_INPUT_XPATH).send_keys(DataGeneration.email_for_authorization())
        driver.find_element(*locators.PASSWORD_INPUT_XPATH).send_keys(DataGeneration.password_for_authorization())
        driver.find_element(*locators.LOGIN_BUTTON_XPATH).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.ORDER_BUTTON_TEXT_XPATH))

        assert driver.find_element(*locators.ORDER_BUTTON_TEXT_XPATH).text == 'Оформить заказ'

    def test_authorization_through_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locators.BUTTON_REGISTRATION_XPATH))

        driver.find_element(*locators.OPEN_LOGIN_PAGE_LINK_XPATH).click()

        driver.find_element(*locators.EMAIL_INPUT_XPATH).send_keys(DataGeneration.email_for_authorization())
        driver.find_element(*locators.PASSWORD_INPUT_XPATH).send_keys(DataGeneration.password_for_authorization())
        driver.find_element(*locators.LOGIN_BUTTON_XPATH).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.ORDER_BUTTON_TEXT_XPATH))

        assert driver.find_element(*locators.ORDER_BUTTON_TEXT_XPATH).text == 'Оформить заказ'

    def test_authorization_through_password_recovery_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*locators.PASSWORD_RECOVERY_XPATH).click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/forgot-password"))

        driver.find_element(*locators.OPEN_LOGIN_PAGE_LINK_XPATH).click()

        driver.find_element(*locators.EMAIL_INPUT_XPATH).send_keys(DataGeneration.email_for_authorization())
        driver.find_element(*locators.PASSWORD_INPUT_XPATH).send_keys(DataGeneration.password_for_authorization())
        driver.find_element(*locators.LOGIN_BUTTON_XPATH).click()

        wait.until(EC.visibility_of_element_located(locators.ORDER_BUTTON_TEXT_XPATH))

        assert driver.find_element(*locators.ORDER_BUTTON_TEXT_XPATH).text == 'Оформить заказ'
