from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class AdvancedTaskPage(BasePage):
    TODO_BUFFER = (By.ID, "list_1")
    NEW_TASK_BTN = (By.ID, "newtask_adv")
    PRIORITY_BTN = (By.CSS_SELECTOR, "[name='prio']")  # select
    DUE_DATE_INPUT = (By.ID, "duedate")  # format 29.12.2023
    TASK_HEADER = (By.CSS_SELECTOR, ".form-row>[name='task']")
    TASK_BODY = (By.CSS_SELECTOR, "[name='note']")
    TAGS = (By.ID, "edittags")
    SAVE_BTN = (By.CSS_SELECTOR, ".form-row.form-bottom-buttons > [type='submit']")
    CANCEL_BTN = (By.CSS_SELECTOR, ".form-row.form-bottom-buttons > .mtt-back-button")

    def __init__(self, driver):
        super().__init__(driver)

    def add_task(self, task_header: str, task_body: str, priority: str, date: str, tags=None):
        self.clicking(self.TODO_BUFFER)
        self.clicking(self.NEW_TASK_BTN)
        self.fill_text(self.TASK_HEADER, task_header)
        self.fill_text(self.TASK_BODY, task_body)
        self.convert_to_select_object(self.PRIORITY_BTN, priority)
        self.fill_text(self.DUE_DATE_INPUT, date)
        self.fill_text(self.TAGS, tags)
        self.clicking(self.SAVE_BTN)
