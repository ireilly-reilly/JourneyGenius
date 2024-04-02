from flask import Blueprint, jsonify, request
import requests
import pandas as pd

# Define description blueprint
FetchSelectedInformation_bp = Blueprint('FetchSelectedInformation_bp', __name__)

# Define route to handle description request
@FetchSelectedInformation_bp.route('/process_data', methods=['POST'])

# Function to fetch restaurants from Flask API
def process_data():
    try:
        # Extract data received from Vue.js
        data = request.json

        # Extract relevant variables from the data
        activities = data.get('activities')
        landmarks = data.get('landmarks')
        foods = data.get('foods')
        shops = data.get('shops')
        hotels = data.get('hotels')
        datesData = data.get('datesData')
        budget = data.get('budget')
        stateData = data.get('stateData')
        city = data.get('city')
        lat = data.get('lat')
        long = data.get('long')
        cityDescription = data.get('cityDescription')
        citySlogan = data.get('citySlogan')

        # Process the received data as needed
        # For example, you can manipulate CSV file based on this data
        print("Received data:")
        print("Activities:", activities)
        print("Landmarks:", landmarks)
        print("Foods:", foods)
        print("Shops:", shops)
        print("Hotels:", hotels)
        print("Dates Data:", datesData)
        print("Budget:", budget)
        print("State Data:", stateData)
        print("City:", city)
        print("Latitude:", lat)
        print("Longitude:", long)
        print("City Description:", cityDescription)
        print("City Slogan:", citySlogan)

        # Perform further operations on the received data

        # Return a response indicating that the data was received and processed successfully
        return jsonify({'message': 'Data received and processed successfully'})

    except Exception as e:
        # Handle any errors that occur during processing
        print("Error processing data:", e)
        return jsonify({'error': 'An error occurred while processing the data'})


# # Function to manipulate CSV file based on fetched restaurants
# def manipulate_csv(restaurants):
#     try:
#         # Load CSV file
#         df = pd.read_csv('your_csv_file.csv')

#         # Manipulate CSV file based on fetched restaurants
#         # For example, you can select a different column based on the restaurants
#         if 'Activity 1' in restaurants:
#             selected_column = df['Column_A']
#         elif 'Activity 2' in restaurants:
#             selected_column = df['Column_B']
#         else:
#             selected_column = df['Column_C']

#         # Perform further operations on selected_column or save it to a new CSV file
#         # Example: selected_column.to_csv('output.csv', index=False)

#         print("CSV manipulation completed")
#     except Exception as e:
#         print("Error manipulating CSV:", e)

# # Main function
# def main():
#     # Fetch restaurants from Flask API
#     restaurants = fetch_restaurants_from_api()

#     # If restaurants are fetched successfully, manipulate CSV file
#     if restaurants:
#         manipulate_csv(restaurants)

# if __name__ == '__main__':
#     main()
