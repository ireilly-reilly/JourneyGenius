from flask import Blueprint, jsonify
from app import db  # Import your SQLAlchemy instance
from app import User  # Import your User model
from app import Trip

superuser_analytics_bp = Blueprint('superuser_analytics', __name__)

#Route to fetch total number of user accounts in database
@superuser_analytics_bp.route('/total_accounts')
def total_accounts():
    total_accounts_count = User.query.count()
    return jsonify(totalAccounts=total_accounts_count)

#Route to fetch total number of trips saved in database
@superuser_analytics_bp.route('/total_trips_saved')
def total_trips_saved():
    total_trips_saved_count = Trip.query.count()
    return jsonify(totalTripsSaved=total_trips_saved_count)