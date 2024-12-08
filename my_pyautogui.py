import pyautogui

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

import cv2 as cv
import numpy

# Path to ChromeDriver executable
chrome_driver_path = r"C:\Users\edsan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Create a Service object
chrome_service = Service(chrome_driver_path)

# Create the Chrome WebDriver instance
chrome_driver = webdriver.Chrome(service=chrome_service)

# Open a test website
# chrome_driver.get("https://www.google.com")
# print("Title of the page is:", chrome_driver.title)
# time.sleep(10)



url = 'https://my.precisionnutrition.com/users/sign_in'
# Step 1: Open the login page
chrome_driver.get(url)
chrome_driver.maximize_window()




# Step 3: Input login credentials
user_id = chrome_driver.find_element(By.ID, "user_email")
# Replace with actual username
user_id.send_keys("barbara_hessel@drhesselmd.com")

password = chrome_driver.find_element(By.ID, "user_password")
password.send_keys("Bruce!!20")  # Replace with actual password

login_button = chrome_driver.find_element(
    By.XPATH, '//*[@id="new_user"]/div[3]/input')
# # click on the continue button
login_button.click()
time.sleep(2)

# # Click the link

calculator_url='https://www.precisionnutrition.com/professional-calculator'
chrome_driver.get(calculator_url)
time.sleep(3)
# # # Wait for the new window or tab to open
# print("Waiting for the calculator page to load...")


# Enter text after focusing the field

# x,y=pyautogui.position()



# sleep(13)  # Optional delay to observe the final state
# driver.quit()

# try:
#     while True:
#         x,y=pyautogui.position()
#         print(f"x: {x} y:{y}")
# except KeyboardInterrupt:
#     print("\nTracking stopped.")
# Close the browser
pyautogui.moveTo(1039,1051,duration=.1)
pyautogui.click()
time.sleep(1)
pyautogui.write("Ed")
print(pyautogui.position())
time.sleep(20)

chrome_driver.quit()
# print(pyautogui.size())