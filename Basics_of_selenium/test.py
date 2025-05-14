from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button").click()

assert "Products" in driver.page_source

driver.quit()
