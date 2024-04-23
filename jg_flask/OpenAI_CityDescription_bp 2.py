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
@cityDescription_bp.route('/generateDescription', methods=['POST'])
def descript_bp():
    try: 
        city = request.json.get("city")
        state = request.json.get("state")
        locationObj = (city + ", " + state)
        location = str(locationObj)
        # print(location)
        
    except Exception as e:
        print("Something's messed up:", e)

    # Compose a prompt using recommended places
    prompt = "Describe the following following location in 3-4 sentences. Highlight what makes this location special: " + location

    # Generate descriptions using OpenAI
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a tour guide."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract and append the description to response_message_array
    response_message = response.choices[0].message.content

    return jsonify(response_message)


