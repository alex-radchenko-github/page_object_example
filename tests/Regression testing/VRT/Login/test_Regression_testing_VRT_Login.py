import allure
import pytest
from src import accounts
from src.pages.main_page import MainPageHelper
from src.pages.login_page import LoginPageHelper
import time


@allure.testcase("https://app.qase.io/case/AT-7")
@allure.feature("main_page")
@allure.title("vrt_main_page")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_vrt_main_page_click_on_the_yellow_button(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site("/")
    main_page.click_on_the_yellow_button()
    time.sleep(3)
    main_page.screenshot_check('AT-7_test_vrt_main_page_click_on_the_yellow_button', '1920x964', 'linux','selenoid')