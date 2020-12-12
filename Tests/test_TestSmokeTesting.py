import allure
import pytest
from App import accounts
from Pages.MainPageLogin import MainPageHelper
from Pages.ProfilePage import ProfileHelper
from selenium.webdriver.common.by import By
import time

import logging
from pytest_reportportal import RPLogger, RPLogHandler


debug = True

@allure.feature("login")
@allure.title("test_login_from_main_page_with_valid_credetials")
@pytest.mark.smoke
def test_login_from_main_page_with_valid_credetials(browser, rp_logger):
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    main_page.full_login(accounts.acc["radwexe"])
    main_page.login_check()
    """
    Description of the test case which will be sent to Report Portal
    """
    rp_logger.info("Case1. Step1")


@allure.feature('login')
@allure.title("login_from_token")
@pytest.mark.smoke
def test_login_from_token(browser, rp_logger):
    """
    Description of the test case which will be sent to Report Portal
    """
    rp_logger.info("Case1. Step1")

    login_from_token = MainPageHelper(browser)
    login_from_token.go_to_site_through_token()
    login_from_token.login_check()
