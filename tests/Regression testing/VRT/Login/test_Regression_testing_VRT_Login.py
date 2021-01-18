import allure
import pytest
from src import accounts
from src.pages.main_page import MainPageHelper
from src.pages.login_page import LoginPageHelper
import time


@allure.testcase("https://app.qase.io/case/AT-7")
@allure.feature("login")
@allure.title("vrt_main_page_click_on_the_yellow_button")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_vrt_main_page_click_on_the_yellow_button(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site("/")
    main_page.click_on_the_yellow_button()
    time.sleep(3)
    main_page.screenshot_check('AT-7_test_vrt_main_page_click_on_the_yellow_button', '1920x964', 'linux', 'selenoid')


@allure.testcase("https://app.qase.io/case/AT-8")
@allure.feature("login")
@allure.title("vrt_main_page_modal_window_top_right_button_with_valid_credentials_before_click")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_vrt_main_page_modal_window_top_right_button_with_valid_credentials_before_click(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site("/")
    main_page.click_on_the_yellow_button()
    main_page.enter_email("radwexe@mail.ru")
    main_page.enter_password("111")
    main_page.screenshot_check('AT-8_vrt_main_page_modal_window_top_right_button_with_valid_credentials_before_click',
                               '1920x964', 'linux', 'selenoid')
