import json
import unittest
from flask import Flask
from TFIDF_ML_Restaurants_Blueprint import restaurantRecommendation_bp, get_recommendations_with_location_and_price

class TestFlaskRoutes(unittest.TestCase):
    def setUp(self): 
        self.app = Flask(__name__)
        self.app.register_blueprint(restaurantRecommendation_bp)
        self.client = self.app.test_client()

    def test_run_ML_model_recommendations_route(self):
        data = {'target_lat_str': '40.730610', 'target_lon_str': '-73.935242', 'desired_price_range_str': '2'}
        response = self.client.post('/run_ML_model_restaurant_recommendations', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"recommended_places", response.data)

        response_json = json.loads(response.data.decode('utf-8'))
        recommended_places = response_json.get('recommended_places', [])

        expected_places = ["Swansons Nursery", "Chinnie's Kitchen & Bar", "Zoka Coffee Roaster & Tea Company", "Ming Garden", "Imperial Wok", 
                           "Beijing Chinese Cuisine", "Noble Palace", "Cupcake Royale", "Bakery Nouveau", "Brother's Chinese Restaurant"]
        for place in expected_places:
            self.assertIn(place, recommended_places)

if __name__ == '__main__':
    unittest.main()
