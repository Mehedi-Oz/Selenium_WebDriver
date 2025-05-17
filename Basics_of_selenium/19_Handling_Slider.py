from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/horizontal_slider")

slider = browser.find_element(By.XPATH, "//input[@type='range']")
action = ActionChains(browser)

action.click_and_hold(slider).move_by_offset(100, 0).release().perform()
time.sleep(1)

browser.quit()