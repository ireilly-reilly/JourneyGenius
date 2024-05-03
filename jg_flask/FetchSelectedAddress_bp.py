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
        state = data.get('State', '').strip()  # Default to an empty string if no city provided
        # print("Descriptions: ")
        print(state)

        # print("Filter: ")
        print("Extraction:\n")
        foods = extract_name(descriptions)
        print(foods)

        # Extract restaurant names from descriptions

    except Exception as e:
        print("Can't get chosen results:", e)

    try:
        for food in foods:
            subset = df.loc[(df['Place'] == food) & (df['State'].str.strip().str.lower() == state.lower()), ['Address']]
            print(f"Filtered subset for {food} in {state}:", subset)
            
            if not subset.empty:
                first_address = subset.iloc[0]['Address']  # Get the first address only
                restaurant_addresses.append(first_address)
            else:
                print(f"No addresses found for {food} in {state}")

        if restaurant_addresses:
            response_data = {
                'message': 'Restaurant addresses retrieved successfully',
                'addresses': restaurant_addresses
            }
            return jsonify(restaurant_addresses), 200
        else:
            return jsonify({'message': 'No addresses found'})

    except Exception as e:
        print("Error retrieving addresses:", e)
        return jsonify({'message': 'Error retrieving addresses', 'error': str(e)}), 500



# Define route to handle description request
@FetchAddress_bp.route('/fetch_activity_address', methods=['POST'])
def ActivityAddress_bp():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
    activity_csv_file_path = os.path.join(CSV_FOLDER, 'activity_data.csv')
    
    df = pd.read_csv(activity_csv_file_path, encoding='utf-8') 

    activity_addresses = []

    try:
        data = request.json
        descriptions = data.get('Activities')
        state = data.get('State', '').strip()  # Default to an empty string if no city provided
        print("Descriptions: ")
        print(state)

        # print("Filter: ")
        print("Extraction:\n")
        activities = extract_name(descriptions)
        print(activities)

        # Extract restaurant names from descriptions

    except Exception as e:
        print("Can't get chosen results:", e)

    try:
        for activity in activities:
            subset = df.loc[(df['Place'] == activity) & (df['State'].str.strip().str.lower() == state.lower()), ['Address']]
            print(f"Filtered subset for {activity} in {state}:", subset)
            
            if not subset.empty:
                first_address = subset.iloc[0]['Address']  # Get the first address only
                activity_addresses.append(first_address)
            else:
                print(f"No addresses found for {activity} in {state}")

        if activity_addresses:
            response_data = {
                'message': 'Activity addresses retrieved successfully',
                'addresses': activity_addresses
            }
            return jsonify(activity_addresses), 200
        else:
            return jsonify({'message': 'No activities found'})

    except Exception as e:
        print("Error retrieving addresses:", e)
        return jsonify({'message': 'Error retrieving addresses', 'error': str(e)}), 500


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
        state = data.get('State', '').strip()  # Default to an empty string if no state provided
        # print("Descriptions: ")
        print(state)

        # print("Filter: ")
        print("Extraction:\n")
        landmarks = extract_name(descriptions)
        print(landmarks)

        # Extract names from descriptions

    except Exception as e:
        print("Can't get chosen results:", e)

    try:
        for landmark in landmarks:
            subset = df.loc[(df['Place'] == landmark) & (df['State'].str.strip().str.lower() == state.lower()), ['Address']]
            print(f"Filtered subset for {landmark} in {state}:", subset)
            
            if not subset.empty:
                first_address = subset.iloc[0]['Address']  # Get the first address only
                landmark_addresses.append(first_address)
            else:
                print(f"No addresses found for {landmark} in {state}")

        if landmark_addresses:
            response_data = {
                'message': 'Landmark addresses retrieved successfully',
                'addresses': landmark_addresses
            }
            return jsonify(landmark_addresses), 200
        else:
            return jsonify({'message': 'No addresses found'})

    except Exception as e:
        print("Error retrieving addresses:", e)
        return jsonify({'message': 'Error retrieving addresses', 'error': str(e)}), 500



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
        state = data.get('State', '').strip()  # Default to an empty string if no state provided
        # print("Descriptions: ")
        print(state)

        # print("Filter: ")
        print("Extraction:\n")
        shops = extract_name(descriptions)
        print(shops)

        # Extract shop names from descriptions

    except Exception as e:
        print("Can't get chosen results:", e)

    try:
        for shop in shops:
            subset = df.loc[(df['Place'] == shop) & (df['State'].str.strip().str.lower() == state.lower()), ['Address']]
            print(f"Filtered subset for {shop} in {state}:", subset)
            
            if not subset.empty:
                first_address = subset.iloc[0]['Address']  # Get the first address only
                shop_addresses.append(first_address)
            else:
                print(f"No addresses found for {shop} in {state}")

        if shop_addresses:
            response_data = {
                'message': 'Shop addresses retrieved successfully',
                'addresses': shop_addresses
            }
            return jsonify(shop_addresses), 200
        else:
            return jsonify({'message': 'No addresses found'})

    except Exception as e:
        print("Error retrieving addresses:", e)
        return jsonify({'message': 'Error retrieving addresses', 'error': str(e)}), 500



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
        state = data.get('State', '').strip()  # Default to an empty string if no state provided
        # print("Descriptions: ")
        print(state)

        # print("Filter: ")
        print("Extraction:\n")
        hotels = extract_name(descriptions)
        print(hotels)

        # Extract hotel names from descriptions

    except Exception as e:
        print("Can't get chosen results:", e)

    try:
        for hotel in hotels:
            subset = df.loc[(df['Place'] == hotel) & (df['State'].str.strip().str.lower() == state.lower()), ['Address']]
            print(f"Filtered subset for {hotel} in {state}:", subset)
            
            if not subset.empty:
                first_address = subset.iloc[0]['Address']  # Get the first address only
                hotel_addresses.append(first_address)
            else:
                print(f"No addresses found for {hotel} in {state}")

        if hotel_addresses:
            response_data = {
                'message': 'Hotel addresses retrieved successfully',
                'addresses': hotel_addresses
            }
            return jsonify(hotel_addresses), 200
        else:
            return jsonify({'message': 'No addresses found'})

    except Exception as e:
        print("Error retrieving addresses:", e)
        return jsonify({'message': 'Error retrieving addresses', 'error': str(e)}), 500



def extract_name(descriptions):
    restaurant_titles = []
    for description in descriptions:
        # Find the portion before the first colon and strip any extra spaces
        title = re.split(r':', description, maxsplit=1)[0].strip()
        restaurant_titles.append(title)
    return restaurant_titles