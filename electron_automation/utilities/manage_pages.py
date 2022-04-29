
# electron objects
from electron_automation.test_cases import conftest as conf
from page_objects.electron_obj.task_page import TaskPage

electron_task = None

class ManagePages:


    @staticmethod
    def init_electron_pages():
        globals()['electron_task'] = TaskPage(conf.driver)