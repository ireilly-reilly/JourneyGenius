# # auth.py

# from flask import Blueprint, jsonify, request, session, make_response
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# from flask_bcrypt import Bcrypt


# auth_bp = Blueprint('auth', __name__)
# bcrypt = Bcrypt()


# from app import db
# from app import User  #Import the User model



# @auth_bp.route('/api/RegisterUser', methods=['POST'])
# def RegisterUser():
#     #Get the data from Vue
#     data = request.json

#     email = data.get('email')
#     firstname = data.get('firstname')
#     lastname = data.get('lastname')
#     password = data.get('password')

#     if not email or not firstname or not lastname or not password:
#         return jsonify({'error': 'Username and password are required'}), 400

#     existing_user = User.query.filter_by(email=email).first()
#     if existing_user:
#         return jsonify({'error': 'Username already exists'}), 400 #TODO Change to 400 later

#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#     new_user = User(email=email, firstname=firstname, lastname=lastname, password=hashed_password)

#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({'message': 'User registered successfully'}), 201


# @auth_bp.route('/api/LoginUser', methods=['POST'])
# def LoginUser():
#     data = request.json

#     email = data.get('email')
#     password = data.get('password')

#     if not email or not password:
#         return jsonify({'error': 'Username and password are required'}), 400

#     user = User.query.filter_by(email=email).first()

#     if user and bcrypt.check_password_hash(user.password, password):
#         #Generate a JWT token
#         access_token = create_access_token(identity=user.id)
#         print("Logging in user... User ID in session: ", user.id)
        
#         return jsonify({'access_token': access_token}), 200
#     else:
#         return jsonify({'error': 'Invalid username or password'}), 401 #TODO change to 401 later 

# @auth_bp.route('/api/check_login_status', methods=['GET'])
# @jwt_required()  #Ensure the request has a valid token
# def check_login_status():
#     current_user_id = get_jwt_identity()
#     print(current_user_id)
#     return jsonify({'message': 'User is logged in', 'user_id': current_user_id}), 200

# @auth_bp.route('/api/LogoutUser', methods=['POST'])
# def logout():
#     response = make_response(jsonify({'message': 'Logout successful'}), 200)
#     response.delete_cookie('login_token')  # Clear the token from the client
#     return response
#     # print("Checking Login status... User ID in session: ", session.get('user_id'))
#     # return jsonify({'message': 'Logout successful'}), 200
