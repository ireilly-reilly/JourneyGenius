import requests
import csv
import random
import time

# Replace with your Google Places API key
api_key = 'AIzaSyDGC5QtIMrpN1HXPJpamkDhgfVUkq9Jw8Y'

# CSV file configuration
csv_file_path = 'places_data.csv'
csv_header = ['Name', 'Address', 'Rating']

# Simulate searches for random places
num_searches = 1  # Number of searches to simulate

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_header)

    for _ in range(num_searches):
        # Simulate random search parameters (you can adjust accordingly)


        # RANDOM LOCATIONS
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        radius = random.randint(500, 5000)  # Random radius in meters


        keyword = 'Restaurants'  # You can change the keyword based on your needs

        # Make a request to the Google Places API
        endpoint_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
        params = {
            'location': f'{latitude},{longitude}',
            'radius': radius,
            'keyword': keyword,
            'key': api_key
        }

        response = requests.get(endpoint_url, params=params)

        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])

            # Extract and save place data to CSV
            for place in results:
                name = place.get('name', 'N/A')
                address = place.get('vicinity', 'N/A')
                rating = place.get('rating', 'N/A')

                csv_writer.writerow([name, address, rating])

            print(f"Search {len(results)} places near ({latitude},{longitude})")
        else:
            print(f"API request failed with status code {response.status_code}")

        # Sleep for a short duration to avoid API rate limits (adjust as needed)
        time.sleep(random.uniform(1, 3))
