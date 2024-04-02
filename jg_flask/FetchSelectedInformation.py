import requests
import pandas as pd

# Function to fetch restaurants from Flask API
def fetch_restaurants_from_api():
    try:
        # Make a GET request to fetch restaurants from Flask API
        response = requests.get('http://localhost:8080/GeneratedItinerary')

        # Check if request was successful
        if response.status_code == 200:
            # Extract restaurants data from response JSON
            restaurants = response.json()['foods']
            print("restaurants:", restaurants)
            return restaurants
        else:
            print("Failed to fetch restaurants")
            return None
    except Exception as e:
        print("Error fetching restaurants:", e)
        return None

restaurant = fetch_restaurants_from_api()
print(restaurant)

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
