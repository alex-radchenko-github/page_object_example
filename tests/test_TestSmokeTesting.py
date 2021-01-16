import allure
import pytest
from src import accounts
from src.pages.mainpagelogin import MainPageHelper


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

@allure.epic("epic_epic")
@allure.feature('feature_feature')
@allure.story("story_story")
@allure.testcase("testcase")
@allure.issue("https://yandex.ru/", "issue")
@allure.suite("suite_suite")
@allure.description("description_description")
@allure.title("title_title")
@allure.tag("tag_UI")
@pytest.mark.smoke
def test_login_from_token11(browser):
    test_login_from_token = MainPageHelper(browser)
    test_login_from_token.go_to_site_through_token()
    test_login_from_token.login_check()
