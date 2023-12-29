import time

from selenium import webdriver

from pages.tasksPage import TasksPage

# setting browser driver:
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.mytinytodo.net/demo/")


# Running tests:
# creating page object:
task_page = TasksPage(driver)
# adding a simple task:
task_page.add_simple_task("Testing task")




input("Type any key to end the run -> ")
