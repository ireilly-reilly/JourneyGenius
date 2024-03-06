import unittest
from app import app, db, User

class TestAuthFunctionality(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register_user(self):
        with app.test_request_context():
            #Register new user
            data = {'email': 'test@example.com', 'firstname': 'Mitch', 'lastname': 'Sorrenstein', 'password': 'password'}
            response = self.app.post('/api/RegisterUser', json=data)
            self.assertEqual(response.status_code, 201)

            #See if user is added to database
            user = User.query.filter_by(email='test@example.com').first()
            self.assertIsNotNone(user)

    def test_login_user(self):
        with app.test_request_context():
            #Login with invalid credentials
            data = {'email': 'test@example.com', 'password': 'password'}
            response = self.app.post('/api/LoginUser', json=data)
            self.assertEqual(response.status_code, 401)  #401 for invalid credentials

            #Creating an account
            data = {'email': 'test@example.com', 'firstname': 'Mitch', 'lastname': 'Sorrenstein', 'password': 'password'}
            response = self.app.post('/api/RegisterUser', json=data)
            self.assertEqual(response.status_code, 201)

            #Logging in with valid credentials
            response = self.app.post('/api/LoginUser', json=data)
            self.assertEqual(response.status_code, 200)

    def test_logout_user(self):
        with app.test_request_context():
            #Creating an account
            data = {'email': 'test@example.com', 'firstname': 'Mitch', 'lastname': 'Sorrenstein', 'password': 'password'}
            response = self.app.post('/api/RegisterUser', json=data)
            self.assertEqual(response.status_code, 201)

            #Logging in with valid credentials
            response = self.app.post('/api/LoginUser', json=data)
            self.assertEqual(response.status_code, 200)

            #Logging out user
            response = self.app.post('/api/LogoutUser')
            self.assertEqual(response.status_code, 200) #200 for successful logout

if __name__ == '__main__':
    unittest.main()
