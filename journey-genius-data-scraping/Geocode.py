import googlemaps
import pandas as pd

# Initialize Google Maps client with your API key
gmaps = googlemaps.Client(key='AIzaSyDGC5QtIMrpN1HXPJpamkDhgfVUkq9Jw8Y')

# Read the existing CSV file into a DataFrame
data_path = 'journey-genius-data-scraping/activity_data.csv'
data = pd.read_csv(data_path, encoding='utf-8')

# Define a function to get latitude and longitude from an address
def get_lat_lng(address):
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None, None

# Apply the function to create new 'Latitude' and 'Longitude' columns
data['Latitude'], data['Longitude'] = zip(*data['Address'].apply(get_lat_lng))

# Write the updated DataFrame back to the CSV file
data.to_csv(data_path, index=False, encoding='utf-8')
