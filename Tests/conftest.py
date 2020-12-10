import pytest
from selenium import webdriver
t_out = 30

def pytest_addoption(parser):
    parser.addoption('--selenoid', action='store', default='selenoid',
                     help="Choose selenoid type: serv or mac")


@pytest.fixture(scope="function")
def browser(request):
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
            command_executor="http://164.90.145.233:4444/wd/hub",
            desired_capabilities=capabilities)
    elif selenoid == "mac":
        browser = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities)
    else:
        raise pytest.UsageError("--selenoid should be mac or serv")

    browser.maximize_window()
    browser.implicitly_wait(t_out)
    yield browser
    browser.quit()
