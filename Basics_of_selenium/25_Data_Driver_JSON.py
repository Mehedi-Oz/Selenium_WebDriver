from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import json

with open("C:/GITHUB/Selenium_WebDriver/Basics_of_selenium/authentication.json") as file:
    test_data = json.load(file)

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://www.saucedemo.com/")
time.sleep(1)

for data in test_data["users"]:
    browser.find_element(By.ID, "user-name").clear()
    browser.find_element(By.ID, "password").clear()
    browser.find_element(By.ID, "user-name").send_keys(data["username"])
    browser.find_element(By.ID, "password").send_keys(data["password"])
    browser.find_element(By.ID, "login-button").click()
    time.sleep(1)

    browser.find_element(By.ID, "react-burger-menu-btn").click()
    browser.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(1)

browser.quit()
