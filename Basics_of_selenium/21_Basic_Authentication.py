from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

username = "admin"
password = "admin"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(2)
