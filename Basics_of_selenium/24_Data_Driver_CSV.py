import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException as exceptions


# df = pd.read_csv("C:/AAA - PROJECTS/SELENIUM WEBDRIVER/Files/authentication.csv")
df = pd.read_csv(
    "C:/GITHUB/Selenium_WebDriver/Basics_of_selenium/Files/authentication.csv"
)

browser = webdriver.Firefox()
browser.get("https://www.saucedemo.com/")

for _, row in df.iterrows():
    try:
        username = browser.find_element(By.ID, "user-name")
        username.clear()
        password = browser.find_element(By.ID, "password")
        password.clear()
        username.send_keys(row["username"])
        password.send_keys(row["password"])
        browser.find_element(By.ID, "login-button").click()

        browser.find_element(By.ID, "react-burger-menu-btn").click()
        browser.find_element(By.ID, "logout_sidebar_link").click()

    except exceptions:
        browser.get("https://www.saucedemo.com/")


browser.quit()
