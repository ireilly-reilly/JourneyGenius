from flask import Blueprint, request, jsonify
import googlemaps
from googlemaps.exceptions import ApiError
import csv
import os
from app import User, db
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from dotenv import load_dotenv


# MODIFIED BLUEPRINT
getShopping_bp = Blueprint('getShopping_bp', __name__)

# MODIFIED ROUTE AND STRING PRINT
@getShopping_bp.route('/scrape_shopping', methods=['POST'])
@jwt_required()
def scrape_shopping():
    # Get the latitude and longitude from the request
    #print()
    #print("#################### Retrieving Shopping Places #####################")
    latitude = request.json.get('target_lat_str')
    longitude = request.json.get('target_lon_str')
    # Check if latitude, longitude, and price range are not None
    if None in (latitude, longitude):
        return jsonify({'error': 'Latitude or longitude is missing/invalid'}), 400

    # Convert latitude, longitude, and price range to float and int respectively
    try:
        target_lat = float(latitude)
        target_lon = float(longitude)
        #print(f"Received input_lat: {target_lat}")
        #print(f"Received input_lon: {target_lon}")
            

    except ValueError as e:
        print(f"Error converting latitude, longitude, or price range: {e}")
        return jsonify({'error': 'Invalid parameter values'}), 400
        

    
    # Rest of your code
    location = f'{target_lat}, {target_lon}'  # Use the latitude and longitude in the location variable
    #print("Received coordinates in test shopping API " + location)

    # Load environment variables from .env file
    load_dotenv()

    # Get the GMAPS API key from the environment
    api_key = os.getenv("GMAPS_api_key")

    # Define our Client
    gmaps = googlemaps.Client(key=api_key)

    # Define initial search parameters
    #location = '40.730610, -73.935242' # New York City
    radius = 55000 # 55 km radius
    open_now = False # Any location - doesn't need to be open
    # type = 'shopping_mall'
    # can use  'shopping_mall', 'clothing_store', 'electronics_store', 'book_store'
    

    ############################################## We can change this keyword in the future ##############################################
    def parse_data(data):
        if isinstance(data, list):
            return [item.lower() for item in data]  # Convert each item in the list to lowercase
        elif isinstance(data, str):
            return [item.lower() for item in data.split(', ')]  # Split string into a list of categories and convert each to lowercase
        else:
            return [str(data).lower()]  # Convert data to string, wrap in a list, and convert to lowercase

    current_user_id = get_jwt_identity()

    # Get the user from the database
    user = User.query.filter_by(id=current_user_id).first()
    print("Favorite Shopping:", user.fav_shopping)

    target_categories = parse_data(user.fav_shopping)

    
    # Loop through each category in the list
    for target_category in target_categories:
        target_category = target_category.strip()  # Clean up any extra spaces
        print("Processing Category:", target_category)


        # Custom adjustments based on category
        if target_category == 'shopping mall':
            type = "shopping_mall"
        elif target_category == 'clothing store':
            type = 'clothing_store'
        elif target_category == 'electronics store':
            type = 'electronics_store'
        elif target_category == 'book store':
            type = 'book_store'
        else:
            type = target_category 

        print(f"Current Keyword: {type}")

        # Desired result count here
        desired_result_count = 25

        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
        shopping_csv_file_path = os.path.join(CSV_FOLDER, 'shopping_data.csv')

        csv_exists = os.path.exists(shopping_csv_file_path)
    

        Number = 1
        # Create and open a CSV file for writing
        with open(shopping_csv_file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Only write the header row if the file is empty (or doesn't exist)
            if not csv_exists:
                writer.writerow(['Number', 'Id', 'Place', 'Price Range', 'Category', 'Types', 'Address', 'Postal Code', 'City', 'State', 'Country', 'Latitude', 'Longitude'])

            # Initialize a variable to store the next_page_token
            next_page_token = None

            # Initialize a variable to keep track of the results fetched
            results_fetched = 0

            # Initialize a set to store processed place IDs
            processed_place_ids = set()

            # If the CSV file exists, read existing place_id values from the CSV file and populate processed_place_ids
            if csv_exists:
                with open(shopping_csv_file_path, mode='r', newline='', encoding='utf-8') as read_file:
                    reader = csv.reader(read_file)
                    rows = list(reader)  # Read all rows into a list
                    if len(rows) > 1:
                        for row in rows[1:]:
                            place_id = row[1]
                            processed_place_ids.add(place_id)
                        last_row = rows[-1]
                        last_number = int(last_row[0])
                        Number = last_number + 1
            try:
                # Use a loop to fetch multiple pages of results
                while results_fetched < desired_result_count:
                    # Define Search as needed, including the next_page_token if available
                    places_result = gmaps.places_nearby(
                        location=location,
                        radius=radius,
                        open_now=open_now,
                        type=type,
                        # keyword=keyword,
                        page_token=next_page_token
                    )
                    
                    chain_shopping_names = ['Walmart Supercenter', 'Target', 'Walgreens', 'Best Buy', 'CSV Pharmacy', 'Winco', 'Patagonia Outlet', 'Marshalls', 'Nordstrom Rack', "Macy's", "JCPenny", "Gamestop", "Ross", "T.J. Maxx"]  # Add more chain names as needed


                    for place in places_result['results']:
                        my_place_id = place['place_id']
                        if my_place_id in processed_place_ids:
                            continue
                        processed_place_ids.add(my_place_id)
                        place_details = gmaps.place(place_id=my_place_id, fields=['name', 'type', 'price_level', 'formatted_address', 'address_component', 'geometry'])
                        name = place_details['result']['name']
                        if any(chain_name in name for chain_name in chain_shopping_names):
                            continue
                        price_range = place_details['result'].get('price_level', '')
                        types = ', '.join(place_details['result']['types'])
                        address_components = place_details['result'].get('address_components', [])
                        address = place_details['result']['formatted_address']
                        postal_code = next((component['long_name'] for component in address_components if 'postal_code' in component['types']), '')
                        city = next((component['long_name'] for component in address_components if 'locality' in component['types']), '')
                        state = next((component['long_name'] for component in address_components if 'administrative_area_level_1' in component['types']), '')
                        country = next((component['long_name'] for component in address_components if 'country' in component['types']), '')
                        latitude = place_details['result']['geometry']['location']['lat']
                        longitude = place_details['result']['geometry']['location']['lng']
                        # print(latitude)
                        # print(longitude)
                        writer.writerow([Number, my_place_id, name, price_range, type, types, f"{address} {postal_code}", postal_code, city, state, country, latitude, longitude])
                        # print(f"Name: {name}, Price Range: {price_range}, Types: {types}, Address: {address}, Postal Code: {postal_code}, City: {city}, State: {state}, Country: {country}, Latitude: {latitude}, Longitude: {longitude}")

                        results_fetched += 1
                        Number += 1
                        if results_fetched >= desired_result_count:
                            break
                    next_page_token = places_result.get('next_page_token', None)
                    if not next_page_token or results_fetched >= desired_result_count:
                        break
            except ApiError as e:
                print("This is the problem (shops): ", e)
                pass
    
    return "Shopping data scraped successfully!"