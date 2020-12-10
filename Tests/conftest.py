import pytest
from selenium import webdriver
from App.browsers import chrome, firefox, opera
from App.remote_driver import ip_selenoid_mac, ip_selenoid_serv

debug = True

t_out = 30


def pytest_addoption(parser):
    parser.addoption('--selenoid', action='store', default='mac',
                     help="Choose selenoid type: serv or mac")
    parser.addoption('--br_type', action='store', default='chrome',
                     help="Choose br_type type: chrome, firefox or opera")


@pytest.fixture(scope="function")
def browser(request):
    br_type = request.config.getoption("br_type")
    if br_type == "chrome":
        capabilities = chrome
    elif br_type == "firefox":
        capabilities = firefox
    elif br_type == "opera":
        capabilities = opera
    else:
        raise pytest.UsageError("--br_type Choose should be chrome, firefox or opera")

    selenoid = request.config.getoption("selenoid")
    if selenoid == "serv":
        browser = webdriver.Remote(
            command_executor=ip_selenoid_serv,
            desired_capabilities=capabilities)
    elif selenoid == "mac":
        browser = webdriver.Remote(
            command_executor=ip_selenoid_mac,
            desired_capabilities=capabilities)
    else:
        raise pytest.UsageError("--selenoid should be mac or serv")

    browser.maximize_window()
    browser.implicitly_wait(t_out)
    yield browser
    browser.quit()
