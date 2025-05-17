from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demo.automationtesting.in/Datepicker.html")

browser.find_element(By.ID, "datepicker2").click()

next_date = datetime.now() + timedelta(days=1)
next_month_year = f"{next_date.month}/{next_date.year}"

month_dropdown = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "select[title='Change the month']")
    )
)
Select(month_dropdown).select_by_value(next_month_year)

year_dropdown = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "select[title='Change the year']"))
)
Select(year_dropdown).select_by_value(f"{next_date.month}/{next_date.year}")

WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.LINK_TEXT, str(next_date.day)))
).click()

time.sleep(1)
browser.quit()
