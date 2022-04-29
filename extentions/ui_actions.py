import time
from selenium.webdriver import ActionChains
import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from electron_automation.test_cases import conftest as conf

# from appium_automation.electron_automation import test_cases




class UiAction:
    @staticmethod
    @allure.step('click')
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step('update text')
    def text_in(elem: WebElement, value: str):
        # elem.clear()
        elem.send_keys(value)

    @staticmethod
    @allure.step('mouse hover')
    def mouse_hover(elem):
        conf.action.move_to_element(elem).perform()
        # test_cases.conftest.action.move_to_element(elem).perform()

    @staticmethod
    @allure.step('mouse hover and click')
    def mouse_hover_click(elem, num):
        # time.sleep(3)
        ActionChains(conf.driver).move_to_element_with_offset(elem, num, 0).click().perform()
        # time.sleep(3)

    @staticmethod
    @allure.step('select by index in dropdown')
    def select1(elem: WebElement, index):
        Select(elem).select_by_index(index)




