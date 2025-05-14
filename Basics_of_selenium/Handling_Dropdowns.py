from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/dropdown')
browser.maximize_window()
time.sleep(1)

dropdown_elements = Select(browser.find_element(By.ID, "dropdown"))
selection_count = len(dropdown_elements.options)
time.sleep(1)

expected_count = 3

if expected_count == selection_count:
    print("success", selection_count)
else:
    print("fail", selection_count)

browser.close()
