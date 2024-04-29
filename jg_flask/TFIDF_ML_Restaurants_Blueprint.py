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
restaurantRecommendation_bp = Blueprint('restaurantRecommendation_bp', __name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CSV_FOLDER = os.path.join(BASE_DIR, '..', 'journey-genius-data-scraping')
restaurant_csv_file_path = os.path.join(CSV_FOLDER, 'restaurant_data.csv')

data = pd.read_csv(restaurant_csv_file_path)

# data = pd.read_csv('JouneyGenius/journey-genius-data-scraping/restaurant_data.csv', encoding='utf-8')

# Preprocess the "Price Range" column
# Fill missing values with 0 (unknown)
data['Price Range'] = data['Price Range'].fillna(0)
# print(data['Price Range'])

# Preprocess the data and extract relevant features
# Include 'Price Range' as a feature
data['Types'] = data['Types'].fillna('')
data['Address'] = data['Address'].fillna('')
data['Features'] = data['Types'] + ' ' + data['Address'] + ' ' + data['Price Range'].astype(str)
# print(data['Types'])
# print(data['Address'])

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


# Calculate semantic similarity between two strings
def calculate_semantic_similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    similarity_score = doc1.similarity(doc2)
    return similarity_score


# Modified code snippet to get recommendations with location and price
def get_recommendations_with_location_and_price(target_place, input_lat, input_lon, input_price, input_keyword, State):
    recommendations = []
    idx = data[(data['Place'].str.strip().str.lower() == target_place.lower().strip()) & (data['Category'].str.strip().str.lower().str.contains(input_keyword.lower().strip()))].index

    if idx.empty:
        print(f"No matching places found for {target_place}")
        return []

    idx = idx[0]

    input_price = int(data.loc[idx, 'Price Range'])
    input_lat = data.loc[idx, 'Latitude']
    input_lon = data.loc[idx, 'Longitude']

    filtered_data = data[(data['Category'] == input_keyword) & (data['State'] == State)]
    
    distances = [haversine(input_lat, input_lon, lat, lon) for lat, lon in zip(filtered_data['Latitude'], filtered_data['Longitude'])]
    text_similarities = [cosine_sim[idx][i] for i in filtered_data.index]
    price_differences = [abs(input_price - price) for price in filtered_data['Price Range']]
    semantic_similarities = [calculate_semantic_similarity(data.loc[i, 'Place'], target_place) for i in filtered_data.index]

    max_distance = max(distances) if distances else 1
    max_price_diff = max(price_differences) if price_differences else 1
    max_semantic_sim = max(semantic_similarities) if semantic_similarities else 1

    composite_scores = [(0.01 * (1 - text_sim) + 2 * (1 - dist / max_distance) + 0.8 * (1 - price_diff / max_price_diff) + 0.3 * (1 - semantic_sim / max_semantic_sim))
                        for text_sim, dist, price_diff, semantic_sim in zip(text_similarities, distances, price_differences, semantic_similarities)]
    
    sorted_data = sorted(zip(composite_scores, filtered_data['Place']), reverse=True)
    recommendations = [{'place': place, 'score': score} for score, place in sorted_data[:5]]

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
        prompt = f"Describe the restaurant {place} regarding its food from online sources in one or two sentences. Do not response with Im sorry, but as an AI model, I am unable to browse the internet. If this happens then make something up. Answer in this format- (Restaurant Name): (Then description). Note: do not take score into consideration."


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

def rank_recommendations(all_recommendations):

    if not all_recommendations:
        print("No recommendations to rank.")
        return []

    # Sort the recommendations by the 'score' key in descending order
    sorted_recommendations = sorted(all_recommendations, key=lambda x: x['score'], reverse=True)

    print("Sorted recommendations:", sorted_recommendations[:5])  

    # Return the top 5 recommendations
    return sorted_recommendations[:5]



@restaurantRecommendation_bp.route('/run_ML_model_restaurant_recommendations', methods=['POST'])
@jwt_required()
def recommend():
    current_user_id = get_jwt_identity()
    # Get the user from the database
    user = User.query.filter_by(id=current_user_id).first()

    target_categories = parse_data(user.fav_foods)
    print("target categories: ", target_categories)
    iteration = 0

    # Grab city name from front end
    try:
        data = request.json
        city = str(data.get('desired_city'))
        state = str(data.get('desired_state'))
        target_lat_str = data.get('target_lat_str')
        target_lon_str = data.get('target_lon_str')
        desired_price_range_str = data.get('desired_price_range_str')
        descriptionToggle = data.get('descriptionToggle')
        print(city + ", " + stateMappings[state])
    except Exception as e:
        print("Can't get city:", e)

    # Initialize a list to store recommended places and keywords
    target_foods = []
    keywords = []


    # Initialize a list to store recommended places
    recommended_places = []
    all_recommendations = []
    ranked_recommendations = []

    df = pd.read_csv(restaurant_csv_file_path)
    for target_category in target_categories:
        print("Processing Category:", target_category)

        # Custom adjustments based on category
        if target_category == 'east asian':
            keyword = "chinese vietnamese"
        elif target_category == 'south asian':
            keyword = "indian thai"
        elif target_category == 'east asian 2':
            keyword = "japanese korean"
        elif target_category == 'specialty food types':
            keyword = "seafood sushi steakhouse buffet"
        elif target_category == 'european & mediterranean':
            keyword = "italian french pizzeria mediterranean"
        elif target_category == 'dietary-focused':
            keyword = "vegan vegetarian"
        else:
            keyword = target_category  # Default to using the category directly

        # print(f"Current Keyword: {keyword}")
        keywords.append(keyword)
        print(keywords)

        try:
            # Try to find a restaurant with the desired price range
            first_row = df[(df['City'] == city) & (df['State'] == stateMappings[state]) & (df['Price Range'] == desired_price_range_str) & (df['Category'] == keyword)].iloc[0]
            iteration += 1
            # print(iteration)
            # print(" iteration")
        except IndexError:
            try:
                # If no restaurants are found with the desired price range, try defaulting to 2
                first_row = df[(df['City'] == city) & (df['State'] == stateMappings[state]) & (df['Price Range'] == 2) & (df['Types'] == 'restaurant')].iloc[0]
            except IndexError as e:
                print("No restaurants found for the specified city with the default price range.")
                # Handle the case where no restaurants are found with the default price range
                # You may want to return an error message or handle this scenario accordingly
                message = {
                    message : "nothing in it bruh"
                }
                return jsonify(message)
        # Process the first row found
        if not first_row.empty:
            first_row_with_city = first_row
            # target_foods = str(first_row_with_city['Place'])
            target_foods.append(first_row_with_city['Place'])
        else:
            print("No rows found for the specified city.")

    print("Total target food/s")
    print(target_foods)
    print("Total target keyword/s")
    print(keywords)

    # recommended_places = []

    iteration = 0
    # for target_food in target_foods:
    for target_food, keyword in zip(target_foods, keywords):
        iteration += 1
        print("Iteration: ", iteration)
        print(target_food)
        print(keyword)
        try:
            # print("Target Latitude: ", target_lat_str)
            # print("Target Longitude: ", target_lon_str)
            # print("Desired Price Range: ", desired_price_range_str)

            # Check if latitude, longitude, and price range are not None
            if None in (target_lat_str, target_lon_str, desired_price_range_str):
                return jsonify({'error': 'Latitude, longitude, or price range is missing or invalid'}), 400

            # Convert latitude, longitude, and price range to float and int respectively
            try:
                target_lat = float(target_lat_str)
                target_lon = float(target_lon_str)
                desired_price_range = int(desired_price_range_str)
            except ValueError as e:
                print(f"Error converting latitude, longitude, or price range: {e}")
                return jsonify({'error': 'Invalid parameter values'}), 400
            State = stateMappings[state]
            print("before calling function: ", State)
            print(target_food)
            recommended_places = get_recommendations_with_location_and_price(target_food, target_lat, target_lon, desired_price_range, keyword, State)
            print(recommended_places)
            print("recommended places type:", type(recommended_places))
            # place_names = recommended_places


            # Extend all_recommendations with recommendations for this target food
            all_recommendations.extend(recommended_places)

        except Exception as e:
            # Log the exception for debugging purposes
            print(f"Error processing request: {e}")
            return jsonify({'error': 'An unexpected error occurred'}), 500

    if (descriptionToggle == True):
        ranked_recommendations = rank_recommendations(all_recommendations)
        description = descriptionGeneration(ranked_recommendations)
        return jsonify({'recommended_places': description})
    else:
        # Extract place names if you need to use just the names elsewhere
        ranked_recommendations = rank_recommendations(all_recommendations)
        place_names = [recommendation['place'] for recommendation in ranked_recommendations]
        print("Place names from ranked recommendations:", place_names)

        return jsonify({'recommended_places': place_names})