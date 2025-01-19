from fileinput import filename

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime
import os

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser...")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser...")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome Browser...")
    return driver

### pytest HTML report ###

def pytest_configure(config):
    config.metadata['Project Name'] = 'OpenCart'
    config.metadata['Module Name'] = 'CustRegistration'
    config.metadata['Tester'] = 'Michael'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
    #config.option.htmlpath = filename("..\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html")






