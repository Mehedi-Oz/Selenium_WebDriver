from selenium import webdriver
import csv
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

csv_file = "C:/GITHUB/Selenium_WebDriver/Basics_of_selenium/Files/authentication.csv"

test_data = []

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append(row)

print(test_data)

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://www.saucedemo.com/")
time.sleep(1)

for data in test_data:
    try:
        browser.find_element(By.ID, "user-name").clear()
        browser.find_element(By.ID, "password").clear()
        browser.find_element(By.ID, "user-name").send_keys(data["username"])
        browser.find_element(By.ID, "password").send_keys(data["password"])
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # Check if login was successful by looking for the burger menu
        browser.find_element(By.ID, "react-burger-menu-btn")
        print(f"Login successful for user: {data['username']}")

        browser.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        browser.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(1)

    except NoSuchElementException:
        print(f"Login failed for user: {data['username']}. Skipping to next user.")
        browser.get("https://www.saucedemo.com/")
        time.sleep(1)

browser.quit()
