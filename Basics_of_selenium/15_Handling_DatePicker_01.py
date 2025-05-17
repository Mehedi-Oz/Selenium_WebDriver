from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.globalsqa.com/demo-site/datepicker/")
time.sleep(1)

popup = browser.find_element(By.CLASS_NAME, "close_img").click()
time.sleep(1)

date_picker_frame = browser.find_element(
    By.XPATH,
    "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame lazyloaded']",
)
browser.switch_to.frame(date_picker_frame)
time.sleep(1)

date_box = browser.find_element(By.CSS_SELECTOR, "#datepicker").click()

current_date = datetime.now()
next_date = current_date + timedelta(days=0)

formatted_date = next_date.strftime("%m/%d/%y")
selecting_date = browser.find_element(By.CSS_SELECTOR, "#datepicker").send_keys(
    formatted_date + Keys.TAB
)

time.sleep(1)

browser.quit()
