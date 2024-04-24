from flask import Blueprint, jsonify, Response
from app import db  # Import your SQLAlchemy instance
from app import User  # Import your User model
from app import Trip
from app import AdminChangeLogEntry
import csv
from io import StringIO
import datetime

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

@superuser_analytics_bp.route('/export_changelog_csv')
def export_changelog_csv():
    # Retrieve all entries from the database
    changelog_entries = AdminChangeLogEntry.query.all()

    #Create a StringIO object to hold CSV data in memory
    csv_data = StringIO()
    
    #Create a CSV writer object
    csv_writer = csv.writer(csv_data)
    
    #Write the title row
    csv_writer.writerow(['Admin Changelog'])
    
    #Write an empty row for spacing
    csv_writer.writerow([])

    #Write the header row
    csv_writer.writerow(['Entry ID', 'Timestamp', 'Super User ID', 'Action', 'Affected User ID'])
    
    #Write each row of data to the CSV file
    for entry in changelog_entries:
        # Convert the timestamp to a datetime object
        timestamp_datetime = datetime.datetime.strptime(entry.timestamp, '%Y-%m-%d %H:%M:%S')

        # Format the datetime object as a string in a format recognized by Excel
        formatted_timestamp = timestamp_datetime.strftime('%Y-%m-%d %H:%M:%S')
        
        csv_writer.writerow([entry.entry_id, formatted_timestamp, entry.super_id, entry.action, entry.affected_user_id])

    # Set up response headers
    headers = {
        'Content-Disposition': 'attachment; filename=changelog.csv',
        'Content-Type': 'text/csv'
    }

    # Create a Flask Response object with CSV data
    response = Response(csv_data.getvalue(), headers=headers)
    
    return response