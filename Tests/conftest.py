import pytest
from selenium import webdriver
import App.browsers as browsers
import App.remote_driver as remote_driver


import logging
import sys
from pytest_reportportal import RPLogger, RPLogHandler


t_out = 30

def pytest_addoption(parser):
    parser.addoption('--selenoid', action='store', default='localhost',
                     help="Choose selenoid type: serv or localhost")
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
    elif selenoid == "localhost":
        browser = webdriver.Remote(
            command_executor=remote_driver.ip_selenoid_mac,
            desired_capabilities=capabilities)
    else:
        raise pytest.UsageError("--selenoid should be localhost or serv")
    browser.maximize_window()
    browser.implicitly_wait(t_out)
    yield browser
    browser.quit()

@pytest.fixture(scope="session")
def rp_logger(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # Create handler for Report Portal if the service has been
    # configured and started.
    if hasattr(request.node.config, 'py_test_service'):
        # Import Report Portal logger and handler to the test module.
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)
        # Add additional handlers if it is necessary
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)
    # Set INFO level for Report Portal handler.
    rp_handler.setLevel(logging.INFO)
    return logger
