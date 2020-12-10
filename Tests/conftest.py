import pytest
from selenium import webdriver
from App.remote_driver import ip_selenoid_mac, ip_selenoid_serv
t_out = 30

def pytest_addoption(parser):
    parser.addoption('--selenoid', action='store', default='mac',
                     help="Choose selenoid type: serv or mac")


@pytest.fixture(scope="function")
def browser(request):
    br_type = request.config.getoption("br_type")
    chrome = {
        "browserName": "chrome",
        "version": "87.0",
        "enableVNC": True,
        "enableVideo": False
    }
    capabilities = chrome

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
