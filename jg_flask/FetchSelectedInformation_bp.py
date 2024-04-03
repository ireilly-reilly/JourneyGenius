from flask import Blueprint, jsonify, request
import requests
import pandas as pd
import os

# Define description blueprint
FetchSelectedInformation_bp = Blueprint('FetchSelectedInformation_bp', __name__)

# Define route to handle description request
@FetchSelectedInformation_bp.route('/process_data', methods=['POST'])

# Function to fetch restaurants from Flask API
def process_data():
    try:
        # Extract data received from Vue.js
        data = request.json

        # Extract relevant variables from the data
        # These variables will differ for each type of place

        # activities = data.get('activities')
        # landmarks = data.get('landmarks')
        foods = data.get('foods')
        # shops = data.get('shops')
        # hotels = data.get('hotels')
        # datesData = data.get('datesData')
        # budget = data.get('budget')
        # stateData = data.get('stateData')
        # city = data.get('city')
        # lat = data.get('lat')
        # long = data.get('long')
        # cityDescription = data.get('cityDescription')
        # citySlogan = data.get('citySlogan')


        # print("Received data:")
        # print("Activities:", activities)
        # print("Landmarks:", landmarks)
        # print("Foods:", foods)
        # print("Shops:", shops)
        # print("Hotels:", hotels)
        # print("Dates Data:", datesData)
        # print("Budget:", budget)
        # print("State Data:", stateData)
        # print("City:", city)
        # print("Latitude:", lat)
        # print("Longitude:", long)
        # print("City Description:", cityDescription)
        # print("City Slogan:", citySlogan)

        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
        restaurant_csv_file_path = os.path.join(CSV_FOLDER, 'restaurant_data.csv')

        df = pd.read_csv(restaurant_csv_file_path, encoding='utf-8') 

        for food in foods:
            subset = df.loc[df['Place'] == food, ['Latitude', 'Longitude']]

            locations = []
            for index, row in subset.iterrows():
                latitude = float(row['Latitude'])
                longitude = float(row['Longitude'])
                locations.append({'latitude': latitude, 'longitude': longitude})

        response_data = {
            'message': 'Location data retrieved successfully',
            'locations': locations
        }

        return jsonify(response_data), 200

    except Exception as e:
        # Handle any errors that occur during processing
        error_message = str(e)  # Convert the exception to a string
        print("Error processing data:", error_message)
        return jsonify({'error': 'An error occurred while processing the data', 'message': error_message})



############################################# MODIFIED SHIT BELOW   :D ####################################################################


from flask import Blueprint, jsonify, request
import requests
import pandas as pd
import os
import googlemaps
from googlemaps.exceptions import ApiError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the GMAPS API key from the environment
api_key = os.getenv("GMAPS_api_key")

# Define our Client
gmaps = googlemaps.Client(key=api_key)


# Define description blueprint
FetchSelectedInformation_bp = Blueprint('FetchSelectedInformation_bp', __name__)

# Define route to handle description request
@FetchSelectedInformation_bp.route('/process_data', methods=['POST'])
def process_data():
    try:
        data = request.json
        foods = data.get('foods')

        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
        restaurant_csv_file_path = os.path.join(CSV_FOLDER, 'restaurant_data.csv')

        df = pd.read_csv(restaurant_csv_file_path, encoding='utf-8') 

        locations = []
        for food in foods:
            subset = df.loc[df['Place'] == food, ['Latitude', 'Longitude']]

            for index, row in subset.iterrows():
                latitude = float(row['Latitude'])
                longitude = float(row['Longitude'])
                locations.append({'latitude': latitude, 'longitude': longitude})

        photo_urls = []
        for location in locations:
            latitude = location['latitude']
            longitude = location['longitude']
            photo_url = fetch_single_photo(latitude, longitude)
            photo_urls.append(photo_url)

        response_data = {
            'message': 'Location data and photo URLs retrieved successfully',
            'locations': locations,
            'photo_urls': photo_urls
        }

        return jsonify(response_data), 200

    except Exception as e:
        error_message = str(e)
        print("Error processing data:", error_message)
        return jsonify({'error': 'An error occurred while processing the data', 'message': error_message})

def fetch_single_photo(latitude, longitude):
    try:
        nearby_search_results = gmaps.places_nearby(location=(latitude, longitude), radius=15)
        if nearby_search_results['results']:
            place_id = nearby_search_results['results'][0]['place_id']
            place_details = gmaps.place(place_id)
            if 'photos' in place_details['result']:
                photo_reference = place_details['result']['photos'][0]['photo_reference']
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"
                
                return photo_url
            else:
                return None
        else:
            return None
    except ApiError as e:
        print(f"Error fetching photo: {e}")
        return None
