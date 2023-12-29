import time

from selenium import webdriver

from pages.searchPage import SearchPage

# setting browser driver:
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.mytinytodo.net/demo/")


# Running tests:
search = SearchPage(driver)
search.search_results("advanced")








input("Type any key to end the run -> ")
