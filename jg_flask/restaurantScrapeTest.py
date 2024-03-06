import json
import unittest
from flask import Flask
from GetRestaurantsPlacesAPI import getRestaurant_bp

class TestScrapeRestaurants(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(getRestaurant_bp)
        self.client = self.app.test_client()

    def test_scrape_restaurants_route_success(self):
        #Send a request to /scrape_restaurants route with valid coordinates
        response = self.client.post('/scrape_restaurants', json={'target_lat_str': '40.730610', 'target_lon_str': '-73.935242'})
        self.assertEqual(response.status_code, 200) #code 200 means the request was received correctly
        self.assertIn(b"Restaurant data scraped successfully!", response.data)
        #Receiving code 200 and success message = restaurant data written to csv correctly

    def test_scrape_restaurants_missing_coordinates(self):
        #Send a request to /scrape_restaurants route without coordinates
        response = self.client.post('/scrape_restaurants', json={})
        self.assertEqual(response.status_code, 400) #Status code 400 means bad request
        self.assertIn(b"Latitude or longitude is missing/invalid", response.data) #Check for error message

    def test_scrape_restaurants_invalid_coordinates(self):
        #Send a request to /scrape_restaurants route with invalid coordinates
        response = self.client.post('/scrape_restaurants', json={'target_lat_str': 'invalid', 'target_lon_str': 'invalid'})
        self.assertEqual(response.status_code, 400) #Status code 400 means bad request
        self.assertIn(b"Invalid parameter values", response.data) #Check for error message

if __name__ == '__main__':
    unittest.main()
