import requests
import csv
import random
import time
import os
import googlemaps
from googlemaps.exceptions import ApiError
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the GMAPS API key from the environment
api_key = os.getenv("GMAPS_api_key")

# Initialize Google Maps client
gmaps = googlemaps.Client(key=api_key)


# df = pd.read_csv('restaurant_data.csv')

def fetch_single_photo(latitude, longitude):
    try:
        # Perform a nearby search based on the coordinates
        nearby_search_results = gmaps.places_nearby(location=(latitude, longitude), radius=15)
        
        # Check if any results were returned
        if nearby_search_results['results']:
            # Get the place ID of the first result
            place_id = nearby_search_results['results'][0]['place_id']
            
            # Get details of the place using the place ID
            place_details = gmaps.place(place_id)
            
            # Check if photos are available
            if 'photos' in place_details['result']:
                # Get the reference of the first photo
                photo_reference = place_details['result']['photos'][0]['photo_reference']
                
                # Construct the URL for the photo
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key=api_key"
                
                return photo_url
            else:
                return None
        else:
            return None
    except ApiError as e:
        print(f"Error fetching photo: {e}")
        return None

latitude = 39.5826834
longitude = -119.7412467

photo_url = fetch_single_photo(latitude, longitude)
if photo_url:
    print(f"Photo URL for place {photo_url}")
else:
    print(f"No photo found for place")
# # Iterate through the DataFrame and fetch photos for each place
# for index, row in df.iterrows():
#     latitude = row['Latitude']
#     longitude = row['Longitude']
#     photo_url = fetch_single_photo(latitude, longitude)
#     if photo_url:
#         print(f"Photo URL for place {index + 1}: {photo_url}")
#     else:
#         print(f"No photo found for place {index + 1}")