from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://ultimateqa.com/simple-html-elements-for-automation/')
browser.maximize_window()
time.sleep(2)

browser.execute_script("window.scrollTo(0, 1000);")
checkboxes = browser.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.click()
    time.sleep(2)

checked_count = 0
expected_checkboxes_count = 3

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count += 1

if checked_count == expected_checkboxes_count:
    print("Checked count varified, Success!", )
else:
    print("Checked count mismatch, Failed!", )

browser.close()
