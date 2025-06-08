from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)

driver.close()
