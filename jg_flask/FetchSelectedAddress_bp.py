# Import necessary modules and functions
from flask import Blueprint, jsonify, request
import pandas as pd
import os
import re



# Define description blueprint
FetchAddress_bp = Blueprint('FetchAddress_bp', __name__)

# Define route to handle description request
@FetchAddress_bp.route('/fetch_restaurant_address', methods=['POST'])
def RestaurantAddress_bp():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
    restaurant_csv_file_path = os.path.join(CSV_FOLDER, 'restaurant_data.csv')
    
    df = pd.read_csv(restaurant_csv_file_path, encoding='utf-8') 

    restaurant_addresses = []
    try:
        data = request.json
        descriptions = data.get('Foods')
        city = data.get('City', '').strip()  # Default to an empty string if no city provided
        # print("Descriptions: ")
        print(city)

        # print("Filter: ")
        print("Extraction:\n")
        foods = extract_name(descriptions)
        print(foods)

        # Extract restaurant names from descriptions

    except Exception as e:
        print("Can't get chosen results:", e)

    try:
        for food in foods:
            subset = df.loc[(df['Place'] == food) & (df['City'].str.strip().str.lower() == city.lower()), ['Address']]
            print(f"Filtered subset for {food} in {city}:", subset)
            
            if not subset.empty:
                for _, row in subset.iterrows():
                    restaurant_addresses.append(row['Address'])
            else:
                print(f"No addresses found for {food} in {city}")

        if restaurant_addresses:
            response_data = {
                'message': 'Restaurant addresses retrieved successfully',
                'addresses': restaurant_addresses
            }
            return jsonify(response_data), 200
        else:
            return jsonify({'message': 'No addresses found'}), 404

    except Exception as e:
        print("Error retrieving addresses:", e)
        return jsonify({'message': 'Error retrieving addresses', 'error': str(e)}), 500



# Define route to handle description request
@FetchAddress_bp.route('/fetch_activity_address', methods=['POST'])
def ActivityAddress_bp():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
    restaurant_csv_file_path = os.path.join(CSV_FOLDER, 'activity_data.csv')
    
    df = pd.read_csv(restaurant_csv_file_path, encoding='utf-8') 

    activity_addresses = []
    try:
        data = request.json
        descriptions = data.get('Activities')
        print(activities)
        activities = extract_name(descriptions)

    except Exception as e:
        print("Can't get chosen results:", e)

    try:
        for activity in activities:
            subset = df.loc[df['Place'] == activity, ['Address']]

            for index, row in subset.iterrows():
                activity_address = row['Address']
                activity_addresses.append(activity_address)
                
        response_data = {
            'message': 'Activity addresses retrieved successfully',
            '==>': activity_addresses
        }

        return jsonify(response_data), 200
    except Exception as e:
        print("Can't get the address:", e)


# Define route to handle description request
@FetchAddress_bp.route('/fetch_landmark_address', methods=['POST'])
def LandmarkAddress_bp():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
    restaurant_csv_file_path = os.path.join(CSV_FOLDER, 'landmark_data.csv')
    
    df = pd.read_csv(restaurant_csv_file_path, encoding='utf-8') 

    landmark_addresses = []
    try:
        data = request.json
        descriptions = data.get('Landmarks')
        print(landmarks)
        landmarks = extract_name(descriptions)

    except Exception as e:
        print("Can't get chosen results:", e)

    try:
        for landmark in landmarks:
            subset = df.loc[df['Place'] == landmark, ['Address']]

            for index, row in subset.iterrows():
                landmark_address = row['Address']
                landmark_addresses.append(landmark_address)
                
        response_data = {
            'message': 'Landmark addresses retrieved successfully',
            '==>': landmark_addresses
        }

        return jsonify(response_data), 200
    except Exception as e:
        print("Can't get the address:", e)


# Define route to handle description request
@FetchAddress_bp.route('/fetch_shopping_address', methods=['POST'])
def ShoppingAddress_bp():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
    restaurant_csv_file_path = os.path.join(CSV_FOLDER, 'shopping_data.csv')
    
    df = pd.read_csv(restaurant_csv_file_path, encoding='utf-8') 

    shop_addresses = []
    try:
        data = request.json
        descriptions = data.get('Shops')
        print(shops)
        shops = extract_name(descriptions)

    except Exception as e:
        print("Can't get chosen results:", e)

    try:
        for shop in shops:
            subset = df.loc[df['Place'] == shop, ['Address']]

            for index, row in subset.iterrows():
                shop_address = row['Address']
                shop_addresses.append(shop_address)
                
        response_data = {
            'message': 'Shopping addresses retrieved successfully',
            '==>': shop_addresses
        }

        return jsonify(response_data), 200
    except Exception as e:
        print("Can't get the address:", e)


# Define route to handle description request
@FetchAddress_bp.route('/fetch_hotel_address', methods=['POST'])
def HotelAddress_bp():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
    restaurant_csv_file_path = os.path.join(CSV_FOLDER, 'hotel_data.csv')
    
    df = pd.read_csv(restaurant_csv_file_path, encoding='utf-8') 

    hotel_addresses = []
    try:
        data = request.json
        descriptions = data.get('Hotels')
        print(hotels)
        hotels = extract_name(descriptions)

    except Exception as e:
        print("Can't get chosen results:", e)

    try:
        for hotel in hotels:
            subset = df.loc[df['Place'] == hotel, ['Address']]

            for index, row in subset.iterrows():
                hotel_address = row['Address']
                hotel_addresses.append(hotel_address)
                
        response_data = {
            'message': 'Hotel addresses retrieved successfully',
            '==>': hotel_addresses
        }

        return jsonify(response_data), 200
    except Exception as e:
        print("Can't get the address:", e)


def extract_name(descriptions):
    restaurant_titles = []
    for description in descriptions:
        # Find the portion before the first colon and strip any extra spaces
        title = re.split(r':', description, maxsplit=1)[0].strip()
        restaurant_titles.append(title)
    return restaurant_titles