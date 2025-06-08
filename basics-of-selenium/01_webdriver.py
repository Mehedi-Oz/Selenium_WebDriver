from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.selenium.dev/documentation/')

browser.set_window_size(1920, 1080)
browser.maximize_window()

title = browser.title
print(title)

assert 'The Selenium Browser Automation Project' in title

time.sleep(2)
browser.quit()

