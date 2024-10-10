from selenium.webdriver.support.wait import WebDriverWait
from helper import DataGeneration
import locators
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:
    def test_registration(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.ENTRY_FORM_XPATH))

        driver.find_element(*locators.NAME_INPUT_XPATH).send_keys(DataGeneration.generate_random_name(2, 12))
        driver.find_element(*locators.EMAIL_REGISTRATION_XPATH).send_keys(DataGeneration.generate_random_email(3, 10))
        driver.find_element(*locators.PASSWORD_INPUT_REGISTRATION_XPATH).send_keys(DataGeneration.generate_random_password(6, 12))
        driver.find_element(*locators.BUTTON_REGISTRATION_XPATH).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.OPEN_LOGIN_PAGE_LINK_XPATH))

        assert driver.find_element(*locators.OPEN_LOGIN_PAGE_LINK_XPATH).text == 'Войти'

    def test_registration_invalid_password(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.ENTRY_FORM_XPATH))

        driver.find_element(*locators.NAME_INPUT_XPATH).send_keys(DataGeneration.generate_random_name(2, 12))
        driver.find_element(*locators.EMAIL_REGISTRATION_XPATH).send_keys(DataGeneration.generate_random_email(3, 10))
        driver.find_element(*locators.PASSWORD_INPUT_REGISTRATION_XPATH).send_keys(DataGeneration.generate_random_password(1, 3))
        driver.find_element(*locators.BUTTON_REGISTRATION_XPATH).click()

        assert driver.find_element(*locators.MASSAGE_IS_AN_INCORRECT_PASSWORD).text == 'Некорректный пароль'