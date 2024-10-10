from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators


class TestLogOutOfAccount:
    def test_log_out_of_account(self, driver, authorization):

        driver.find_element(*locators.PERSONAL_CABINET_BUTTON_XPATH).click()
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located(locators.PERSONAL_CABINET_FORM_MAIN_XPATH))

        driver.find_element(*locators.BUTTON_EXIT_XPATH).click()
        wait.until(EC.visibility_of_element_located(locators.LOGIN_BUTTON_XPATH))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

