from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Locators


def test_log_out_of_account(driver, authorization):

    driver.find_element(*Locators.PERSONAL_CABINET_BUTTON_XPATH).click()
    wait = WebDriverWait(driver, 3)
    wait.until(EC.visibility_of_element_located(Locators.PERSONAL_CABINET_FORM_MAIN_XPATH))

    driver.find_element(*Locators.BUTTON_EXIT_XPATH).click()
    wait.until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_XPATH))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

