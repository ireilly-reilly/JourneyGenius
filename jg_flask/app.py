from flask import Flask, jsonify, request, session, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import secrets


#Blueprint imports
from TFIDF_ML_Restaurants_Blueprint import restaurantRecommendation_bp
from GetRestaurantsPlacesAPI import getRestaurant_bp
from TFIDF_ML_Activities_Blueprint import activitiesRecommendation_bp
from GetActivitiesPlacesAPI import getActivity_bp
from TFIDF_ML_Landmarks_Blueprint import landmarksRecommendation_bp
from GetLandmarksPlacesAPI import getLandMark_bp
from TFIDF_ML_Shopping_Blueprint import shoppingRecommendation_bp
from GetShoppingPlacesAPI import getShopping_bp
#from GetHotelsPlacesAPI import getHotels_bp


#from email_verification import email_verification_bp

#Flask App Initializations
app = Flask(__name__, static_folder='../journey-genius-ui/dist', static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://JourneyGenius:WanderDeezNutz@localhost/useraccounts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
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
#app.register_blueprint(getHotels_bp, url_prefix='/api')


CORS(app, supports_credentials=True)


#app.register_blueprint(auth_bp)#, url_prefix='/auth') <--might add later
#app.register_blueprint(email_verification_bp)

#Format for 'Users' in database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(40), nullable=False)
    gender = db.Column(db.String(5))
    age = db.Column(db.String(5))
    interests = db.Column(db.String(10))
    accommodations = db.Column(db.String(5))
    transportation = db.Column(db.String(5))

# Create the database tables (including the User table)
# db.create_all()


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
    new_user = User(email=email, firstname=firstname, lastname=lastname, password=hashed_password)

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
        print("Logging in user... User ID in session: ", user.id)
        
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


@app.route('/api/get_user_profile', methods=['GET'])
@jwt_required()  
def get_user_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    user_data = {
        'firstName': user.firstname,
        'lastName': user.lastname,
        'gender': user.gender,
        'age': user.age,
        'email': user.email,
        'accommodationPreference': user.accommodations,
        'transportationPreference': user.transportation,
        'selectedActivities': user.interests.split(',')
    }

    return jsonify(user_data), 200





if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True) #Runs on port 8000!!!
