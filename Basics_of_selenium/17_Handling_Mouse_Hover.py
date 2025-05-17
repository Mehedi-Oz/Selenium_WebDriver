from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demo.automationtesting.in/Datepicker.html")

actions = ActionChains(browser)
hover_element = browser.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
actions.move_to_element(hover_element).perform()
time.sleep(1)

browser.find_element(By.XPATH, "//a[normalize-space()='Frames']").click()
time.sleep(1)

browser.quit()
