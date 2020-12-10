from selenium.webdriver.common.by import By
from App.BaseApp import BasePage
import time
from selenium.webdriver.remote.file_detector import LocalFileDetector

class ProfilePageLoginLokators:
    LOCATOR_ATTACH_FAVICON = (By.XPATH, '//*[@id="profile"]/div[1]/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div[1]/div/label/span[1]')

    ICON_PATH = "/Users/alexradchenko/Downloads/krest.jpeg"
    LOCATOR_PROFILE_SAFE = (By.XPATH, "//*[contains(text(), 'Сохранить')]")

class ProfileHelper(BasePage):

    def new_icon(self):
        time.sleep(30)
        self.find_element(ProfilePageLoginLokators.LOCATOR_ATTACH_FAVICON).send_keys(ProfilePageLoginLokators.ICON_PATH)
        time.sleep(3)


    def profile_safe(self):
        return self.find_element(ProfilePageLoginLokators.LOCATOR_PROFILE_SAFE).click()
