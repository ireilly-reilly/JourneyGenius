from flask import Blueprint, jsonify, request
from app import db  # Import your SQLAlchemy instance
from app import User  # Import your User model

#Create the blueprint object
superuser_accounts_bp = Blueprint('superuser_accounts', __name__, url_prefix='/api')

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