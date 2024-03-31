from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def login(username, password):

    driver.refresh()
    time.sleep(1)
    driver.get("https://internet.msfu.ru/login?")
    time.sleep(2)  # Wait for the page to load

    # Find username and password input fields and submit button
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")

    # Enter login credentials and submit the form
    username_input.send_keys(username)
    password_input.send_keys(password)
    submit_button.click()

    time.sleep(5)

# Call the login function
login('mop', "18301919")

# to keep the session alive

while True:

    current_url = driver.current_url
    if current_url == "https://internet.msfu.ru/status":
        print("Session is active")
        driver.refresh()
    else:
        print("Session expired. Re-login required.")
        driver.refresh()
        login('mop', "18301919")  # Re-login if session expired

    time.sleep(3)  # Check session status every 5 minutes