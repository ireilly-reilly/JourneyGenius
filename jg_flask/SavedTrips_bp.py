from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db  # Import your SQLAlchemy instance
from app import User, Trip  # Import your User model
from app import app

#Create the blueprint object
saved_trips_bp = Blueprint('saved_trips_bp', __name__, url_prefix='/api')

#Route to save trip to database
@saved_trips_bp.route('/save_trip_to_user', methods=['POST'])
def save_trip_to_user():
    data = request.json  # Get the trip data from the request

    trip = Trip(
        user_id=data['userID'],  # Assuming you are passing the user_id along with trip data
        activities=data['activities'],
        landmarks=data['landmarks'],
        foods=data['foods'],
        shops=data['shops'],
        hotels=data['hotels'],
        dates=data['datesData'],
        budget=data['budget'],
        state=data['stateData'],
        city=data['city'],
        latitude=data['lat'],
        longitude=data['long'],
        city_description=data['cityDescription'],
        city_slogan=data['citySlogan']
        # Add other fields as needed
    )

    db.session.add(trip)
    db.session.commit()
    return jsonify({'message': 'Trip saved successfully'})

#Route to fetch saved trips for the current user
@saved_trips_bp.route('/fetch_saved_trips', methods=['GET'])
@jwt_required()  # Requires authentication
def get_saved_trips():
    current_user_id = get_jwt_identity()  # Get current user's ID from JWT token
    # Query the database for saved trips associated with the current user
    saved_trips = Trip.query.filter_by(user_id=current_user_id).all()
    # Check if there are no trips saved
    if not saved_trips:
        return jsonify({'message': 'No trips saved, let\'s plan one!'}), 200

    # Serialize the trip objects into JSON format
    serialized_trips = [{
        'id': trip.id,
        'city': trip.city,
        'city_description': trip.city_description,
        'activities': trip.activities,
        'state' : trip.state,
        'dates' : trip.dates,
        #'imageSrc': trip.image_src  # Assuming you have an image source field in your Trip model
        # Add more fields as needed
    } for trip in saved_trips]
    return jsonify({'savedTrips': serialized_trips}), 200

@saved_trips_bp.route('/delete_trip/<trip_id>', methods=['DELETE'])
@jwt_required()  # Ensure the user is authenticated
def delete_trip(trip_id):
    # Get the current user's ID from the JWT token
    current_user_id = get_jwt_identity()

    # Retrieve the trip from the database
    trip = Trip.query.filter_by(id=trip_id, user_id=current_user_id).first()

    if trip:
        # Delete the trip from the database
        db.session.delete(trip)
        db.session.commit()
        return jsonify({'message': 'Trip deleted successfully'}), 200
    else:
        return jsonify({'error': 'Trip not found or unauthorized to delete'}), 404