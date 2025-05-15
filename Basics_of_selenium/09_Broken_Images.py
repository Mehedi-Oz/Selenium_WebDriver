from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/broken_images")
browser.maximize_window()

all_images = browser.find_elements(By.TAG_NAME, "img")

# for image in all_images:
#     src = image.get_attribute("src")
#     response = requests.get(src)
#
#     if response.status_code != 200:
#         print(f"Broken Image: {image.get_attribute('src')} | Status code: {response.status_code}")
#
# browser.quit()

broken_images = []

for image in all_images:
    src = image.get_attribute("src")
    response = requests.get(src)

    if response.status_code != 200:
        broken_images.append(src)

for image in broken_images:
    print(f"Broken image: {image}")

browser.quit()
