#-----------SUMMARY-------------
#This is a Flask blueprint version of TFIDF_ML script
#Make sure the filepath for the CSV is correct on the machine it is running on
#We may need to make the filepath dynamic for ease of use across multiple computers
#It may also make more sense to make this a blueprint to the original Flask app so it can all run on the same port 
#TO MAKE A CALL TO THIS MODEL:
#API link is: '/api/run_ML_model_recommendations'
#Note to Ethan: We will need to add a json request to receive the location or whatever parameters
#   this function requires

from flask import Flask, jsonify, request, Blueprint, make_response, Response
from app import db
from app import User
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

#Blueprint declaration
hotelsRecommendation_bp = Blueprint('hotelsRecommendation_bp', __name__)

# Load the data from the CSV file with the correct encoding
# Ethan's Filepath
# data = pd.read_csv('/Users/dontstealmyshxt/Documents/GitHub/JourneyGenius/journey-genius-data-scraping/restaurant_data.csv', encoding='utf-8') #TODO Make sure this is set to the correct location depending on the machine running it 

#Dynamic filepath
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
landmark_csv_file_path = os.path.join(CSV_FOLDER, 'hotel_data.csv')

data = pd.read_csv(landmark_csv_file_path, encoding='utf-8') 
# #print(f"Number of rows in data: {len(data)}")

# data = pd.read_csv('JouneyGenius/journey-genius-data-scraping/restaurant_data.csv', encoding='utf-8')

# Preprocess the "Price Range" column
# Fill missing values with 0 (unknown)
data['Price Range'] = data['Price Range'].fillna(0)

# Preprocess the data and extract relevant features
# Include 'Price Range' as a feature
data['Types'] = data['Types'].fillna('')
data['Address'] = data['Address'].fillna('')
data['Features'] = data['Types'] + ' ' + data['Address'] + ' ' + data['Price Range'].astype(str)

# Create a TF-IDF vectorizer to convert text features into numerical vectors
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
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
def get_recommendations_with_location_and_price(target_place, input_lat, input_lon, input_price):

    #print(f"Received target_place: {target_place}")
    #print(f"Received input_lat: {input_lat}")
    #print(f"Received input_lon: {input_lon}")
    #print(f"Received input_price: {input_price}")
    #print("Variables successfully passed by parameter :)")
    #print()
    #print(data.head())  # Print the first few rows
    #print(data.info())  # Print column names and data types
    #print()

    # Get the index of the input place
    idx = data[data['Place'] == target_place].index
    #print(idx)
    #print(data['Place'].unique())


    if len(idx) == 0:
        return {'error': f'Place "{target_place}" not found'}, 404

    idx = idx[0]  # Get the first index if multiple matches exist

    # Extract the price range of the input place as an integer
    input_price = int(data['Price Range'][idx])
    
    # Extract the latitude and longitude of the input place
    input_lat = data['Latitude'].iloc[idx]
    input_lon = data['Longitude'].iloc[idx]
    #print(input_lat)
    #print(input_lon)

    # Calculate geographical distances and text-based similarities
    distances = [haversine(input_lat, input_lon, lat, lon) for lat, lon in zip(data['Latitude'], data['Longitude'])]
    text_similarities = cosine_sim[idx]

    # Calculate price differences
    price_differences = [abs(input_price - price) for price in data['Price Range']]

    # Calculate composite scores, safely handling divisions
    composite_scores = []
    max_distance = max(distances) if max(distances) > 0 else 1  # Avoid division by zero
    max_price_difference = max(price_differences) if max(price_differences) > 0 else 1  # Avoid division by zero

    for text_sim, dist, price_diff in zip(text_similarities, distances, price_differences):
        # Calculate the score, considering safe division
        score = (1 - text_sim)
        score += (1 - dist / max_distance)
        score += (1 - price_diff / max_price_difference)
        composite_scores.append(score)

    # Sort places by composite similarity score
    sorted_places = [place for _, place in sorted(zip(composite_scores, data['Place']), reverse=True)]

    # Return the top 10 similar places as a list of dictionaries
    recommendations = [{'place': place} for place in sorted_places[1:6]]
    return {'recommendations': recommendations}


# def descriptionGeneration(recommended_places):
#     # Ensure recommended_places is a list
#     if not isinstance(recommended_places, list):
#         recommended_places = [recommended_places]

#     # Initialize an empty array to store descriptions
#     response_message_array = []

#     # Iterate over recommended_places and generate descriptions
#     for place in recommended_places:
#         # Compose a prompt using the current place
#         prompt = f"Describe the hotel {place} regarding accommodation experience from online sources in one or two sentences. Do not response with Im sorry, but as an AI model, I am unable to browse the internet. If this happens then make something up. Answer in this format- (Hotel Name): (Then description)"

#         # Generate descriptions using OpenAI
#         response = client.chat.completions.create(
#             model="gpt-4",
#             messages=[
#                 {"role": "system", "content": "You are a travel critic."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
        
#         # Extract and append the description to response_message_array
#         response_message = response.choices[0].message.content
#         response_message_array.append(response_message)

#     # Print the array of descriptions
#     #print(response_message_array)

#     return response_message_array

#Returns item if 1, returns first item if more than one
def parse_data(data):
    if isinstance(data, list):
        if len(data) > 1:
            return data[0]
        else:
            return data[0]
    else:
        return data


@hotelsRecommendation_bp.route('/run_ML_model_hotel_recommendations', methods=['POST'])
@jwt_required()
def recommend():
    current_user_id = get_jwt_identity()
    # Get the user from the database
    user = User.query.filter_by(id=current_user_id).first()

    #target_accommodations will looke like: 'hotels' or 'resorts' or 'vacation_rentals'
    target_accomodations = parse_data(user.fav_accomodations)
    try:
        data = request.json
        target_place = 'Reno' 
        target_lat_str = data.get('target_lat_str')
        target_lon_str = data.get('target_lon_str')
        desired_price_range_str = data.get('desired_price_range_str')
        print(target_place)
        #print(target_lat_str)
        #print(target_lon_str)
        #print(desired_price_range_str)
        #print()
        #print("#################### TFIDF - Hotel Recommendations ####################")
        #print("Values from the frontend is successfully sent over :)")
        #print()

        # Check if latitude, longitude, and price range are not None
        if None in (target_lat_str, target_lon_str, desired_price_range_str):
            return jsonify({'error': 'Latitude, longitude, or price range is missing or invalid'}), 400

        # Convert latitude, longitude, and price range to float and int respectively
        try:
            target_lat = float(target_lat_str)
            target_lon = float(target_lon_str)
            desired_price_range = int(desired_price_range_str)
            #print(target_lat_str)
            #print(target_lon_str)
            #print(desired_price_range_str)
            #print("Variables successfully converted from strings to floats and int")
            #print()

        except ValueError as e:
            print(f"Error converting latitude, longitude, or price range: {e}")
            return jsonify({'error': 'Invalid parameter values'}), 400

        # Call the recommendation function
        recommended_places = get_recommendations_with_location_and_price(target_place, target_lat, target_lon, desired_price_range)

        # Extract just the place names from the list of dictionaries
        place_names = [place['place'] for place in recommended_places['recommendations']]

        # Print the place names
        #print("Here are the recommended Landmark Names from the TFIDF Model:")
        #print(place_names)
        #print()

        # Return the recommended places (limited to 10)
        # descriptions = descriptionGeneration(place_names)
        # return jsonify({'recommended_places': descriptions[:5]})
    
        # Use this for the recommended places without the description!
        return jsonify({'recommended_places': place_names[:5]})

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error processing request: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500