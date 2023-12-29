import time

from selenium import webdriver

from pages.advancedTaskPage import AdvancedTaskPage


# setting browser driver:
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.mytinytodo.net/demo/")


# Running tests:

# adding an advanced task:
advanced_task_page = AdvancedTaskPage(driver)
advanced_task_page.add_task(
    task_header= "advanced test",
    task_body= "automation test body",
    priority= "2",
    date= "31.12.2023",
    tags= "LICHI, CAT"
)
time.sleep(1)
advanced_task_page.add_task(
    task_header= "3rd test",
    task_body= "automation test body",
    priority= "0",
    date= "31.12.2023",
    tags= "test, auto"
)





input("Type any key to end the run -> ")
