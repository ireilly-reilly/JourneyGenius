from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db  # Import your SQLAlchemy instance
from app import User  # Import your User model
from app import bcrypt


# Create a Blueprint for user profiling routes
user_account_bp = Blueprint('user_account_bp', __name__, url_prefix='/api/user_account')

@user_account_bp.route('/reset_user_password', methods=['PUT'])
@jwt_required()
def reset_user_password():
    user_id = get_jwt_identity()
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
    
#Route to fetch user information
@user_account_bp.route('/fetch_user_info', methods=['GET'])
@jwt_required()  
def get_user_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    user_data = {
        'firstName': user.firstname,
        'lastName': user.lastname,
        'email': user.email,
    }

    return jsonify(user_data), 200

#Route to update user account information
@user_account_bp.route('/edit_user_account', methods=['PUT'])
@jwt_required()
def update_user_profile():
    user_id = get_jwt_identity()
    data = request.json

    # Check if user exists
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Update user profile
    user.firstname = data.get('newFirstName', user.firstname)
    user.lastname = data.get('newLastName', user.lastname)
    user.email = data.get('newEmail', user.email)

    # Save changes to database
    db.session.commit()

    return jsonify({'message': 'User profile updated successfully'}), 200