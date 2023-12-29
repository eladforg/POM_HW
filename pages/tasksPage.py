from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class TasksPage(BasePage):
    TODO_BUFFER = (By.ID, "list_1")
    TASK_INPUT = (By.ID, "task")
    SUBMIT_TASK_BTN = (By.ID, "newtask_submit")


    def __init__(self, driver):
        super().__init__(driver)

    def add_simple_task(self, task_text) -> None:
        self.clicking(self.TODO_BUFFER)
        self.fill_text(self.TASK_INPUT, task_text)
        self.clicking(self.SUBMIT_TASK_BTN)

