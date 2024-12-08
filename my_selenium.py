from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import my_pyautogui
import cv2 as cv
import numpy

# Path to ChromeDriver executable
chrome_driver_path = r"C:\Users\edsan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Create a Service object
chrome_service = Service(chrome_driver_path)

# Create the Chrome WebDriver instance
chrome_driver = webdriver.Chrome(service=chrome_service)

# Open a test website
chrome_driver.get("https://www.google.com")
print("Title of the page is:", chrome_driver.title)
time.sleep(10)
# Close the browser
chrome_driver.quit()

edge_driver_path=r"C:\Users\edsan\Downloads\edgedriver_win64\msedgedriver.exe"

# # Create a Service object
edge_service = Service(edge_driver_path)

# # Create the Edge WebDriver instance
edge_driver = webdriver.Edge(service=edge_service)

# # Open a website
edge_driver.get("https://www.amazon.com")
print("Page title is:", edge_driver.title)
time.sleep(10)
# # Close the browser
edge_driver.quit()

