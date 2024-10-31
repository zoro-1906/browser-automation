from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-sesrch-engine-choice-screen")
service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get('https://demoqa.com/login')

username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))



input("Press Enter to exit the browser")
driver.quit()