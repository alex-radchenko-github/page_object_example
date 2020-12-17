import allure
import pytest
from App import accounts
from Pages.MainPageLogin import MainPageHelper

@allure.feature("login")
@allure.title("login_from_main_page")
@pytest.mark.smoke
def test_login_from_main_page(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    main_page.full_login(accounts.acc["radwexe"])
    main_page.login_check()

@allure.feature('login')
@allure.title("login_from_token")
@pytest.mark.smoke
def test_login_from_token(browser):
    test_login_from_token = MainPageHelper(browser)
    test_login_from_token.go_to_site_through_token()
    test_login_from_token.login_check()

@allure.feature("login11")
@allure.title("login_from_main_page11")
@pytest.mark.smoke
def test_login_from_main_pag11(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    main_page.full_login(accounts.acc["radwexe"])
    main_page.login_check()

@allure.feature('login22')
@allure.title("login_from_token22")
@pytest.mark.smoke
def test_login_from_token22(browser):
    test_login_from_token = MainPageHelper(browser)
    test_login_from_token.go_to_site_through_token()
    test_login_from_token.login_check()

@allure.feature("login33")
@allure.title("login_from_main_page33")
@pytest.mark.smoke
def test_login_from_main_pag33(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    main_page.full_login(accounts.acc["radwexe"])
    main_page.login_check()

@allure.feature('login44')
@allure.title("login_from_token44")
@pytest.mark.smoke
def test_login_from_token44(browser):
    test_login_from_token = MainPageHelper(browser)
    test_login_from_token.go_to_site_through_token()
    test_login_from_token.login_check()

@allure.feature("login55")
@allure.title("login_from_main_page55")
@pytest.mark.smoke
def test_login_from_main_pag55(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    main_page.full_login(accounts.acc["radwexe"])
    main_page.login_check()

@allure.feature('login66')
@allure.title("login_from_token66")
@pytest.mark.smoke
def test_login_from_token66(browser):
    test_login_from_token = MainPageHelper(browser)
    test_login_from_token.go_to_site_through_token()
    test_login_from_token.login_check()
