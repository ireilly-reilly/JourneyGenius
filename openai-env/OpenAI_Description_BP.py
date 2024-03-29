# Import necessary modules and functions
from flask import Blueprint, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import requests
import os
import TFIDF_ML_Recommendations_Blueprint as TF

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Define description blueprint
description_bp = Blueprint('description', __name__)

# Define route to handle description request
@description_bp.route('/descript', methods=['POST'])
def descript():
    # Extract data from request (if needed)
    # For example, you might receive user preferences as JSON data in the request
    
    # Get descriptions from TF-IDF script
    target_place = "SF Kitchen"
    target_lat = 39.5296
    target_lon = -119.8138
    desired_price_range = 2
    recommended_places = TF.get_descriptions_with_location_and_price(target_place, target_lat, target_lon, desired_price_range)

    # Compose a prompt using recommended places
    prompt = "Describe the following restaurants from online sources:\n" + "\n".join(recommended_places)

    # Generate descriptions using OpenAI
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an experienced food critic."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract and return the generated description
    generated_description = completion.choices[0].message
    return jsonify({'description': generated_description})


# #Define description blueprint
# description_bp = Blueprint('description', __name__)

# # Define route to handle description request
# @description_bp.route('/generate_description', methods=['POST'])
# def generate_description():
#     try:
#         # Extract data from the request
#         data = request.json
#         prompt = data.get('prompt')

#         # Check if prompt is provided
#         if prompt is None:
#             return jsonify({'error': 'Prompt is missing in the request'}), 400

#         # Generate description using OpenAI
#         description = generate_description_with_openai(prompt)

#         # Return the generated description
#         return jsonify({'description': description})

#     except Exception as e:
#         # Log the exception for debugging purposes
#         print(f"Error processing request: {e}")
#         return jsonify({'error': 'An unexpected error occurred'}), 500

