import pytest
from selenium import webdriver
import App.browsers as browsers
import App.remote_driver as remote_driver
t_out = 30
import argparse

def pytest_addoption(parser):
    parser.addoption('--selenoid', action='store', default='selenoid',
                     help="Choose selenoid type: serv or mac")
    parser.addoption('--br_type', action='store', default='chrome',
                     help="Choose br_type type: chrome, firefox, opera, safari, MicrosoftEdge")

@pytest.fixture(scope="function")
def browser(request):
    br_type = request.config.getoption("br_type")
    if br_type == "chrome":
        capabilities = browsers.chrome
    elif br_type == "firefox":
        capabilities = browsers.firefox
    elif br_type == "opera":
        capabilities = browsers.opera
    elif br_type == "safari":
        capabilities = browsers.safari
    elif br_type == "MicrosoftEdge":
        capabilities = browsers.MicrosoftEdge
    else:
        raise pytest.UsageError("--br_type Choose should be chrome, firefox, opera, safari, MicrosoftEdge")

    selenoid = request.config.getoption("selenoid")
    if selenoid == "serv":
        browser = webdriver.Remote(
            command_executor=remote_driver.ip_selenoid_serv,
            desired_capabilities=capabilities)
    elif selenoid == "mac":
        browser = webdriver.Remote(
            command_executor=remote_driver.ip_selenoid_mac,
            desired_capabilities=capabilities)
    else:
        raise pytest.UsageError("--selenoid should be mac or serv")
    browser.maximize_window()
    browser.implicitly_wait(t_out)
    yield browser
    browser.quit()
