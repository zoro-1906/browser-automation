from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Set up Chrome options and driver service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options, service=service)

# Open the target login page
driver.get('https://demoqa.com/login')

# Wait until the username, password fields, and login button are visible
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))

# Enter login credentials and click login
username_field.send_keys('yourusername')
password_field.send_keys('yourpassword')
login_button.click()

# Locate the Elements dropdown and Text Box
elements = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]')))
elements.click()
text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()

# Locate the form fields
fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'email')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'submit')))

# Fill in the form fields


# Wait for user input to exit
input("Press Enter to exit the browser")
driver.quit()
