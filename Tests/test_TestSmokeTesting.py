import allure
import pytest
from App import accounts
from Pages.MainPageLogin import MainPageHelper

@allure.feature("login")
@allure.title("test_login_from_main_page_with_valid_credetials")
@pytest.mark.smoke
def test_login_from_main_page_with_valid_credetials(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    main_page.full_login(accounts.acc["radwexe"])
    main_page.login_check()


@allure.feature('login')
@allure.title("login_from_token")
@pytest.mark.smoke
def test_login_from_token(browser):
    login_from_token = MainPageHelper(browser)
    login_from_token.go_to_site_through_token()
    login_from_token.login_check()

