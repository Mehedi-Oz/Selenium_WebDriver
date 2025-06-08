from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.maximize_window()
driver.implicitly_wait(2)

username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com"
driver.get(login_url)

username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_field.send_keys(username)
password_field.send_keys(password)
assert not login_button.get_attribute("disabled")
login_button.click()

assert "Products" in driver.page_source

driver.quit()
