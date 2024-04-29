# auth_bp.py

from flask import Blueprint, jsonify, request, session, make_response, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import bcrypt
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import random
import string
import os
import requests
from dotenv import load_dotenv
from app import db
from app import User  #Import the User model

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/api/auth')


#Route to send verification email
@auth_bp.route('/api/auth/send_verification_email', methods=['POST'])
def send_verification_email():
    print("send_verification_email: got here")
    email = request.json.get('email')
    print('Email to send to: ', email)
    if not email:
        return jsonify({'message': 'Email address not provided'}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404
    #Generate a random verification token
    verification_token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    print('Verification Token: ', verification_token)
    # Send email using SendGrid
    sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
    sender_email = os.getenv('SENDER_EMAIL')

    if not sendgrid_api_key or not sender_email:
        return jsonify({'message': 'SendGrid API key or sender email not configured'}), 500

    message = Mail(
        from_email=sender_email,
        to_emails=email,
        subject='Verify your email address for JourneyGenius',
        html_content=f'Click <a href="http://localhost:8080/VerifyEmail/{verification_token}/{email}">here</a> to verify your email address.'
    )

    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print('Response from sendgrid: ', response)
        user.verification_token = verification_token
        db.session.commit()
        
        return jsonify({'message': 'Verification email sent'}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to verify user'}), 500
    
#Route that actually verifies email
@auth_bp.route('/verify_email/<token>/<email>', methods=['POST'])
def verify_email(token, email):
    print("Got to this point")#This does not print, issue is with previous line
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'Invalid or expired token'}), 400
    
    verification_token = user.verification_token
    print("Verification token from database: ", verification_token)
    if (token == verification_token):

        user.email_verified = True
        db.session.commit()

        return jsonify({'message': 'Email verified successfully'}), 200
    else:
        return jsonify({'message': 'Error validating email'}), 500
    
#Route to resend email
@auth_bp.route('/resend_verification_email/<email>', methods=['POST'])
def resend_verification_email(email):
    

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404
    #Generate a random verification token
    verification_token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    print('Verification Token: ', verification_token)
    # Send email using SendGrid
    sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
    sender_email = os.getenv('SENDER_EMAIL')

    email = user.email
    if not sendgrid_api_key or not sender_email:
        return jsonify({'message': 'SendGrid API key or sender email not configured'}), 500

    message = Mail(
        from_email=sender_email,
        to_emails=email,
        subject='Verify your email address for JourneyGenius',
        html_content=f'Click <a href="http://localhost:8080/VerifyEmail/{verification_token}/{email}">here</a> to verify your email address.'
    )

    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print('Response from sendgrid: ', response)
        user.verification_token = verification_token
        db.session.commit()
        
        return jsonify({'message': 'Verification email sent.'}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to send verification email. '}), 500
    
#Route to check email verification flag
@auth_bp.route('/check_verification/<email>', methods=['GET'])
def isVerified(email):
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    print(user.email_verified)
    if (user.email_verified == False):
        return jsonify({'error': 'Email not verified'}), 401
    else:
        return jsonify({'message': 'success.'}), 200