import json
import unittest
from flask import Flask
from FetchSelectedInformation_bp import FetchSelectedInformation_bp, process_data

class TestFetchPhotos(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(FetchSelectedInformation_bp)
        self.client = self.app.test_client()

    def test_fetch_photos_route(self):
        # Mock data for fetching photos
        data = {'foods': ["Rico's Mexican Food", 'China Kitchen']}  # Example list of restaurants

        response = self.client.post('/process_data', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"photo_urls", response.data)  # Checking if response contains "photo_urls"

        response_json = json.loads(response.data.decode('utf-8'))  # Make response readable
        photo_urls = response_json.get('photo_urls', [])  # Pull photo URLs from response

        # Example list of expected photo URLs
        expected_urls = [
            "https://lh3.googleusercontent.com/places/ANXAkqGvalQfk1eB12TFjNfFK0Jk3TlfpAnQisiPqvunhTajAUp92cexXXDzPA9giNjV3VV6YdYlA1cJzwayzVBCmncqKpAO5BtKpJQ=s1600-w400",
            "https://lh3.googleusercontent.com/places/ANXAkqEbc1OXIIEsQ9LSyEw5UwaHwdl2dB9w0iDe4r7xIiQzijUisWXS3S-r7k3r58bu_9JpN3CGMuubmvn8p509DS1f6hYI3fZNseM=s1600-w400"
        ]
        
        # Ensure all expected photo URLs are in the response
        for url in expected_urls:
            self.assertIn(url, photo_urls)


if __name__ == '__main__':
    unittest.main()
