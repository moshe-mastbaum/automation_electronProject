from selenium.webdriver.common.by import By

create = (By.XPATH,  "/html/body/div/div[1]/div[2]/input")
tasks = (By.XPATH,          "/html/body/div/div[1]/div[4]/div[2]/div/div/div/div")
units_in_task = (By.XPATH,  "/html/body/div/div[1]/div[4]/div[2]/div/div/div/div/*")
complete_tasks = (By.XPATH, "//label[@class='label_5i8SP completed_bHv-Q']")
toggle_panel = (By.XPATH, "//div[@class='toggleVisibilityPanel_hNPyc']")
button = (By.XPATH, "//button")


class TaskPage:
    def __init__(self, driver):
        self.driver = driver

    def create(self):
        return self.driver.find_element(create[0], create[1])
    def tasks(self):
        return self.driver.find_elements(tasks[0], tasks[1])
    def complete_tasks(self):
        return self.driver.find_elements(complete_tasks[0], complete_tasks[1])
    def toggle_panel(self):
        return self.driver.find_element(toggle_panel[0], toggle_panel[1])
    def button(self):
        return self.driver.find_elements(button[0], button[1])

    def units_in_task(self):
        return self.driver.find_elements(units_in_task[0], units_in_task[1])

    # def ebtn(self):
    #     return self.driver.find_element(ebtn[0], ebtn[1])
