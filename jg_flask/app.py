from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt

#Flask App Initializations
app = Flask(__name__, static_folder='../journey-genius-ui/dist', static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///useraccounts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True)

#Format for 'Users' in database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


#Route to register new users
@app.route('/api/RegisterUser', methods=['POST'])
def RegisterUser():
    #Get the data from Vue
    data = request.json

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 400 #TODO Change to 400 later

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

#Route to login existing user
@app.route('/api/LoginUser', methods = ['POST'])
def LoginUser():
    data = request.json

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        session['user_id'] = user.id  # Store user ID in the session
        print("Logging in user... User ID in session: ", session.get('user_id'))
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401 #TODO change to 401 later 
    
#Route to check login status
@app.route('/api/check_login_status', methods=['GET'])
def check_login_status():
    user_id = session.get('user_id')
    print("Checking Login status... User ID in session: ", session.get('user_id'))
    if user_id:
        return jsonify({'message': 'User is logged in', 'user_id': user_id}), 200
    else:
        return jsonify({'message': 'User is not logged in'}), 401


#Route to logout user
@app.route('/api/LogoutUser', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Remove user ID from the session
    return jsonify({'message': 'Logout successful'}), 200


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True) #Runs on port 8000!!!