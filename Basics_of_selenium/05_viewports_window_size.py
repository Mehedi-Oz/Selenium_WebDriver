from selenium import webdriver
import time

viewports = [(1920, 1080), (1920, 720), (360, 560), (414, 900)]
driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    for width, height in viewports:
        driver.set_window_size(width, height)
        time.sleep(2)

finally:
    driver.close()
