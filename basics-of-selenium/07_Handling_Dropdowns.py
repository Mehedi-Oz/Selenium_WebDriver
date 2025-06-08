from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/dropdown')
browser.maximize_window()
time.sleep(1)


# dropdown = browser.find_element(By.ID, "dropdown")
# select = Select(dropdown)

# select.select_by_visible_text("Option 2")
# select.select_by_value("1")
# select.select_by_index(2)


# Dropdown Counts

# dropdown_element = Select(browser.find_element(By.ID, "dropdown"))
# selection_count = len(dropdown_element.options)
# time.sleep(1)
#
# expected_count = 3
#
# if expected_count == selection_count:
#     print("success", selection_count)
# else:
#     print("fail", selection_count)
#
# browser.close()

dropdown_elements = browser.find_element(By.ID, "dropdown")
dropdown = Select(dropdown_elements)
target_value = "Option 6"

for option in dropdown.options:
    if option.text == target_value:
        option.click()
        print(f"Target Value '{target_value}' is in the dropdown")
        time.sleep(1)
    else:
        print(f"Target Value '{target_value}' is not in the dropdown")

browser.close()