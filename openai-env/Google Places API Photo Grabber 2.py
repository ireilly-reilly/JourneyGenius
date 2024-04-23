import googlemaps
import csv
import os
import pandas as pd
import TFIDF_ML as TF

# Define the API Key that is being used
api_key = 'AIzaSyDGC5QtIMrpN1HXPJpamkDhgfVUkq9Jw8Y'

# Define our Client
gmaps = googlemaps.Client(key=api_key)

# Grab returned results from below function to generate pictures
returned_locations = get_recommendations_with_location_and_price(place_name, Latitude, Longitude, desired_price, cosine_sim=cosine_sim):

