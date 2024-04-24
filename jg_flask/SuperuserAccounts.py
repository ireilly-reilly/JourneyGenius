from flask import Blueprint, jsonify, request, g
from app import db  # Import your SQLAlchemy instance
from app import User  # Import your User model
from app import Trip
from app import bcrypt

#Create the blueprint object
superuser_accounts_bp = Blueprint('superuser_accounts', __name__, url_prefix='/api')

# # Custom function to check if the user is a superuser
# def require_superuser():
#     if not getattr(g, 'user', None) or not g.user.is_superuser:
#         return jsonify({'error': 'Access denied. Superuser privileges required.'}), 403

# # Add before_request hook to check if the user is a superuser for certain routes
# @superuser_accounts_bp.before_request
# def before_request():
#     if request.endpoint in ['superuser_accounts.get_user_accounts',
#                             'superuser_accounts.freeze_user_account',
#                             'superuser_accounts.delete_trips',
#                             'superuser_accounts.delete_user_account']:
#         return require_superuser()


#Route to fetch user accounts
@superuser_accounts_bp.route('/user_accounts', methods=['GET'])
def get_user_accounts():
    try:
        # Query all user accounts from the database
        users = User.query.all()
        
        # Serialize user accounts data
        user_accounts = [{
            'DatabaseID': user.id,
            'FirstName': user.firstname,
            'LastName': user.lastname,
            'Email': user.email,
            'LastLoggedIn': user.last_login,
            'FreezeFlag': user.freeze_flag,
            # 'SavedTrips': user.saved_trips,  # Assuming you have this attribute in your User model
            # 'LastLoggedIn': user.last_logged_in  # Assuming you have this attribute in your User model
        } for user in users]
        
        return jsonify(user_accounts), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#Route to freeze user account
@superuser_accounts_bp.route('/user_accounts/<int:user_id>/freeze', methods=['PUT'])
def freeze_user_account(user_id):
    user = User.query.get_or_404(user_id)
    user.freeze_flag = request.json.get('freezeFlag')
    db.session.commit()
    return jsonify({'message': 'Account freeze status updated in database', 'freezeFlag': user.freeze_flag}), 200

#Route to delete all trips associated with a user
@superuser_accounts_bp.route('delete_user_trips/<int:user_id>', methods=['DELETE'])
def delete_trips(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            # Delete all trips associated with the user
            trips = Trip.query.filter_by(user_id=user_id).all()
            print("Trips:", trips)
            for trip in trips:
                db.session.delete(trip)
            db.session.commit()
            return jsonify({'message': 'Trips deleted successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#Route to delete a user account
@superuser_accounts_bp.route('/delete_user_account/<int:user_id>', methods=['DELETE'])
def delete_user_account(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User account deleted successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@superuser_accounts_bp.route('/reset_user_password/<int:user_id>', methods=['PUT'])
def reset_user_password(user_id):
    try:
        # Retrieve the user from the database
        user = User.query.get(user_id)
        if user:
            # Get the new password from the request
            new_password = request.json.get('newPassword')

            # Hash the new password using bcrypt
            hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')

            # Update the user's password with the hashed password
            user.password = hashed_password
            db.session.commit()
            return jsonify({'message': 'User password reset successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    # Route to update user profile
@superuser_accounts_bp.route('/edit_user_account/<int:user_id>', methods=['PUT'])
def update_user_profile(user_id):
    data = request.json
    print(data)

    # Check if user exists
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Update user profile
    user.firstname = data.get('FirstName', user.firstname)
    user.lastname = data.get('LastName', user.lastname)
    user.email = data.get('Email', user.email)

    # Save changes to database
    db.session.commit()

    return jsonify({'message': 'User profile updated successfully'}), 200

#Route to fetch saved trips for the current user
@superuser_accounts_bp.route('/fetch_user_trips/<int:user_id>', methods=['GET'])
def get_saved_trips(user_id):
    # Query the database for saved trips associated with the current user
    saved_trips = Trip.query.filter_by(user_id=user_id).all()
    # Check if there are no trips saved
    if not saved_trips:
        return jsonify({'message': 'No trips saved.'}), 200

    # Serialize the trip objects into JSON format
    serialized_trips = [{
        'id': trip.id,
        'city': trip.city,
        'city_description': trip.city_description,
        'activities': trip.activities,
        'state' : trip.state,
        'dates' : trip.dates,
        'budget' : trip.budget,
        'foods' : trip.foods,
        'shops' : trip.shops,
        'landmarks' : trip.landmarks,
        'hotels' : trip.hotels,
        'city_slogan' : trip.city_slogan,
        'generated_activities' : trip.generated_activities,
        'generated_shops' : trip.generated_shops,
        'generated_landmarks' : trip.generated_landmarks,
        'generated_hotels' : trip.generated_hotels,
        'generated_foods' : trip.generated_foods,
        'latitude' : trip.latitude,
        'longitude' : trip.longitude,
        #'imageSrc': trip.image_src  # Assuming you have an image source field in your Trip model
        # Add more fields as needed
    } for trip in saved_trips]
    return jsonify({'savedTrips': serialized_trips}), 200

#Route to delete single trip associated with a user
@superuser_accounts_bp.route('delete_single_user_trip/<int:trip_id>', methods=['DELETE'])
def delete_single_trip(trip_id):
    try:
        trip = Trip.query.get(trip_id)
        if trip:
            #Delete the trip
            db.session.delete(trip)
            db.session.commit()
            return jsonify({'message': 'User trip deleted successfully'}), 200
        else:
            return jsonify({'error': 'Trip not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500