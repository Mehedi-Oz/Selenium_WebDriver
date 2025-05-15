from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

browser = webdriver.Chrome()
browser.get("https://jqueryui.com/")
browser.maximize_window()

all_links = browser.find_elements(By.TAG_NAME, "a")
print(f"Number of links found: {len(all_links)}")

for link in all_links:
    href = link.get_attribute("href")
    response = requests.get(href)

    if response.status_code >= 400:
        print(f"Broken link: {href} | Status code: {response.status_code}")

browser.quit()
