import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://cosmocode.io/automation-practice-webtable/")
browser.execute_script("window.scrollTo(0, 700)")
time.sleep(1)

table = browser.find_element(By.ID, "countries")
rows = table.find_elements(By.TAG_NAME, "tr")
row_count = len(rows) - 1
print(f"There are {row_count} rows")

target_value = "Bangladesh"

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")

    for cell in cells:
        if cell.text == target_value:
            print(f"Target value: {cell.text} is found.")
            break

browser.quit()
