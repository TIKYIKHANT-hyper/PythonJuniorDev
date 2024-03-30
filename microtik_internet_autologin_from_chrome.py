from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#Note the following scripts doesn't include tokens , if required please add your own.
#This python script is tested on chrome browser Version 123.0.6312.86 (Official Build) (64-bit) Wins and uses chrome driver from official drive https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.86/win64/chromedriver-win64.zip,
#add chromedriver to path
#requires selenium library.
#logout other login tabs of the same site first otherwise it will rise errors
#created by Ti Kyi Khant (Kaung Thant Hein)
driver = webdriver.Chrome()

#Enter your creditials Here!

URL = "" #enter your URL here
username = ""#enter your username
password = ""#enter your password , this will take as string format which can further utlized to html format encoding
def login(username, password):

    driver.get(URL)
    time.sleep(2)  # Wait for the page to load

    # Find username and password input fields and submit button
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    submit_button  = driver.find_element(By.XPATH, "//input[@type='submit']")

    # Enter login credentials and submit the form
    username_input.send_keys(username)
    password_input.send_keys(password)
    submit_button.click()

    time.sleep(5)

# Call the login function
login(username, password)

# to keep the session alive
while True:
    current_url = driver.current_url
    if current_url != URL:
        print("Session is active")
    else:
        print("Session expired. Re-login required.")
        login(username, password)  # Re-login if session expired

    time.sleep(300)  # Check session status every 5 minutes