########################### RELATED LOCATION WITH DESIRED PRICE RANGE AND RELATED RESTAURANT WITH RELATIVE LOCATION ########################################



import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
# import os

# Load the data from the CSV file with the correct encoding
# data = pd.read_csv('/Users/dontstealmyshxt/Documents/GitHub/JourneyGenius/journey-genius-data-scraping/restaurant_data.csv', encoding='utf-8')
data = pd.read_csv('journey-genius-data-scraping/restaurant_data.csv')

# Preprocess the "Price Range" column
# Fill missing values with 0 (unknown)
data['Price Range'] = data['Price Range'].fillna(0)

# Preprocess the data and extract relevant features
# Include 'Price Range' as a feature
data['Types'] = data['Types'].fillna('')
data['Address'] = data['Address'].fillna('')
# data['Place'] = data['Place'].fillna('')
data['Features'] = data['Types'] + ' ' + data['Address'] + ' ' + data['Price Range'].astype(str) 
# + data['Place']

# Create a TF-IDF vectorizer to convert text features into numerical vectors
# tfidf_vectorizer = TfidfVectorizer(stop_words=["english", "Mcdonald's", "Starbucks", "Barnes & Noble"])
tfidf_vectorizer = TfidfVectorizer(stop_words=["english"])
tfidf_matrix = tfidf_vectorizer.fit_transform(data['Features'])

# Compute the cosine similarity between places based on their feature vectors
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to calculate Haversine distance between two sets of coordinates
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in km
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = R * c

    return distance


# Function to get recommendations by text similarity, location, and price range
def get_recommendations_with_location_and_price(place_name, Latitude, Longitude, desired_price, cosine_sim=cosine_sim):
    # Get the index of the input place
    idx = data[data['Place'] == place_name].index[0]

    # Extract the price range of the input place as an integer
    input_price = int(data['Price Range'][idx])

    # Extract the latitude and longitude of the input place
    input_lat = data['Latitude'].iloc[idx]
    input_lon = data['Longitude'].iloc[idx]

    # Calculate geographical distances and text-based similarities
    distances = [haversine(input_lat, input_lon, lat, lon) for lat, lon in zip(data['Latitude'], data['Longitude'])]
    text_similarities = cosine_sim[idx]

    # Calculate price differences
    price_differences = [abs(input_price - price) for price in data['Price Range']]

    # Combine text similarity, geographical distance, and price difference into a composite score
    composite_scores = [(1 - text_sim) + (1 - dist / max(distances)) + (1 - price_diff / max(price_differences))
                        for text_sim, dist, price_diff in zip(text_similarities, distances, price_differences)]

    # Sort places by composite similarity score
    sorted_places = [place for _, place in sorted(zip(composite_scores, data['Place']), reverse=True)]

    # Return the top 10 similar places
    return sorted_places[1:11]  # Exclude the input place


# Get recommendations for a place with location, price range, and text-based ranking
# target_place = "Shanghai 21"
target_place = "SF Kitchen"

target_lat = 39.5296  # Latitude of SF Kitchen
target_lon = -119.8138  # Longitude of SF Kitchen
desired_price_range = 2  # Desired price range
recommended_places = get_recommendations_with_location_and_price(target_place, target_lat, target_lon, desired_price_range)
print(recommended_places)



# SKip lag
# AWS Compute
# STOP WORD LIKE MCDONALDS OR STARBUCKS