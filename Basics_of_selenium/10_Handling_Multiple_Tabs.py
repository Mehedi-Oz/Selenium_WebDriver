import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.selenium.dev/")

browser.switch_to.new_window()
browser.get("https://www.selenium.dev/documentation/webdriver/")
time.sleep(1)

# number_of_tabs = len(browser.window_handles)
# print(f"Number of tabs: {number_of_tabs}")

# tabs_value = browser.window_handles
# print(f"Tab values: {tabs_value}")

current_tab = browser.current_window_handle

browser.find_element(By.CSS_SELECTOR, "a[href='https://www.w3.org/TR/webdriver1/']").click()
time.sleep(1)

first_tab = browser.window_handles[0]

if current_tab != first_tab:
    browser.switch_to.window(first_tab)

browser.find_element(By.XPATH, "//span[normalize-space()='Downloads']").click()
time.sleep(1)

browser.quit()
