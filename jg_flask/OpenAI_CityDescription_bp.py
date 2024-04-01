# Import necessary modules and functions
from flask import Blueprint, jsonify, request
from openai import OpenAI
from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Define description blueprint
cityDescription_bp = Blueprint('cityDescription_bp', __name__)

# Define route to handle description request
@cityDescription_bp.route('/cityDescription_bp', methods=['POST'])
def descript_bp():
    try: 
        # data = request.json
        # Stores 10 recommendations in the variable below for GPT
        recommended_places = TF.get_recommendations_with_location_and_price()
    except Exception as e:
        print("Something's fucked up:", e)

    # Compose a prompt using recommended places
    prompt = "Describe the following restaurants regarding its food from online sources in one or two sentences:\n" + "\n".join(recommended_places)

    # Generate descriptions using OpenAI
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an experienced food critic."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract and return the generated description
    generated_description = completion.choices[0].message
    return jsonify({'description': generated_description})


