import time
import allure
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from electron_automation.utilities.common_ops import get_data, get_timestamp

driver = None
action = None


@pytest.fixture(scope='class')
def init_elctron_driver(request):
    edriver = get_electron_driver()
    globals()['driver']= edriver
    driver=globals()['driver']
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    driver.implicitly_wait(int(get_data('WaitTime')))

    yield
    driver.quit()

def get_electron_driver():
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data('ElectronApp')
    driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data('ElectronDriver'))
    return driver

def pytest_exception_interact(node, call, report):
    image = "/electronProject/allure-screen-shots/screen"+str(get_timestamp())+'.png'
    if globals()['driver']:
        globals()['driver'].get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)