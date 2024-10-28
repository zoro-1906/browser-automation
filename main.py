from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.chrome(service)

