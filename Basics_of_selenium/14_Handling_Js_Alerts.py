import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/javascript_alerts")

# Alert (Clicking)

JS_Alert_Button = browser.find_element(
    By.XPATH, "//button[normalize-space()='Click for JS Alert']"
)
JS_Alert_Button.click()
time.sleep(1)

alert = browser.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(1)

# Alert (Dismiss)

JS_Alert_Button = browser.find_element(
    By.XPATH, "//button[normalize-space()='Click for JS Confirm']"
)
JS_Alert_Button.click()
time.sleep(1)

alert = browser.switch_to.alert
print(alert.text)
alert.dismiss()
time.sleep(1)

# Alert (Giving input in an alert)
JS_Alert_Button = browser.find_element(
    By.XPATH, "//button[normalize-space()='Click for JS Prompt']"
)
JS_Alert_Button.click()

alert = browser.switch_to.alert
print(alert.text)
alert.send_keys("RED DEAD!")
alert.accept()
time.sleep(2)


browser.quit()
