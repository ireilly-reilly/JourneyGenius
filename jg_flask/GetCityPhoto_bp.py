from flask import Blueprint, jsonify, request, session, make_response, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import User
from app import Trip

GetCityPhoto_bp = Blueprint('GetCityPhoto_bp', __name__, url_prefix='/api')

#Route to get photo url
@GetCityPhoto_bp.route('get_city_photo', methods=['POST'])
def get_city_photo():
    data = request.json
    city = data.get('cityName')
    print('City from GetDestinationPhoto_bp: ', city)


    #Ethan enter your photo logic here

    photo_url = 'https://images.nationalgeographic.org/image/upload/t_edhub_resource_key_image/v1638892254/EducationHub/photos/kkk-gathering.jpg'

    return jsonify({"photo_url": photo_url}), 200