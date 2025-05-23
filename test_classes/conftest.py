import pytest

from selenium import webdriver
from utility_files.read_properties import ReadConfig

"""
@pytest.fixture
def open_browser():
    driver = webdriver.Chrome()
    return driver
"""

# Rewritten Version of fixture for multiple browser so commenting out above fixture
@pytest.fixture
def open_browser(browser):
    if browser == "chrome" or browser == "Chrome":
        driver = webdriver.Chrome()
        # return driver
    elif browser == "edge" or browser == "Edge":
        driver = webdriver.Edge()
        # return  driver
    elif browser == "firefox" or browser == "Firefox":
        driver = webdriver.Firefox()
        # return driver
    else:
        raise ValueError("Unsupported browser: {browser}")

    driver.get(ReadConfig.getURL())
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

# Use to get browser name from command - line & pass value browser to openbrowser fixture
@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

# To set default value of browser
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="provide browser name - chrome, firefox, edge, etc")

###-----Html Report-----####
# It is hook for adding environment info into Report (customize info in report)
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata['Project Name'] = 'Swag Labs'
    metadata['Module Name'] = 'Login'
    metadata['Tester Name'] = 'Amar Patil'
