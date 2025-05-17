from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.maximize_window()
browser.get("https://www.saucedemo.com/")

browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("secret_sauce")
browser.find_element(By.ID, "login-button").click()
browser.find_element(By.ID, "react-burger-menu-btn").click()
browser.find_element(By.ID, "logout_sidebar_link").click()

browser.close()
