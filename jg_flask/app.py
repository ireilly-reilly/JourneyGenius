from datetime import datetime
import click
from flask import Flask, jsonify, request, session, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import secrets
import os
from flask_migrate import Migrate
from dotenv import load_dotenv


#Blueprint imports
from TFIDF_ML_Restaurants_Blueprint import restaurantRecommendation_bp
from GetRestaurantsPlacesAPI import getRestaurant_bp
from TFIDF_ML_Activities_Blueprint import activitiesRecommendation_bp
from GetActivitiesPlacesAPI import getActivity_bp
from TFIDF_ML_Landmarks_Blueprint import landmarksRecommendation_bp
from GetLandmarksPlacesAPI import getLandMark_bp
from TFIDF_ML_Shopping_Blueprint import shoppingRecommendation_bp
from GetShoppingPlacesAPI import getShopping_bp
from TFIDF_ML_Hotels_Blueprint import hotelsRecommendation_bp
from GetHotelsPlacesAPI import getHotels_bp
from OpenAI_CityDescription_bp import cityDescription_bp
from OpenAI_CitySlogan_bp import citySlogan_bp
from FetchSelectedInformation_bp import FetchSelectedInformation_bp
# from GetSavedTrip import saved_trips_bp



#from email_verification import email_verification_bp

#This loads .env for database migrations
load_dotenv()




#Get database information securely
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

#Flask App Initializations
app = Flask(__name__, static_folder='../journey-genius-ui/dist', static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})
# CORS(app, resources={r"/api/*": {"origins": "*"}})


#Register blueprints TODO Refactor into bluprints to make it nicer!
app.register_blueprint(restaurantRecommendation_bp, url_prefix='/api')
app.register_blueprint(getRestaurant_bp, url_prefix='/api')
app.register_blueprint(activitiesRecommendation_bp, url_prefix='/api')
app.register_blueprint(getActivity_bp, url_prefix='/api')
app.register_blueprint(landmarksRecommendation_bp, url_prefix='/api')
app.register_blueprint(getLandMark_bp, url_prefix='/api')
app.register_blueprint(shoppingRecommendation_bp, url_prefix='/api')
app.register_blueprint(getShopping_bp, url_prefix='/api')
app.register_blueprint(getHotels_bp, url_prefix='/api')
app.register_blueprint(hotelsRecommendation_bp, url_prefix='/api')
app.register_blueprint(cityDescription_bp, url_prefix='/api')
app.register_blueprint(citySlogan_bp, url_prefix='/api')
app.register_blueprint(FetchSelectedInformation_bp, url_prefix='/api')
# app.register_blueprint(saved_trips_bp, url_prefix='/api')



CORS(app, supports_credentials=True)

#       |----------------------------------DATABASE MIGRATION INFO----------------------------------|
#       |    After making desired changes to tables or pulling modified database code               |
#       |    In command line, run:                                                                  |
#       |        flask db migrate -m "<your message>"                                               |
#       |    Then enter the mysql command prompt:                                                   |
#       |        mysql -u root -p                                                                   |
#       |    Enter password                                                                         |
#       |    In mysql command prompt, run:                                                          |
#       |        GRANT ALL PRIVILEGES ON useraccounts.user TO 'JourneyGenius'@'localhost';          |
#       |        GRANT ALL PRIVILEGES ON useraccounts.super_user TO 'JourneyGenius'@'localhost';    |
#       |        GRANT ALL PRIVILEGES ON useraccounts.trip TO 'JourneyGenius'@'localhost';          |
#       |        FLUSH PRIVILEGES;                                                                  |
#       |        exit                                                                               |
#       |    Then in command line, run:                                                             |
#       |        flask db upgrade                                                                   |
#       |                                                                                           |
#       |    This will save all entries in current                                                  | 
#       |    database and implement new changes!                                                    |
#       |___________________________________________________________________________________________|

#User Table Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(40), nullable=False)
    gender = db.Column(db.String(5))
    age = db.Column(db.String(5))
    interests = db.Column(db.String(10))
    accommodations = db.Column(db.String(5))
    transportation = db.Column(db.String(5))
    last_login = db.Column(db.String(50))
    date_created = db.Column(db.String(50))

#SuperUser Table Model:
class SuperUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(40), nullable=False)

class Trip(db.Model):
    #Strings
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    dates = db.Column(db.String(100), nullable=False)
    trip_length = db.Column(db.Integer)
    budget = db.Column(db.String(50))
    city_description = db.Column(db.Text)
    city_slogan = db.Column(db.String(100))
    
    #Arrays of strings
    activities = db.Column(db.JSON)  # Example: ["hiking", "sightseeing"]
    landmarks = db.Column(db.JSON)   # Example: ["Statue of Liberty", "Golden Gate Bridge"]
    shops = db.Column(db.JSON)       # Example: ["local markets", "boutiques"]
    foods = db.Column(db.JSON)       # Example: ["Italian cuisine", "street food"]
    hotels = db.Column(db.JSON)      # Example: ["luxury resorts", "budget hotels"]
    
    #Pictures
    activities_images = db.Column(db.JSON)  # Example: ["activity1.jpg", "activity2.png"]
    landmarks_images = db.Column(db.JSON)   # Example: ["landmark1.jpg", "landmark2.png"]
    shops_images = db.Column(db.JSON)       # Example: ["shop1.jpg", "shop2.png"]
    foods_images = db.Column(db.JSON)       # Example: ["food1.jpg", "food2.png"]
    hotels_images = db.Column(db.JSON)      # Example: ["hotel1.jpg", "https://example.com/hotel2.png"]

