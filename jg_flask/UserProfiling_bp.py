# Import necessary modules
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db  # Import your SQLAlchemy instance
from app import User  # Import your User model

# Create a Blueprint for user profiling routes
user_profiling_bp = Blueprint('user_profiling_bp', __name__, url_prefix='/api/user_profiling')

# Route to save selected preferences to user database model
@user_profiling_bp.route('/save_preferences_to_user', methods=['POST'])
@jwt_required()
def save_preferences_to_user():
    try:
        # Get current user's ID from JWT token
        current_user_id = get_jwt_identity()

        # Parse JSON data from request body
        preferences = request.json

        # Get the user from the database
        user = User.query.filter_by(id=current_user_id).first()

        # Update user's preferences fields
        # user.fav_activities = preferences['selectedActivities']
        # user.fav_foods = preferences['selectedFoods']
        # user.fav_shopping = preferences['selectedShopping']
        # user.fav_accomodations = preferences['selectedAccommodation']

        user.fav_activities = preferences.get('selectedActivities', [])
        user.fav_foods = preferences.get('selectedFoods', [])
        user.fav_shopping = preferences.get('selectedShopping', [])
        user.fav_accomodations = preferences.get('selectedAccommodation', [])

        print('Saved activities: ', user.fav_activities)
        print('Saved foods: ', user.fav_foods)
        print('Saved shopping: ', user.fav_shopping)
        print('Saved accommodation: ', user.fav_accomodations)
        # Commit changes to the database
        db.session.commit()
        print('User preferences updated.')

        return jsonify({'message': 'Preferences saved successfully'}), 200

    except Exception as e:
        # Handle any errors
        return jsonify({'error': str(e)}), 500

#Route to fetch user preferences
@user_profiling_bp.route('/fetch_user_preferences', methods=['GET'])
@jwt_required()
def get_user_preferences():
    try:
        # Get current user's ID from JWT token
        current_user_id = get_jwt_identity()

        # Get the user from the database
        user = User.query.filter_by(id=current_user_id).first()

        # Construct a dictionary containing user's preferences
        preferences = {
            'activities': user.fav_activities if user.fav_activities else [],
            'foods': user.fav_foods if user.fav_foods else [],
            'shopping': user.fav_shopping if user.fav_shopping else [],
            'accommodation': user.fav_accomodations if user.fav_accomodations else None
        }

        return jsonify(preferences), 200

    except Exception as e:
        # Handle any errors
        return jsonify({'error': str(e)}), 500