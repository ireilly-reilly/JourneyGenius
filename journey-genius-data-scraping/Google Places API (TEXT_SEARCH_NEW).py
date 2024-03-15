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
num_searches = 3  # Number of searches to simulate

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_header)

    for _ in range(num_searches):
        # Simulate random search queries
        search_query = 'Chinese Restaurants in San Francisco'  # Modify search query accordingly

        # Make a Text Search (New) request to the Google Places API
        endpoint_url = 'https://places.googleapis.com/v1/places:searchText'
        params = {
            'textQuery': search_query,
            'key': api_key
        }

        response = requests.post(endpoint_url, json=params)

        if response.status_code == 200:
            data = response.json()
            results = data.get('places', [])

            # Extract and save place data to CSV
            for place in results:
                name = place.get('displayName', {}).get('text', 'N/A')
                address = place.get('formattedAddress', 'N/A')
                rating = place.get('userRating', {}).get('value', 'N/A')

                csv_writer.writerow([name, address, rating])

            print(f"Search returned {len(results)} places for query: {search_query}")
        else:
            print(f"API request failed with status code {response.status_code}")

        # Sleep for a short duration to avoid API rate limits (adjust as needed)
        time.sleep(random.uniform(1, 3))
