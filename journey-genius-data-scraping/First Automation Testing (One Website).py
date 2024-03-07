
############################################################

#################   PRE RENDITION   ######################

############################################################


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# import requests
# from bs4 import BeautifulSoup as BS
# import csv


# # Create Chrome options with headless mode
# # chrome_options = Options()
# # chrome_options.add_argument('--headless')

# chromedriver_path = "C:/Program Files (x86)/chromedriver-win64/chromedriver.exe"

# chrome_options = webdriver.ChromeOptions()

# chrome_options.binary_location = "c:\Program Files\Google\Chrome Beta\Application\chrome.exe"

# # Create a WebDriver object with the specified options
# driver = webdriver.Chrome(options=chrome_options, service=ChromeService(executable_path=chromedriver_path))

# # Navigate to the Google search website
# driver.get("https://www.google.com")

# # Find the search input field by name
# search_input = driver.find_element(By.NAME, "q")

# # Enter the search query
# search_input.send_keys("San Francisco Activities")

# # Submit the form (you can use Keys.RETURN instead of finding the button)
# search_input.send_keys(Keys.RETURN)

# # Wait for the search results to load
# driver.implicitly_wait(5)

# # Verify that the search results are displayed
# assert "San Francisco" in driver.page_source

# # Use WebDriverWait to wait for the presence of the fifth result link
# try:
#     fifth_result_link = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div[13]/div/div[2]/div[2]/div/div/div[3]"))
#     )
#     print("Fifth result link found")
# except Exception as e:
#     print(f"Exception: {e}")

# # Click on the fifth search result link if found
# if 'fifth_result_link' in locals():
#     fifth_result_link.click()
#     print("Clicked on the fifth result link")

# # Now you are on the clicked website
# s = driver.getCurrentUrl()

# # s initializes the html and parses it
# s = BS(driver.content, 'html.parser')

# # From here you have to go ahead and inspect the website to find the correct div id of where the information is coming from
# # In this case, the div id is 'body-copy'
# results = s.find(id='body-copy')


# # This is where the actual information is located
# # It's located in the div header, and the class is called 'h3'
# Activity = results.find_all('div', class_='h3')

# # Because BeautifulSoup is array based, you print out the desired number of the information
# # In this case, there is only one anime title, so the array is at 0
# print(Activity[0].text)

# # This is where the actual information is located
# # It's located in the div header, and the class is called 'h3'
# activities = results.find_all('div', class_='h3')

# # Create a CSV file and write the header
# csv_filename = 'activities_data.csv'
# csv_header = ['Activity']
# with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(csv_header)

#     # Write each activity to the CSV file
#     for activity in activities:
#         csv_writer.writerow([activity.text.strip()])

# # Close the browser
# driver.quit()



############################################################

#################    CSS RENDITION    ######################

############################################################

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup as BS
import csv


# """Returns the first unsponsored search result link from the given soup object using CSS selectors."""#
def get_first_unsponsored_link_css(soup):

    # CSS selector for the first unsponsored result link
    # css_selector = "div.MjjYud:first-of-type > a:not([data-adchannel]):first-of-type"

    css_selector = "div.b_results > li:nth-child(7) > div.b_title > h2 > a"


    # Find the first matching element using CSS selector
    first_unsponsored_link = soup.select_one(css_selector)

    return first_unsponsored_link





# Create a Chrome options object with headless mode enabled
chrome_options = Options()
# chrome_options.add_argument("--headless")

# Create a WebDriver object with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the Google search website
driver.get("https://www.bing.com")

# Find the search input field by name
search_input = driver.find_element(By.NAME, "q")

# Enter the search query
search_input.send_keys("San Francisco Activities")

# Submit the form
search_input.send_keys(webdriver.common.keys.Keys.RETURN)

# Wait for the search results to load
driver.implicitly_wait(5)

# Get the soup object from the Bing search results page
soup = BS(driver.page_source, "html.parser")

# Get the first search result link
first_unsponsored_link = get_first_unsponsored_link_css(soup)

# Optional debugging
print(first_unsponsored_link) 

# Click on the first search result link
first_unsponsored_link.click()

# Now you are on the clicked website
# You can continue with your code to scrape the website
s = driver.getCurrentUrl()

# s initializes the html and parses it
s = BS(driver.content, 'html.parser')

# From here you have to go ahead and inspect the website to find the correct div id of where the information is coming from
# In this case, the div id is 'body-copy'
results = s.find(id='body-copy')

# This is where the actual information is located
# It's located in the div header, and the class is called 'h3'
Activity = results.find_all('div', class_='h3')

# Because BeautifulSoup is array based, you print out the desired number of the information
# In this case, there is only one anime title, so the array is at 0
print(Activity[0].text)

# This is where the actual information is located
# It's located in the div header, and the class is called 'h3'
activities = results.find_all('div', class_='h3')

# Create a CSV file and write the header
csv_filename = 'activities_data.csv'
csv_header = ['Activity']
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_header)

    # Write each activity to the CSV file
    for activity in activities:
        csv_writer.writerow([activity.text.strip()])

# Close the browser
driver.quit()


# Try on mozilla or edge 
# Might want to find an adblocker plugin to 
# pi hole 
# COULD TAKE A TRAVEL SITE THAT YOU LIKE AND SCRAPE THAT
# COULD USE ML MODEL THAT GOES OFF DATA THAT 

# GENERATE DATA TYPE INTO CHAT GPT WITH PARAMETERS YOU CARE ABOUT
    # 3 COLUMNS , FLIGHT TIME, FLIGHT, DATE, DURATION
    # DATASET 10000 POINTS - 

    # AUTO GLUE ON IS A PACKAGE FOR RANKING DATA 
    # KAGGLE IS A DATA COMPETITION FOR ML 