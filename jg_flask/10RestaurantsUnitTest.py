import json
import unittest
from flask import Flask
from TFIDF_ML_Restaurants_Blueprint import restaurantRecommendation_bp, get_recommendations_with_location_and_price
from GetRestaurantsPlacesAPI import getRestaurant_bp

class TestFlaskRoutes(unittest.TestCase):
    def setUp(self): #Creating test Flask app and client
        self.app = Flask(__name__)
        self.app.register_blueprint(restaurantRecommendation_bp)
        self.app.register_blueprint(getRestaurant_bp)
        self.client = self.app.test_client()

    def test_run_ML_model_recommendations_route(self):
        #Mock data for recommendation
        data = {'target_lat_str': '40.730610', 'target_lon_str': '-73.935242', 'desired_price_range_str': '2'}

        response = self.client.post('/run_ML_model_restaurant_recommendations', json=data)#Send request to /run_ML_model_recommendations route in TFIDF file
        self.assertEqual(response.status_code, 200)#Status code 200 means response request received correctly
        self.assertIn(b"recommended_places", response.data) #Checking if response from TFIDF contains "recommended_places", will check for data below

        response_json = json.loads(response.data.decode('utf-8')) #Make response readable
        recommended_places = response_json.get('recommended_places', []) #Pull recommended places from TFIDF response

        expected_places = ["Swansons Nursery", "Chinnie's Kitchen & Bar", "Zoka Coffee Roaster & Tea Company", "Ming Garden", "Imperial Wok", 
                           "Beijing Chinese Cuisine", "Noble Palace", "Cupcake Royale", "Bakery Nouveau", "Brother's Chinese Restaurant"]
        for place in expected_places:
            self.assertIn(place, recommended_places) #Make sure all 10 locations in expected places are in response from TFIDF
    

if __name__ == '__main__':
    unittest.main()
