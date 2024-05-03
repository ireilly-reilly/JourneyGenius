from flask import Flask, jsonify, request, Blueprint, make_response, Response
from app import db
from app import User
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import spacy
from openai import OpenAI
import numpy as np
import pandas as pd
import os
from dotenv import load_dotenv
from typing import Dict


# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_md")  

#Blueprint declaration
hotelsRecommendation_bp = Blueprint('hotelsRecommendation_bp', __name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
hotel_csv_file_path = os.path.join(CSV_FOLDER, 'hotel_data.csv')


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

def find_closest_city(target_lat, target_lon, df, threshold_km):
    closest_city = None
    min_distance = float('inf')

    for index, row in df.iterrows():
        city_lat = row['Latitude']
        city_lon = row['Longitude']
        distance = haversine(target_lat, target_lon, city_lat, city_lon)
        
        if distance < min_distance and distance <= threshold_km:
            min_distance = distance
            closest_city = row['City']

    return closest_city

# Calculate semantic similarity between two strings
def calculate_semantic_similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    similarity_score = doc1.similarity(doc2)
    return similarity_score


# Modified code snippet to get recommendations with location 
def get_recommendations_with_location(target_place, input_lat, input_lon, State, new_data):

    # Preprocess the data and extract relevant features
    new_data['Types'] = new_data['Types'].fillna('')
    new_data['Address'] = new_data['Address'].fillna('')
    new_data['Features'] = new_data['Types'] + ' ' + new_data['Address'].astype(str)
    # print(data['Types'])
    # print(data['Address'])

    # Create a TF-IDF vectorizer to convert text features into numerical vectors
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(new_data['Features'])

    # Compute the cosine similarity between places based on their feature vectors
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    recommendations = []

    idx = new_data[(new_data['Place'].str.strip().str.lower() == target_place.lower().strip())].index
    # idx = data[data['Place'] == target_place].index


    if idx.empty:
        print(f"No matching places found for {target_place}")
        return []

    idx = idx[0]

    input_lat = new_data.loc[idx, 'Latitude']
    input_lon = new_data.loc[idx, 'Longitude']

    filtered_data = new_data[(new_data['State'] == State)]
    filtered_data.reset_index(drop=True, inplace=True)
    
    distances = [haversine(input_lat, input_lon, lat, lon) for lat, lon in zip(filtered_data['Latitude'], filtered_data['Longitude'])]
    text_similarities = [cosine_sim[idx][i] for i in filtered_data.index]
    semantic_similarities = [calculate_semantic_similarity(new_data.loc[i, 'Place'], target_place) for i in filtered_data.index]

    max_distance = max(distances) if distances else 1
    max_semantic_sim = max(semantic_similarities) if semantic_similarities else 1

    composite_scores = [(0.01 * (1 - text_sim) + 2 * (1 - dist / max_distance) + 0.3 * (1 - semantic_sim / max_semantic_sim))
                        for text_sim, dist, semantic_sim in zip(text_similarities, distances, semantic_similarities)]
    
    sorted_places = [place for _, place in sorted(zip(composite_scores, filtered_data['Place']), reverse=True)]
    recommendations = [place for place in sorted_places[1:6]]
    return recommendations



def descriptionGeneration(recommended_places):
    # Ensure recommended_places is a list
    if not isinstance(recommended_places, list):
        recommended_places = [recommended_places]

    # Initialize an empty array to store descriptions
    response_message_array = []

    # Iterate over recommended_places and generate descriptions
    for place in recommended_places:
        # Compose a prompt using the current place
        prompt = f"Describe the hotel {place} regarding accommodation experience from online sources in one or two sentences. Do not response with Im sorry, but as an AI model, I am unable to browse the internet. If this happens then make something up. Answer in this format- (Hotel Name): (Then description)Note: do not take score into consideration."


        # Generate descriptions using OpenAI
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an experienced food critic."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract and append the description to response_message_array
        response_message = response.choices[0].message.content
        response_message_array.append(response_message)

    # Print the array of descriptions
    #print(response_message_array)

    return response_message_array


def parse_data(data):
    if isinstance(data, list):
        return [item.lower() for item in data]  # Convert each item in the list to lowercase
    elif isinstance(data, str):
        return [item.lower() for item in data.split(', ')]  # Split string into a list of categories and convert each to lowercase
    else:
        return [str(data).lower()]  # Convert data to string, wrap in a list, and convert to lowercase
    
stateMappings: Dict[str, str] = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming'
}



@hotelsRecommendation_bp.route('/run_ML_model_hotel_recommendations', methods=['POST'])

def recommend():


    # Grab city name from front end
    try:
        data = request.json
        city = str(data.get('desired_city'))
        state = str(data.get('desired_state'))
        target_lat_str = data.get('target_lat_str')
        target_lon_str = data.get('target_lon_str')
        descriptionToggle = data.get('descriptionToggle')

        print(city + ", " + stateMappings[state])
        descriptionToggle = data.get('descriptionToggle')
    except Exception as e:
        print("Can't get city:", e)

    # Initialize a list to store recommended places 
    target_hotels = []


    # Initialize a list to store recommended places
    recommended_places = []
    all_recommendations = []

    df = pd.read_csv(hotel_csv_file_path)




    try:
        # Try to find a restaurant 
        first_row = df[(df['City'] == city) & (df['State'] == stateMappings[state])].iloc[0]

    except IndexError:
        print("No hotels found for the specified city")
        message = {
            message : "nothing in it bruh"
        }
        return jsonify(message)
    # Process the first row found
    if not first_row.empty:
        first_row_with_city = first_row
        # target_foods = str(first_row_with_city['Place'])
        target_hotels.append(first_row_with_city['Place'])
    else:
        print("No rows found for the specified city.")

    print("Total target hotel/s")
    print(target_hotels)


    # for target_food in target_foods:
    for target_food in target_hotels:
        print(target_food)

        try:
            # print("Target Latitude: ", target_lat_str)
            # print("Target Longitude: ", target_lon_str)

            # Check if latitude, longitude range are not None
            if None in (target_lat_str, target_lon_str):
                return jsonify({'error': 'Latitude or longitude is missing or invalid'}), 400

            # Convert latitude, longitude to float and int respectively
            try:
                target_lat = float(target_lat_str)
                target_lon = float(target_lon_str)
            except ValueError as e:
                print(f"Error converting latitude or longitude: {e}")
                return jsonify({'error': 'Invalid parameter values'}), 400
            City = city
            State = stateMappings[state]
            print("before calling function: ", State)
            recommended_places = get_recommendations_with_location(target_food, target_lat, target_lon, State, df)

            # place_names = recommended_places


            # Extend all_recommendations with recommendations for this target food
            all_recommendations.extend(recommended_places)

        except Exception as e:
            # Log the exception for debugging purposes
            print(f"Error processing request: {e}")
            return jsonify({'error': 'An unexpected error occurred'}), 500

    if (descriptionToggle == True):
        description = descriptionGeneration(all_recommendations)
        return jsonify({'recommended_places': description})
    else:
        return jsonify({'recommended_places': all_recommendations})
