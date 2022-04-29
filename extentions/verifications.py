import allure
from selenium.webdriver.remote.webelement import WebElement


class Verifications:
    @staticmethod
    @allure.step('verify equals')
    def verify_equals(actual, expected):
        assert str(actual) == expected, 'actual is: '+str(actual)+', but expected is: '+str(expected)

    @staticmethod
    @allure.step('is displayed')
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), 'no :'+elem.text