from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://github.com/Mehedi-Oz/Selenium_WebDriver')
driver.maximize_window()
driver.implicitly_wait(5)

go_to_file = driver.find_element(By.XPATH, "//input[@placeholder='Go to file']")

try:
    go_to_file = driver.find_element(By.XPATH, "//input[@placeholder='Go to file']")

    print("Element found!")
    print("Placeholder text:", go_to_file.get_attribute('placeholder'))

except Exception as e:
    print("Element not found:", e)

finally:
    driver.quit()
