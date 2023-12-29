import time

from selenium.webdriver.common.by import By

from pages.basePage import BasePage
from pages.tasksPage import TasksPage


class NewListPage(BasePage):

    NEW_LIST_BTN = (By.CSS_SELECTOR, ".mtt-tabs-new-button")
    NEW_LIST_NAME_INPUT = (By.ID, "modalTextInput")
    NEW_LIST_NAME_APPRV_BTN = (By.ID, "btnModalOk")
    TASKS_LIST_BAR = (By.CSS_SELECTOR, ".mtt-tabs.ui-sortable>li")
    TASK_INPUT = (By.ID, "task")
    SUBMIT_TASK_BTN = (By.ID, "newtask_submit")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "#tasklist>li")

    def __init__(self, driver):
        super().__init__(driver)


    def add_new_list(self, new_list_name):
        self.clicking(self.NEW_LIST_BTN)
        self.fill_text(self.NEW_LIST_NAME_INPUT, new_list_name)
        self.clicking(self.NEW_LIST_NAME_APPRV_BTN)
        time.sleep(1)
        NEW_LIST_NAME = (By.CSS_SELECTOR, f"[title='{new_list_name}']")
        self.clicking(NEW_LIST_NAME)
        # time.sleep(1)
        # self.driver.find_element(By.CSS_SELECTOR, f"[title='{new_list_name}']").click()

    def add_task_to_list(self, task_text):
        self.fill_text(self.TASK_INPUT, task_text)
        self.clicking(self.SUBMIT_TASK_BTN)
        time.sleep(1)
        # self.return_elements(self.SEARCH_RESULTS)

    def check_results(self):
        return self.return_elements(self.SEARCH_RESULTS)








