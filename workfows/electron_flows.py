import time
from selenium.webdriver.common.keys import Keys
import allure
from electron_automation.utilities import manage_pages as page
from extentions.ui_actions import UiAction

# from appium_automation.electron_automation import utilities

class ElectronFlows:
    @staticmethod
    @allure.step('add new task')
    def add_task(self, task_name):
        UiAction.text_in(page.TaskPage.create(self), task_name)
        UiAction.text_in(page.TaskPage.create(self), Keys.RETURN)


    @staticmethod
    @allure.step('tasks number')
    def number_of_tasks(self):
        return len(page.TaskPage.tasks(self))

    @staticmethod
    @allure.step('completed tasks number')
    def number_of_complete_tasks(self):
        return len(page.TaskPage.complete_tasks(self))

    @staticmethod
    @allure.step('click panel')
    def click_panel(self):
        UiAction.click(page.TaskPage.toggle_panel(self))
        time.sleep(1)
        UiAction.click(page.TaskPage.button(self)[3])

    @staticmethod
    @allure.step('click task')
    def click_unit_in_task(self, unit_num, next):
        UiAction.mouse_hover_click(page.TaskPage.units_in_task(self)[unit_num], next)
