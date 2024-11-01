from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time

class WebAutomation:
    def __init__(self):
        # Set up Chrome options and driver service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        download_path = os.getcwd()

        preference = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', preference)

        service = Service('chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        # Open the target login page
        self.driver.get('https://demoqa.com/login')

        # Wait until the username, password fields, and login button are visible
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))

        # Enter login credentials and click login
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

        print("Login Successful!")

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Locate the Elements dropdown and Text Box
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]')))
        elements.click()
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Locate the form fields
        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'submit')))

        # Fill in the form fields
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

        print("Form Submitted!")
      time.sleep(1)

    def download(self):
        # Locate and click the "Upload and Download" section and download button
        upload_download = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
        self.driver.execute_script("arguments[0].click();", upload_download)

        download_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'downloadButton')))
        self.driver.execute_script("arguments[0].click();", download_button)

        download_path = os.getcwd()
        file_downloaded = False
        timeout = time.time() + 40  # 40-second timeout for the download to complete

        while not file_downloaded:
            for file_name in os.listdir(download_path):
                if file_name.endswith(".tmp"):
                    continue  # Wait until .tmp becomes a complete file
                elif file_name:
                    file_downloaded = True
                    print("Download Complete!")
                    break
            if time.time() > timeout:
                print("Download timed out.")
                break
            time.sleep(1)  # Short delay before checking again

    def close(self):
        self.driver.quit()



if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login('yourusername', 'yourpassword')
    webautomation.fill_form("Zuhair", "zuhair@gamil.com", "NIBM", "NIBM")
    webautomation.download()
    webautomation.close()