#Blueprints requiring database info go here because of circular import issues (idk why)
from SuperuserAccounts import superuser_accounts_bp
from SavedTrips_bp import saved_trips_bp
app.register_blueprint(superuser_accounts_bp, url_prefix='/api')
app.register_blueprint(saved_trips_bp, url_prefix='/api')

#This is a command line prompt to create an initial super user
#Used like this: flask create_super_user
@app.cli.command("create_super_user")
def create_super_user():
    email = click.prompt("Enter email")
    password = click.prompt("Enter password", hide_input=True, confirmation_prompt=True)
    firstname = click.prompt("Enter firstname")
    lastname = click.prompt("Enter lastname")

    existing_user = SuperUser.query.filter_by(email=email).first()
    if existing_user:
        print("Username already exists.")
    else:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        super_user = SuperUser(email=email, password=hashed_password, firstname=firstname, lastname=lastname)
        db.session.add(super_user)
        db.session.commit()
        print("SuperUser created successfully.")


#Route to register new users
@app.route('/api/RegisterUser', methods=['POST'])
def RegisterUser():
    #Get the data from Vue
    data = request.json

    email = data.get('email')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    password = data.get('password')

    if not email or not firstname or not lastname or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 400 #TODO Change to 400 later

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    date_created = datetime.utcnow().replace(microsecond=0)
    new_user = User(email=email, firstname=firstname, lastname=lastname, password=hashed_password, date_created=date_created)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

#Route to login existing user
@app.route('/api/LoginUser', methods = ['POST'])
def LoginUser():
    data = request.json

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        #Generate a JWT token
        access_token = create_access_token(identity=user.id)
        user.last_login = datetime.utcnow().replace(microsecond=0)
        db.session.commit()
        print("Logging in user... User ID in session: ", user.id)
        
        return jsonify({'access_token': access_token, 'user_id': user.id}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401 #TODO change to 401 later 
    

#Route to login superuser
@app.route('/api/LoginSuperUser', methods = ['POST'])
def LoginSuperUser():
    data = request.json

    email = data.get('email')
    password = data.get('password')


    if not email or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    super_user = SuperUser.query.filter_by(email=email).first()
    if super_user:
        stored_password_hash = super_user.password

    print(bcrypt.check_password_hash(super_user.password, password))
    if super_user and bcrypt.check_password_hash(super_user.password, password):
        #Generate a JWT token
        access_token = create_access_token(identity=super_user.id)
        print("Logging in user... User ID in session: ", super_user.id)
        
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401 #TODO change to 401 later

#Route to check login status
@app.route('/api/check_login_status', methods=['GET'])
@jwt_required()  #Ensure the request has a valid token
def check_login_status():
    current_user_id = get_jwt_identity()
    print(current_user_id)
    return jsonify({'message': 'User is logged in', 'user_id': current_user_id}), 200

#Route to logout user
@app.route('/api/LogoutUser', methods=['POST'])
def logout():
    response = make_response(jsonify({'message': 'Logout successful'}), 200)
    response.delete_cookie('login_token')  # Clear the token from the client
    response.delete_cookie('database_id')
    return response
    # print("Checking Login status... User ID in session: ", session.get('user_id'))
    # return jsonify({'message': 'Logout successful'}), 200



#TODO Refactor into separate blueprint
#---------------------USER PROFILING METHODS--------------------------

# @app.route('/api/GetUserProfile', methods=['GET'])
# @jwt_required()
# def fetchUserData():
#     print("hello from fetchUserData")
#     current_user_id = get_jwt_identity()
# #     #current_user_id = user.id
# #     print('Current user ID: ', current_user_id)
#     user = User.query.get(current_user_id)

#     if user:
# #         #Convert user data to a dictionary and send it as JSON response
# #         user_data = {
# #             'firstName': user.firstname,
# #             'lastName': user.lastname,
# #             'email': user.email,
# #             # Add other fields as needed
# #         }
# #         return jsonify(user_data), 200
# #     else:
# #         print("Current User ID: ", current_user_id)
# #         print('error')
# #         return jsonify({'error': 'User not found from fetch data'}), 404


@app.route('/api/save_user_data', methods=['POST'])
@jwt_required()  # Ensure the request has a valid JWT token
def save_user_data():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    user.firstname = data.get('firstName')
    user.lastname = data.get('lastName')
    user.gender = data.get('gender')
    user.age = data.get('age')
    user.email = data.get('email')
    user.accommodations = data.get('accommodationPreference')
    user.transportation = data.get('transportationPreference')
    user.interests = ','.join(data.get('selectedActivities'))

    db.session.commit()

    return jsonify({'message': 'Data saved successfully'}), 200


@app.route('/api/get_user_info', methods=['GET'])
@jwt_required()  
def get_user_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    user_data = {
        'firstName': user.firstname,
        # 'lastName': user.lastname,
        # 'gender': user.gender,
        # 'age': user.age,
        # 'email': user.email,
        # 'accommodationPreference': user.accommodations,
        # 'transportationPreference': user.transportation,
        # 'selectedActivities': user.interests.split(',')
    }

    return jsonify(user_data), 200

#Route to fetch super user's name
@app.route('/api/GetSuperuserName', methods=['GET'])
@jwt_required()
def get_superuser_name():
    current_user_id = get_jwt_identity()
    super_user = SuperUser.query.get(current_user_id)

    if not super_user:
        return jsonify({'error': 'Super user not found'}), 404

    return jsonify({'name': super_user.firstname + ' ' + super_user.lastname}), 200





if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True) #Runs on port 8000!!!
