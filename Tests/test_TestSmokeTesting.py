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

    rp_logger.info("Case1. Step1")
    x = "this"
    rp_logger.info("x is: %s", x)
    assert 'h' in x

    # Message with an attachment.
    import subprocess
    free_memory = subprocess.check_output("free -h".split())
    rp_logger.info(
        "Case1. Memory consumption",
        attachment={
            "name": "free_memory.txt",
            "data": free_memory,
            "mime": "application/octet-stream",
        },
    )

    # This debug message will not be sent to the Report Portal.
    rp_logger.debug("Case1. Debug message")


@allure.feature('login')
@allure.title("login_from_token")
@pytest.mark.smoke
def test_login_from_token(browser, rp_logger):
    login_from_token = MainPageHelper(browser)
    login_from_token.go_to_site_through_token()
    login_from_token.login_check()

    rp_logger.info("Case1. Step1")
    x = "this"
    rp_logger.info("x is: %s", x)
    assert 'h' in x

    # Message with an attachment.
    import subprocess
    free_memory = subprocess.check_output("free -h".split())
    rp_logger.info(
        "Case1. Memory consumption",
        attachment={
            "name": "free_memory.txt",
            "data": free_memory,
            "mime": "application/octet-stream",
        },
    )

    # This debug message will not be sent to the Report Portal.
    rp_logger.debug("Case1. Debug message")

