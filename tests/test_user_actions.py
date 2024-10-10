import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators


class TestUserActions:
    def test_transfer_to_personal_account(self, driver, authorization):

        driver.find_element(*locators.PERSONAL_CABINET_BUTTON_XPATH).click()
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located(locators.PERSONAL_CABINET_FORM_MAIN_XPATH))

        assert driver.find_element(*locators.BUTTON_EXIT_XPATH).text == "Выход"

    def test_switching_from_personal_account_to_the_construct(self, driver, authorization):

        driver.find_element(*locators.PERSONAL_CABINET_BUTTON_XPATH).click()
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located(locators.PERSONAL_CABINET_FORM_MAIN_XPATH))

        driver.find_element(*locators.CONSTRUCTOR_TAB_LINK_XPATH).click()
        wait.until(EC.visibility_of_element_located(locators.CONFIRM_ORDER_BUTTON_XPATH))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_click_on_constructor_and_on_logo(self, driver, authorization):

        driver.find_element(*locators.PERSONAL_CABINET_BUTTON_XPATH).click()
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located(locators.PERSONAL_CABINET_FORM_MAIN_XPATH))

        driver.find_element(*locators.CONSTRUCTOR_TAB_LINK_XPATH).click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

        wait.until(EC.visibility_of_element_located(locators.CONFIRM_ORDER_BUTTON_XPATH))

        driver.find_element(*locators.PERSONAL_CABINET_BUTTON_XPATH).click()
        wait.until(EC.visibility_of_element_located(locators.PERSONAL_CABINET_FORM_MAIN_XPATH))

        driver.find_element(*locators.LOGO_BUTTON_XPATH).click()
        wait.until(EC.visibility_of_element_located(locators.CONFIRM_ORDER_BUTTON_XPATH))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

