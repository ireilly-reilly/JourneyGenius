from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
import googlemaps
from googlemaps.exceptions import ApiError
import os

# Load environment variables from .env file
load_dotenv()

# Get the Google Maps API key from the environment
api_key = os.getenv("GMAPS_api_key")

# Initialize Google Maps client
gmaps = googlemaps.Client(key=api_key)

GetCityPhoto_bp = Blueprint('GetCityPhoto_bp', __name__, url_prefix='/api')

# Helper function to get photo url
def fetch_single_photo(city):
    try:
        # Use the Places API to get a place_id for the city
        places_result = gmaps.places(city)

        # If results are found, proceed to get photo reference
        if places_result['status'] == 'OK' and places_result['results']:
            place_id = places_result['results'][0]['place_id']
            place_details = gmaps.place(place_id=place_id)

            # Extract photo URL from the response
            if 'photos' in place_details['result']:
                photo_reference = place_details['result']['photos'][0]['photo_reference']  # Use the first photo reference
                # Construct photo URL
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"
                return photo_url
            else:
                return "No photo found for the place."

        return "No results found for the specified city."
    except ApiError as e:
        print(f"API Error: {e}")
        return "Error fetching photo from Google Places API."

# Route to get photo url
@GetCityPhoto_bp.route('/get_city_photo', methods=['POST'])
def get_city_photo():
    try:
        data = request.json
        city = data.get('cityName')
        print('City from GetCityPhoto_bp: ', city)

        # Fetch the photo using the helper function
        photo_url = fetch_single_photo(city)

        return jsonify({"photo_url": photo_url}), 200
    except Exception as e:
        print(f"Exception occurred: {e}")
        return jsonify({"error": str(e)}), 500
