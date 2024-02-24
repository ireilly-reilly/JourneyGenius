from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the data and preprocess it (same as before)
data = pd.read_csv('restaurant_data.csv', encoding='utf-8')
data['Price Range'] = data['Price Range'].fillna(0)
data['Types'] = data['Types'].fillna('')
data['Address'] = data['Address'].fillna('')
data['Features'] = data['Types'] + ' ' + data['Address'] + ' ' + data['Price Range'].astype(str)
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(data['Features'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
CORS(app, supports_credentials=True)

# Define the Haversine function
def haversine(lat1, lon1, lat2, lon2):
    # Implementation of haversine function
    R = 6371.0
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = R * c
    return distance

# Define the recommendation function
def get_recommendations_with_location_and_price(place_name, Latitude, Longitude, desired_price):
    idx = data[data['Place'] == place_name].index[0]
    input_price = int(data['Price Range'][idx])
    input_lat = data['Latitude'].iloc[idx]
    input_lon = data['Longitude'].iloc[idx]
    distances = [haversine(input_lat, input_lon, lat, lon) for lat, lon in zip(data['Latitude'], data['Longitude'])]
    text_similarities = cosine_sim[idx]
    price_differences = [abs(input_price - price) for price in data['Price Range']]
    composite_scores = [(1 - text_sim) + (1 - dist / max(distances)) + (1 - price_diff / max(price_differences))
                        for text_sim, dist, price_diff in zip(text_similarities, distances, price_differences)]
    sorted_places = [place for _, place in sorted(zip(composite_scores, data['Place']), reverse=True)]
    return sorted_places[1:11]

@app.route('/generate_itinerary', methods=['POST'])
def generate_itinerary():
    request_data = request.json
    place_name = request_data['place_name']
    latitude = request_data['latitude']
    longitude = request_data['longitude']
    desired_price_range = request_data['desired_price_range']

    recommended_places = get_recommendations_with_location_and_price(place_name, latitude, longitude, desired_price_range)
    return jsonify(recommended_places)

if __name__ == '__main__':
    app.run(debug=True)
