import requests
from bs4 import BeautifulSoup as BS


# Put target URL in here
url = 'https://myanimelist.net/anime/17265/Log_Horizon'

# 'Requests' library will grab that URL
html = requests.get(url)



# s initializes the html and parses it
s = BS(html.content, 'html.parser')

# From here you have to go ahead and inspect the website to find the correct div id of where the information is coming from
# In this case, the div id is 'myanimelist'
results = s.find(id='myanimelist')


# This is where the actual information is located
# It's located in the div header, and the class is called 'h1-title'
animeTitle = results.find_all('div', class_='h1-title')

# Because BeautifulSoup is array based, you print out the desired number of the information
# In this case, there is only one anime title, so the array is at 0
print(animeTitle[0].text)