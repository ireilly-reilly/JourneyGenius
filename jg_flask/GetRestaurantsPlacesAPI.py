from flask import Blueprint, request, jsonify
import googlemaps
import csv
import os

getRestaurant_bp = Blueprint('getRestaurant_bp', __name__)

@getRestaurant_bp.route('/scrape_restaurants', methods=['POST'])
def scrape_restaurants():
    # Get the latitude and longitude from the request
    print("#################### Restaurants BP #####################")
    latitude = request.json.get('target_lat_str')
    longitude = request.json.get('target_lon_str')
    # Check if latitude, longitude, and price range are not None
    if None in (latitude, longitude):
        return jsonify({'error': 'Latitude or longitude is missing/invalid'}), 400

    # Convert latitude, longitude, and price range to float and int respectively
    try:
        target_lat = float(latitude)
        target_lon = float(longitude)
        print(f"Received input_lat: {target_lat}")
        print(f"Received input_lon: {target_lon}")
            

    except ValueError as e:
        print(f"Error converting latitude, longitude, or price range: {e}")
        return jsonify({'error': 'Invalid parameter values'}), 400
        

    
    # Rest of your code
    location = f'{target_lat}, {target_lon}'  # Use the latitude and longitude in the location variable
    print("Received coordinates in test restaurants API " + location)

    # Define the API Key that is being used
    api_key = 'AIzaSyDGC5QtIMrpN1HXPJpamkDhgfVUkq9Jw8Y'

    # Define our Client
    gmaps = googlemaps.Client(key=api_key)

    # Define initial search parameters
    #location = '40.730610, -73.935242' # New York City
    radius = 55000 # 55 km radius
    open_now = False # Any location - doesn't need to be open
    type = 'restaurant' 
    
    ############################################## We can change this keyword in the future ##############################################
    keyword = 'mexican' 
    desired_result_count = 1 # Desired result count here

    # Check if the CSV file already exists
    # Kai's filepath
    csv_exists = os.path.exists('/Users/kai/Capstone/JouneyGenius/journey-genius-data-scraping/restaurant_data.csv')
    # Isaac's filepath
    # Isaac add your filepath here!

    # Create and open a CSV file for writing
    with open('/Users/kai/Capstone/JouneyGenius/journey-genius-data-scraping/restaurant_data.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Only write the header row if the file is empty (or doesn't exist)
        if not csv_exists:
            writer.writerow(['Place', 'Price Range', 'Types', 'Address', 'Postal Code', 'City', 'State', 'Country', 'Latitude', 'Longitude'])
        # Initialize a variable to store the next_page_token
        next_page_token = None

        # Initialize a variable to keep track of the results fetched
        results_fetched = 0

        # Initialize a set to store processed place IDs
        processed_place_ids = set()

        # Use a loop to fetch multiple pages of results
        while results_fetched < desired_result_count:
            # Define Search as needed, including the next_page_token if available
            places_result = gmaps.places_nearby(
                location=location,
                radius=radius,
                open_now=open_now,
                type=type,
                keyword=keyword,
                page_token=next_page_token  # Include the next_page_token
            )

            # Initialize a set to store processed place IDs
            processed_place_ids = set()

            # Loop through each place in the results
            for place in places_result['results']:
                my_place_id = place['place_id']

                # Check if the place ID has already been processed
                if my_place_id in processed_place_ids:
                    continue  # Skip this place

                # Add the place ID to the set of processed IDs
                processed_place_ids.add(my_place_id)

                # Make a request for details
                place_details = gmaps.place(place_id=my_place_id, fields=['name', 'type', 'price_level', 'formatted_address', 'address_component', 'geometry'])

                # Extract and format the data
                name = place_details['result']['name']
                price_range = place_details['result'].get('price_level', '')  # Check if 'price_level' exists
                types = ', '.join(place_details['result']['types'])
                address_components = place_details['result'].get('address_components', [])  # Check if 'address_components' exists
                address = place_details['result']['formatted_address']
                postal_code = next((component['long_name'] for component in address_components if 'postal_code' in component['types']), '')
                city = next((component['long_name'] for component in address_components if 'locality' in component['types']), '')
                state = next((component['long_name'] for component in address_components if 'administrative_area_level_1' in component['types']), '')
                country = next((component['long_name'] for component in address_components if 'country' in component['types']), '')
                latitude = place_details['result']['geometry']['location']['lat']
                longitude = place_details['result']['geometry']['location']['lng']

                # Write the data to the CSV file
                writer.writerow([name, price_range, types, address, postal_code, city, state, country, latitude, longitude])

                print(f"Name: {name}")
                print(f"Price Range: {price_range}")
                print(f"Types: {types}")
                print(f"Address: {address}")
                print(f"Postal Code: {postal_code}")
                print(f"City: {city}")
                print(f"State: {state}")
                print(f"Country: {country}")
                print(f"Latitude: {latitude}")
                print(f"Longitude: {longitude}")
                # Increment the results fetched counter
                results_fetched += 1

                # Check if you have reached the desired result count
                if results_fetched >= desired_result_count:
                    break

            # Check if there are more results to fetch
            next_page_token = places_result.get('next_page_token', None)

            # If there are no more results or you have reached the desired count, exit the loop
            if not next_page_token or results_fetched >= desired_result_count:
                break

    return "Restaurant data scraped successfully!"

