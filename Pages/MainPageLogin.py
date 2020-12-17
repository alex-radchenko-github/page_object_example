from selenium.webdriver.common.by import By
from App.BaseApp import BasePage
import allure


class MainPageLoginLokators:
    LOCATOR_BUTTON_LOGIN = (By.XPATH, "//span[contains(text(),'Войти')]")
    LOCATOR_EMAIL_FIELD = (By.XPATH, "//input[@name='login']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOCATOR_ENTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOCATOR_CHECK_CREATE_COURS = (By.LINK_TEXT, "Создать курс в папке")

class MainPageHelper(BasePage):

    @allure.step
    def click_on_the_yellow_button(self):
        return self.find_element(MainPageLoginLokators.LOCATOR_BUTTON_LOGIN).click()

    @allure.step
    def enter_email(self, login):
        search_field = self.find_element(MainPageLoginLokators.LOCATOR_EMAIL_FIELD)
        search_field.send_keys(login)
        return search_field

    @allure.step
    def enter_password(self, pas):
        search_field = self.find_element(MainPageLoginLokators.LOCATOR_PASSWORD_FIELD)
        search_field.send_keys(pas)
        return search_field

    @allure.step
    def click_on_the_enter_button(self):
        return self.find_element(MainPageLoginLokators.LOCATOR_ENTER_BUTTON).click()

    @allure.step
    def full_login(self, acc):
        login = acc["login"]
        pas = acc["pass"]
        self.click_on_the_yellow_button()
        self.enter_email(login)
        self.enter_password(pas)
        self.click_on_the_enter_button()

    @allure.step
    def login_check(self):
        check_el = self.find_element(MainPageLoginLokators.LOCATOR_CHECK_CREATE_COURS)
        assert check_el.is_displayed() == False

