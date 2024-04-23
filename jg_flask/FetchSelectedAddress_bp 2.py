# Import necessary modules and functions
from flask import Blueprint, jsonify, request
import pandas as pd
import os


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
        foods = data.get('Foods')
        print(foods)

    except Exception as e:
        print("Can't get chosen results:", e)

    try:
        for food in foods:
            subset = df.loc[df['Place'] == food, ['Address']]

            for index, row in subset.iterrows():
                restaurant_address = row['Address']
                restaurant_addresses.append(restaurant_address)
                
        response_data = {
            'message': 'Restaurant addresses retrieved successfully',
            '==>': restaurant_addresses
        }

        return jsonify(response_data), 200
    except Exception as e:
        print("Can't get the address:", e)



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
        activities = data.get('Activities')
        print(activities)

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
        landmarks = data.get('Landmarks')
        print(landmarks)

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
        shops = data.get('Shops')
        print(shops)

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
        hotels = data.get('Hotels')
        print(hotels)

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


