import time
import allure
import pytest
from extentions.verifications import Verifications
from workfows.electron_flows import ElectronFlows


@pytest.mark.usefixtures('init_elctron_driver')
class Test_Electron:

    @allure.title('test1 add and verify task')
    @allure.description('test1 add and verify task')
    def test_add_task(self):
        ElectronFlows.add_task(self, 'task rr1')
        ElectronFlows.add_task(self, 'task rr2')
        ElectronFlows.add_task(self, 'task rr3')
        time.sleep(1)
        Verifications.verify_equals(ElectronFlows.number_of_tasks(self), '3')

    @allure.title('test2 complete task')
    @allure.description('test2 complete task')
    def test_complete_task(self):
        ElectronFlows.click_unit_in_task(self, 1, 0)
        time.sleep(2)
        Verifications.verify_equals(ElectronFlows.number_of_complete_tasks(self), '1')

    @allure.title('test3 filter')
    @allure.description('test3 filter todo tasks')
    def test_filter_task(self):
        # time.sleep(5)
        ElectronFlows.click_panel(self)
        time.sleep(1)
        Verifications.verify_equals(ElectronFlows.number_of_tasks(self), '2')

    @allure.title('test2 delete and verify task')
    @allure.description('test2 delete and verify task')
    def test_delete_task(self):
        time.sleep(1)
        ElectronFlows.click_unit_in_task(self, 4, 15)
        time.sleep(1)
        Verifications.verify_equals(ElectronFlows.number_of_tasks(self), '1')
        time.sleep(1)
