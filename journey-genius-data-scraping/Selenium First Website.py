from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup as BS

# Specify the path to the ChromeDriver executable
chromedriver_path = "C:/Program Files (x86)/chromedriver-win64/chromedriver.exe"

# Create a ChromeOptions object
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "c:\Program Files\Google\Chrome Beta\Application\chrome.exe"

# Set the path to the ChromeDriver executable
chrome_options.add_argument(f"webdriver.chrome.driver={chromedriver_path}")

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Get the desired URL
driver.get("https://www.sftravel.com/article/28-things-not-to-miss-san-francisco")


# Locate all <h2> elements with class "h3"
activity_options = driver.find_elements(By.CLASS_NAME, "h3")

# Get the text content of each element
activities_text = [activity.text for activity in activity_options]

# Quit the WebDriver
driver.quit()

# Print the extracted text for all matching elements
for text in activities_text:
    print(text)