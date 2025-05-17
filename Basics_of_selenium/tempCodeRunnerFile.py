from selenium import webdriver
import csv
import time
from selenium.webdriver.common.by import By

csv_file = "C:/GITHUB/Selenium_WebDriver/Basics_of_selenium/authentication.csv"

test_data = []


with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        test_data.append(row)

print(test_data)

for data in test_data:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://www.saucedemo.com/")
    time.sleep(1)

    browser.find_element(By.ID, "user-name").send_keys(data["username"])
    browser.find_element(By.ID, "password").send_keys(data["password"])
    browser.find_element(By.ID, "login-button").click()
    time.sleep(1)

    browser.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    browser.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(1)
    
    browser.quit()
