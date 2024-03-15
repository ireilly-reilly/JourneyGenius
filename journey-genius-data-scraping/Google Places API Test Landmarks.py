import googlemaps
import csv
import os

# Define the API Key that is being used
api_key = 'AIzaSyDGC5QtIMrpN1HXPJpamkDhgfVUkq9Jw8Y'

# Define our Client
gmaps = googlemaps.Client(key=api_key)

# Define initial search parameters
# location = '47.620564,-122.350616' # Seattle, Washington
# location = '37.7749,-122.4194' # San Francisco, California
# location = '39.530895,-119.814972' # Reno, Nevada
# location = '39.744137, -104.950050' # Denver, Colorado 
location = '34.052235, -118.243683' # Los Angeles, California
radius = 55000 # 55 km radius
open_now = False # Any location - doesn't need to be open
type = 'park' # 
# keyword = 'chinese' 
desired_result_count = 100 # Desired result count here

# Create and open a CSV file for writing
# with open('journey-genius-data-scraping/landmark_data.csv', mode='a', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)

#     # Write the header row with column names
#     writer.writerow(['Place', 'Price Range', 'Types', 'Address', 'Postal Code', 'City', 'State', 'Country'])


# Check if the CSV file already exists
csv_exists = os.path.exists('journey-genius-data-scraping/landmark_data.csv')

# Create and open a CSV file for writing
with open('journey-genius-data-scraping/landmark_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Only write the header row if the file is empty (or doesn't exist)
    if not csv_exists:
        writer.writerow(['Place', 'Price Range', 'Types', 'Address', 'Postal Code', 'City', 'State', 'Country'])
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
            # keyword=keyword,
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
            place_details = gmaps.place(place_id=my_place_id, fields=['name', 'type', 'price_level', 'address_component'])

            # Extract and format the data
            name = place_details['result']['name']
            price_range = place_details['result'].get('price_level', '')  # Check if 'price_level' exists
            types = ', '.join(place_details['result']['types'])
            address_components = place_details['result'].get('address_components', [])  # Check if 'address_components' exists
            address = ' '.join([component['long_name'] for component in address_components if 'street_number' in component['types'] or 'route' in component['types']])
            postal_code = next((component['long_name'] for component in address_components if 'postal_code' in component['types']), '')
            city = next((component['long_name'] for component in address_components if 'locality' in component['types']), '')
            state = next((component['long_name'] for component in address_components if 'administrative_area_level_1' in component['types']), '')
            country = next((component['long_name'] for component in address_components if 'country' in component['types']), '')

            # Write the data to the CSV file
            writer.writerow([name, price_range, types, f"{address} {postal_code}", postal_code, city, state, country])

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


