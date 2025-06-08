from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demo.automationtesting.in/Resizable.html")

resizeable_bar = browser.find_element(
    By.CSS_SELECTOR,
    ".ui-resizable-handle.ui-resizable-se.ui-icon.ui-icon-gripsmall-diagonal-se",
)

initial_element_size = browser.find_element(By.CSS_SELECTOR, "#resizable")
initial_size = print(initial_element_size.size)
time.sleep(1)

action = ActionChains(browser)
action.click_and_hold(resizeable_bar).move_by_offset(100, 100).release().perform()
time.sleep(1)

resized_element = print(initial_element_size.size)
