# from flask import Blueprint, jsonify, request
# import pandas as pd
# import os
# import googlemaps
# from googlemaps.exceptions import ApiError
# from dotenv import load_dotenv


# # Define description blueprint
# FetchSelectedInformation_bp = Blueprint('FetchSelectedInformation_bp', __name__)

# # Define route to handle description request
# @FetchSelectedInformation_bp.route('/process_data', methods=['POST'])

# # Function to fetch restaurants from Flask API
# def process_data():
#     try:
#         # Extract data received from Vue.js
#         data = request.json

#         # Extract relevant variables from the data
#         # These variables will differ for each type of place

#         # activities = data.get('activities')
#         # landmarks = data.get('landmarks')
#         foods = data.get('foods')
#         # shops = data.get('shops')
#         # hotels = data.get('hotels')
#         # datesData = data.get('datesData')
#         # budget = data.get('budget')
#         # stateData = data.get('stateData')
#         # city = data.get('city')
#         # lat = data.get('lat')
#         # long = data.get('long')
#         # cityDescription = data.get('cityDescription')
#         # citySlogan = data.get('citySlogan')


#         # print("Received data:")
#         # print("Activities:", activities)
#         # print("Landmarks:", landmarks)
#         # print("Foods:", foods)
#         # print("Shops:", shops)
#         # print("Hotels:", hotels)
#         # print("Dates Data:", datesData)
#         # print("Budget:", budget)
#         # print("State Data:", stateData)
#         # print("City:", city)
#         # print("Latitude:", lat)
#         # print("Longitude:", long)
#         # print("City Description:", cityDescription)
#         # print("City Slogan:", citySlogan)

#         BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#         CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
#         restaurant_csv_file_path = os.path.join(CSV_FOLDER, 'restaurant_data.csv')

#         df = pd.read_csv(restaurant_csv_file_path, encoding='utf-8') 

#         for food in foods:
#             subset = df.loc[df['Place'] == food, ['Latitude', 'Longitude']]

#             locations = []
#             for index, row in subset.iterrows():
#                 latitude = float(row['Latitude'])
#                 longitude = float(row['Longitude'])
#                 locations.append({'latitude': latitude, 'longitude': longitude})

#         response_data = {
#             'message': 'Location data retrieved successfully',
#             'locations': locations
#         }

#         return jsonify(response_data), 200

#     except Exception as e:
#         # Handle any errors that occur during processing
#         error_message = str(e)  # Convert the exception to a string
#         print("Error processing data:", error_message)
#         return jsonify({'error': 'An error occurred while processing the data', 'message': error_message})



############################################# MODIFIED SHIT BELOW   :D ####################################################################


# # Load environment variables from .env file
# load_dotenv()

# # Get the GMAPS API key from the environment
# api_key = os.getenv("GMAPS_api_key")

# # Define our Client
# gmaps = googlemaps.Client(key=api_key)


# # Define description blueprint
# FetchSelectedInformation_bp = Blueprint('FetchSelectedInformation_bp', __name__)

# # Define route to handle description request
# @FetchSelectedInformation_bp.route('/process_data', methods=['POST'])

# def process_data():
#     try:
#         data = request.json
#         foods = data.get('foods')
#         print(foods)

#         BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#         CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
#         restaurant_csv_file_path = os.path.join(CSV_FOLDER, 'restaurant_data.csv')

#         df = pd.read_csv(restaurant_csv_file_path, encoding='utf-8') 

#         locations = []
#         photo_urls = []
#         for food in foods:
#             subset = df.loc[df['Place'] == food, ['Latitude', 'Longitude']]

#             for index, row in subset.iterrows():
#                 latitude = float(row['Latitude'])
#                 longitude = float(row['Longitude'])
#                 locations.append({'latitude': latitude, 'longitude': longitude})

#                 print(locations)
#                 photo_url = fetch_single_photo(latitude, longitude)
#                 photo_urls.append(photo_url)

#         # photo_url = fetch_single_photo(47.611757, -122.2895465)

#         response_data = {
#             'message': 'Location data and photo URLs retrieved successfully',
#             'locations': locations,
#             'photo_urls': photo_url
#         }

#         return jsonify(response_data), 200

#     except Exception as e:
#         error_message = str(e)
#         print("Error retrieving photos:", error_message)
#         return jsonify({'error': 'An error occurred while retriving the photos', 'message': error_message})

# def fetch_single_photo(latitude, longitude):
#     try:
#         nearby_search_results = gmaps.places_nearby(location=(latitude, longitude), radius=15)
#         if nearby_search_results['results']:
#             for place in nearby_search_results['results']:
#                 if 'photos' in place:
#                     photo_reference = place['photos'][1]['photo_reference']
#                     print(f"Photo Reference: {photo_reference}")

#                     # Construct photo URL
#                     # photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"
#                     photo_url = f"https://places.googleapis.com/v1/places/{photo_reference}?fields=id,displayName&key=API_KEY"
#                     print(f"Photo URL: {photo_url}")

#                     return photo_url  # Return the first photo URL found
#             # If no photo URLs found
#             print("No photo URLs found for the nearby places.")
#             return None
#         else:
#             print("No nearby places found.")
#             return None
#     except ApiError as e:
#         print(f"Error fetching photo: {e}")
#         return None


from flask import Blueprint, jsonify, request
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
        print(foods)

        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
        restaurant_csv_file_path = os.path.join(CSV_FOLDER, 'restaurant_data.csv')

        df = pd.read_csv(restaurant_csv_file_path, encoding='utf-8') 

        place_ids = []
        photo_urls = []
        for food in foods:
            subset = df.loc[df['Place'] == food, ['Id']]

            for index, row in subset.iterrows():
                place_id = row['Id']
                
                photo_url = fetch_single_photo(place_id)
                place_ids.append(place_id)
                photo_urls.append(photo_url)
        
        print(photo_urls)

        response_data = {
            'message': 'Location data and photo URLs retrieved successfully',
            'location_ids': place_ids,
            'photo_urls': photo_urls
        }

        return jsonify(response_data), 200

    except Exception as e:
        error_message = str(e)
        print("Error retrieving photos:", error_message)
        return jsonify({'error': 'An error occurred while retrieving the photos', 'message': error_message})

# def fetch_single_photo(place_id):
#     try:
#         # Construct place details URL using the place ID
#         place_details_url = f"https://places.googleapis.com/v1/places/{place_id}?fields=photo&key={api_key}"
        
#         # Make a request to fetch place details
#         response = gmaps.places(place_id)

#         # Extract photo URL from the response
#         if 'photo' in response:
#             photo_reference = response['photo'][1]['photo_reference']
#             # Construct photo URL
#             photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"
#             print(f"Photo URL: {photo_url}")

#             return photo_url
#         else:
#             print("No photo found for the place.")
#             return None
#     except ApiError as e:
#         print(f"Error fetching photo: {e}")
#         return None

def fetch_single_photo(place_id):
    try:
        # Make a request to fetch place details
        place_details = gmaps.place(place_id)

        # Extract photo URL from the response
        if 'photos' in place_details['result']:
            photo_reference = place_details['result']['photos'][1]['photo_reference']  # Assuming photo reference is at index 1
            # Construct photo URL
            photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"
            print(f"Photo URL: {photo_url}")

            return photo_url
        else:
            print("No photo found for the place.")
            return None
    except ApiError as e:
        print(f"Error fetching photo: {e}")
        return None
