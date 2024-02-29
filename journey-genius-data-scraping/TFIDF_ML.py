# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel

# # Load the data from the CSV file
# data = pd.read_csv('places_data.csv')

# # Preprocess the "Price Range" column
# # Encode 'Price Range' values into numerical categories (1 for low, 2 for medium, 3 for high)
# # Fill missing values with 0 (unknown)
# data['Price Range'] = data['Price Range'].map({'Low': 1, 'Medium': 2, 'High': 3})
# data['Price Range'] = data['Price Range'].fillna(0)

# # Preprocess the data and extract relevant features
# # Include 'Price Range' as a feature
# data['Types'] = data['Types'].fillna('')
# data['Address'] = data['Address'].fillna('')
# data['Features'] = data['Types'] + ' ' + data['Address'] + ' ' + data['Price Range'].astype(str)

# # Create a TF-IDF vectorizer to convert text features into numerical vectors
# tfidf_vectorizer = TfidfVectorizer(stop_words='english')
# tfidf_matrix = tfidf_vectorizer.fit_transform(data['Features'])

# # Compute the cosine similarity between places based on their feature vectors
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# def get_recommendations_by_price(place_name, desired_price, cosine_sim=cosine_sim):
#     # Get the index of the input place
#     idx = data[data['Place'] == place_name].index[0]

#     # Map 'Price Range' values to integers (1 for Low, 2 for Medium, 3 for High)
#     price_mapping = {'Low': 1, 'Medium': 2, 'High': 3}

#     # Extract the price range of the input place and convert it to an integer
#     # input_price = price_mapping.get(data['Price Range'][idx], 0)

#     # Filter places with the desired price range
#     similar_places = []
#     for i, sim_score in enumerate(cosine_sim[idx]):
#         place_price = price_mapping.get(data['Price Range'][i], 0)
#         if place_price == desired_price and i != idx:  # Exclude the input place
#             similar_places.append((data['Place'].iloc[i], sim_score))

#     # Sort similar places by cosine similarity
#     similar_places.sort(key=lambda x: x[1], reverse=True)

#     # Return the top 10 similar places
#     return [place for place, _ in similar_places[:10]]






# # Get recommendations for a place with desired price range '2' (Medium)
# desired_price_range = 2
# recommended_places = get_recommendations_by_price('SF Kitchen', desired_price_range)
# print(recommended_places)

# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel

# # Load the data from the CSV file with the correct encoding
# data = pd.read_csv('places_data.csv', encoding='utf-8')

# # Preprocess the "Price Range" column
# # Fill missing values with 0 (unknown)
# data['Price Range'] = data['Price Range'].fillna(0)

# # Preprocess the data and extract relevant features
# # Include 'Price Range' as a feature
# data['Types'] = data['Types'].fillna('')
# data['Address'] = data['Address'].fillna('')
# data['Features'] = data['Types'] + ' ' + data['Address'] + ' ' + data['Price Range'].astype(str)

# # Create a TF-IDF vectorizer to convert text features into numerical vectors
# tfidf_vectorizer = TfidfVectorizer(stop_words='english')
# tfidf_matrix = tfidf_vectorizer.fit_transform(data['Features'])

# # Compute the cosine similarity between places based on their feature vectors
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# # Function to get recommendations for a given place
# def get_recommendations(place_name, cosine_sim=cosine_sim):
#     idx = data[data['Place'] == place_name].index[0]
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:11]  # Top 10 similar places (excluding itself)
    
#     recommended_places = data['Place'].iloc[[i[0] for i in sim_scores]].tolist()
#     numbered_recommendations = [f"{i+1}. {place}" for i, place in enumerate(recommended_places)]
    
#     return '\n'.join(numbered_recommendations)


# # Function to get recommendations for a given place by price
# def get_recommendations_by_price(place_name, desired_price, cosine_sim=cosine_sim):
#     # Get the index of the input place
#     idx = data[data['Place'] == place_name].index[0]

#     # Extract the price range of the input place as an integer
#     input_price = int(data['Price Range'][idx])

#     # Filter places with the desired price range
#     similar_places = []
#     for i, sim_score in enumerate(cosine_sim[idx]):
#         place_price = int(data['Price Range'][i])
#         if place_price == desired_price and i != idx:  # Exclude the input place
#             similar_places.append((data['Place'].iloc[i], sim_score))

#     # Sort similar places by cosine similarity
#     similar_places.sort(key=lambda x: x[1], reverse=True)

#     # Get up to the top 10 similar places
#     recommended_places_with_price_range = [f"{idx + 1}. {place}" for idx, (place, _) in enumerate(similar_places[:10])]
    
#     return recommended_places_with_price_range

# # Get recommendations for a place
# recommended_places = get_recommendations('SF Kitchen')
# print("Recommended Places:\n")
# print(recommended_places)
# print("\n\n\n")

# # Get recommendations for a place with desired price range '2' (Medium)
# desired_price_range = 2
# recommended_places_with_price_range = get_recommendations_by_price('Hong Kong Diner', desired_price_range)
# print("Recommended Places With Desired Price Range:\n")
# for recommend_places_with_desired_price in recommended_places_with_price_range:
#     print(recommend_places_with_desired_price)



# Wrap into a flask app
    # Create a JSON 
    # Should have connection to the DB
    # Should have descriptions in a DB
    # have suer roles (e.g. travel agent role)



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
target_place = "Shanghai 21"
target_lat = 39.5296  # Latitude of SF Kitchen
target_lon = -119.8138  # Longitude of SF Kitchen
desired_price_range = 2  # Desired price range
recommended_places = get_recommendations_with_location_and_price(target_place, target_lat, target_lon, desired_price_range)
print(recommended_places)



# SKip lag
# AWS Compute
# STOP WORD LIKE MCDONALDS OR STARBUCKS