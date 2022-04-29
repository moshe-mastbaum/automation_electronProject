import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET

from electron_automation.test_cases import conftest as conf


def change_window(self, num):
    chwnd = self.driver.window_handles[num]
    self.driver.switch_to.window(chwnd)

def scrollto(self):
    self.driver.execute_script("window.scrollTo(0,500)")

def get_timestamp():
    return time.time()

def clickjs(self, elem):
    self.driver.execute_script("arguments[0].click();" ,elem)

def sett(self, element):
    # self.driver.execute_script("arguments[0].setAttribute('value',arguments[1])",element, value)
    self.driver.execute_script('element.value="12/03/2021";')

def get_data(node_name):
    # root = ET.parse('/automation_project_boi/configuration/data.xml')
    root = ET.parse('/electronProject/configuration/data.xml')
    return root.find('.//'+node_name).text

def wait (for_element, elem):
    if for_element == 'element_exists':
        WebDriverWait(conf.driver, 5).until(EC.presence_of_element_located((elem[0],elem[1])))
    if for_element == 'element_displayed':
        WebDriverWait(conf.driver, 5).until(EC.visibility_of_element_located((elem[0],elem[1])))

# Enum for selecting displayed element or exist element, for wait method
class For:
    ELEMENT_EXISTS = 'element_exists'
    ELEMENT_DISPLEYED = 'element_displayed'