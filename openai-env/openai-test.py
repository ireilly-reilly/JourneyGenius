from openai import OpenAI
from dotenv import load_dotenv
import os
import TFIDF_ML_Recommendations_Blueprint as TF

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# # Function to invoke TF-IDF script and capture output
# def get_recommendations_from_tfidf():
#     # Call the TF-IDF script using subprocess and capture its output
#     process = subprocess.Popen(["python", "/Users/dontstealmyshxt/Github/JourneyGenius/journey-genius-data-scraping/TFIDF_ML.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     output, error = process.communicate()
#     print("Output:", output.decode('utf-8'))  # Print the output
#     print("Error:", error.decode('utf-8'))    # Print the error
#     # Decode the byte output to string and parse it as JSON
#     recommendations = json.loads(output.decode('utf-8'))

# Get recommendations from TF-IDF script
# recommended_places = get_recommendations_from_tfidf()

target_place = "SF Kitchen"

target_lat = 39.5296  # Latitude of SF Kitchen
target_lon = -119.8138  # Longitude of SF Kitchen
desired_price_range = 2  # Desired price range
recommended_places = TF.get_recommendations_with_location_and_price(target_place, target_lat, target_lon, desired_price_range)
print(recommended_places)




# Initialize OpenAI client
client = OpenAI(api_key=api_key)

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

# Return the generated description


# Print the generated description
print(completion.choices[0].message)
