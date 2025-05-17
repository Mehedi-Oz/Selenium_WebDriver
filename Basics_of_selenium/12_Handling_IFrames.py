import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/iframe")
time.sleep(1)

popup = browser.find_element(By.CSS_SELECTOR, "path[d='M17.3 8.2L13.4 12l3.9 3.8a1 1 0 01-1.5 1.5L12 13.4l-3.8 3.9a1 1 0 01-1.5-1.5l3.9-3.8-3.9-3.8a1 1 0 011.5-1.5l3.8 3.9 3.8-3.9a1 1 0 011.5 1.5z']").click()
time.sleep(1)

iFrame = browser.find_element(By.ID, "mce_0_ifr")
browser.switch_to.frame(iFrame)

text_editor = browser.find_element(By.ID, "tinymce")
text_editor.clear()
text_editor.send_keys("RDR")
time.sleep(1)

browser.switch_to.default_content()  #to get out of the iframe to the main window




browser.quit()