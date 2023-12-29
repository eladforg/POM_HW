import pytest
import self

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.newListPage import NewListPage


# option 1: creating the driver and page object outside the class
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://www.mytinytodo.net/demo/")
#
# new_list1 = NewListPage(driver)


class TestsOfNewList:

    # option 2: creating the driver and page object within the class
    # notice that at this case we'll need to add self before the new_list1 within the methods

    # setting browser driver:
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.get("http://www.mytinytodo.net/demo/")
    # new_list1 = NewListPage(self.driver)

    # option 3: with Decorator - creating the driver and page object within the class as a setup function
    # @pytest.fixture(scope="function", autouse=True)
    # def setup(self):
        # setting browser driver:
        # global driver
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        # driver.get("http://www.mytinytodo.net/demo/")

    # with decorator (option 3) it's better to outsource the setup function to conftest file.


    def test_set_driver(self):
        global new_list1
        new_list1 = NewListPage(self.driver)

    # running tests:
    def test_1(self):

        # self.new_list1.add_new_list("clothes shopping")
        new_list1.add_new_list("clothes shopping")
        new_list1.add_task_to_list("buy shirt")
        new_list1.add_task_to_list("buy pants")
        assert new_list1.check_results() > 0, "The tasks in the list should NOT be empty"


    def test_2(self):

        # self.new_list1.add_new_list("clothes shopping")
        new_list1.add_new_list("food shopping")
        new_list1.add_task_to_list("buy bread")
        new_list1.add_task_to_list("buy water")
        assert new_list1.check_results() > 0, "The tasks in the list should NOT be empty"

# input("Type eny key to end the run -> ")
