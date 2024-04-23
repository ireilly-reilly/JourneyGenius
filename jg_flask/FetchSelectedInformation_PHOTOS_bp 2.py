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
@FetchSelectedInformation_bp.route('/restaurant_photo_data', methods=['POST'])

def process_restaurant_data():
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
            'message': 'Location data and photo URLs retrieved successfully (restaurants)',
            'location_ids': place_ids,
            'photo_urls': photo_urls
        }

        return jsonify(response_data), 200

    except Exception as e:
        error_message = str(e)
        print("Error retrieving photos:", error_message)
        return jsonify({'error': 'An error occurred while retrieving the photos', 'message': error_message})

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



# Define route to handle description request
@FetchSelectedInformation_bp.route('/activity_photo_data', methods=['POST'])

def process_activity_data():
    try:
        data = request.json
        activities = data.get('activities')
        print(activities)

        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
        activity_csv_file_path = os.path.join(CSV_FOLDER, 'activity_data.csv')

        df = pd.read_csv(activity_csv_file_path, encoding='utf-8') 

        place_ids = []
        photo_urls = []
        for activity in activities:
            subset = df.loc[df['Place'] == activity, ['Id']]

            for index, row in subset.iterrows():
                place_id = row['Id']
                
                photo_url = fetch_single_photo(place_id)
                place_ids.append(place_id)
                photo_urls.append(photo_url)
        
        print(photo_urls)

        response_data = {
            'message': 'Location data and photo URLs retrieved successfully (activities)',
            'location_ids': place_ids,
            'photo_urls': photo_urls
        }

        return jsonify(response_data), 200

    except Exception as e:
        error_message = str(e)
        print("Error retrieving photos:", error_message)
        return jsonify({'error': 'An error occurred while retrieving the photos', 'message': error_message})

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



# Define route to handle description request
@FetchSelectedInformation_bp.route('/landmark_photo_data', methods=['POST'])

def process_landmark_data():
    try:
        data = request.json
        landmarks = data.get('landmarks')
        print(landmarks)

        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
        landmark_csv_file_path = os.path.join(CSV_FOLDER, 'landmark_data.csv')

        df = pd.read_csv(landmark_csv_file_path, encoding='utf-8') 

        place_ids = []
        photo_urls = []
        for landmark in landmarks:
            subset = df.loc[df['Place'] == landmark, ['Id']]

            for index, row in subset.iterrows():
                place_id = row['Id']
                
                photo_url = fetch_single_photo(place_id)
                place_ids.append(place_id)
                photo_urls.append(photo_url)
        
        print(photo_urls)

        response_data = {
            'message': 'Location data and photo URLs retrieved successfully (landmarks)',
            'location_ids': place_ids,
            'photo_urls': photo_urls
        }

        return jsonify(response_data), 200

    except Exception as e:
        error_message = str(e)
        print("Error retrieving photos:", error_message)
        return jsonify({'error': 'An error occurred while retrieving the photos', 'message': error_message})

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



# Define route to handle description request
@FetchSelectedInformation_bp.route('/shopping_photo_data', methods=['POST'])

def process_shopping_data():
    try:
        data = request.json
        shops = data.get('shops')
        print(shops)

        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
        shopping_csv_file_path = os.path.join(CSV_FOLDER, 'shopping_data.csv')

        df = pd.read_csv(shopping_csv_file_path, encoding='utf-8') 

        place_ids = []
        photo_urls = []
        for shops in shops:
            subset = df.loc[df['Place'] == shops, ['Id']]

            for index, row in subset.iterrows():
                place_id = row['Id']
                
                photo_url = fetch_single_photo(place_id)
                place_ids.append(place_id)
                photo_urls.append(photo_url)
        
        print(photo_urls)

        response_data = {
            'message': 'Location data and photo URLs retrieved successfully (shops)',
            'location_ids': place_ids,
            'photo_urls': photo_urls
        }

        return jsonify(response_data), 200

    except Exception as e:
        error_message = str(e)
        print("Error retrieving photos:", error_message)
        return jsonify({'error': 'An error occurred while retrieving the photos', 'message': error_message})

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
    


# Define route to handle description request
@FetchSelectedInformation_bp.route('/hotel_photo_data', methods=['POST'])

def process_hotel_data():
    try:
        data = request.json
        hotels = data.get('hotels')
        print(hotels)

        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
        hotel_csv_file_path = os.path.join(CSV_FOLDER, 'hotel_data.csv')

        df = pd.read_csv(hotel_csv_file_path, encoding='utf-8') 

        place_ids = []
        photo_urls = []
        for hotel in hotels:
            subset = df.loc[df['Place'] == hotel, ['Id']]

            for index, row in subset.iterrows():
                place_id = row['Id']
                
                photo_url = fetch_single_photo(place_id)
                place_ids.append(place_id)
                photo_urls.append(photo_url)
        
        print(photo_urls)

        response_data = {
            'message': 'Location data and photo URLs retrieved successfully (hotels)',
            'location_ids': place_ids,
            'photo_urls': photo_urls
        }

        return jsonify(response_data), 200

    except Exception as e:
        error_message = str(e)
        print("Error retrieving photos:", error_message)
        return jsonify({'error': 'An error occurred while retrieving the photos', 'message': error_message})

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

