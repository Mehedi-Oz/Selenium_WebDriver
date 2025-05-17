from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://www.saucedemo.com/")

browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("secret_sauce")
browser.find_element(By.ID, "login-button").click()
browser.find_element(By.ID, "react-burger-menu-btn").click()

element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))

browser.close()
