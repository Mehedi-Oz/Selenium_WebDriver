import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/nested_frames")
time.sleep(1)

# Switching To First Frame
browser.switch_to.frame("frame-top")

# Switching To Middle Frame
browser.switch_to.frame("frame-middle")
content = browser.find_element(By.ID, "content").text
print(f"Content in middle frame is {content}")

# Switching Back To First Frame To Catch Another Frame
browser.switch_to.default_content()

browser.switch_to.frame("frame-bottom")
content = browser.find_element(By.TAG_NAME, "body").text
print(f"Content in bottom frame is {content}")

browser.quit()