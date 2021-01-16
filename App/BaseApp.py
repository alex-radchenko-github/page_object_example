from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from App import save_token
from Tests import conftest
import allure


class BasePage:
    def __init__(self, browser):
        self.driver = browser
        self.base_url = "https://antitreningi.ru"
        self.base_url_token = "https://antitreningi.ru/account/auth?&token=" + save_token.token()

    def find_element(self, locator, time=conftest.T_OUT):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=conftest.T_OUT):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
    #go to page
    @allure.step
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step
    def go_to_site_through_token(self):

        return self.driver.get(self.base_url_token)

    @allure.step
    def switch_iframe(self, locator):
        time.sleep(3)
        return self.driver.switch_to_frame(locator)

    @allure.step
    def switch_from_iframe(self):
        return self.driver.switch_to_default_content()

    @allure.step
    def screenshot(self):
        return self.driver.get_screenshot_as_png()
