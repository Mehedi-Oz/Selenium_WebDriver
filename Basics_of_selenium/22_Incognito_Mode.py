from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
browser.get("https://google.com")
time.sleep(2)
