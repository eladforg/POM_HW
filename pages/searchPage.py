import time

from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class SearchPage(BasePage):

    ALL_TASKS_BUFFER = (By.ID, "list_all")
    SEARCH_INPUT = (By.ID, "search")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "#tasklist>li")

    def __init__(self, driver):
        super().__init__(driver)


    def search_results(self, search_text):
        self.clicking(self.ALL_TASKS_BUFFER)
        self.fill_text(self.SEARCH_INPUT, search_text)
        time.sleep(3)
        self.return_elements(self.SEARCH_RESULTS)