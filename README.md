# JourneyGenius Python Flask Backend

### The following are instructions to get the basic JourneyGenius python flask backend running on your machine. 

**Important Note: This has been tested to work on Mac, instructions may vary for Windows.**  

**If you are running a Mac with an M1 chip or newer, I highly recommend you use Homebrew, as it makes package installation much smoother.**

### To install Homebrew:  
1. Paste the following command into your terminal:  
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```  
   This can take a while, so make sure to wait until it is finished. 

### To setup running environment:


1. Download the "Flask Introduction" folder from this branch
2. Open the "Flask Introduction" in your IDE and **MAKE SURE** your terminal is in that directory  
  **This is essential because it isolates any necessary environment installations to this directory without having to deal with globally installed packages throughout your machine!**
3. In your IDE terminal, paste and run the following commands individually:  

     
   Install VirtualEnv:  
   ```
   pip3 install virtualenv
   ```
   Create virtual environment:  
   ```
   virtualenv env
   ```
   Activate virtual environment:  
   ```
   source env/bin/activate
   ```
   Install project dependencies:
   ```
   pip3 install flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator
   ```

### To access running application on a web browser:
1. To run the application, paste the following commands one at a time into your IDE terminal:  
   ```
   flask shell
   ```
   ```
   from app import db
   ```
   ```
   db.create_all()
   ```
   ```
   exit()
   ```
   ```
   python3 app.py
   ```  
2. Enter the following in your web browser search bar:
   ```
   http://localhost:8080
   ```  
   
**This should install all the necessary packages to run the basic Python Flask Framework for JourneyGenius.**


# journey-genius-ui

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


# MySQL localhost Initialization and Migration Setup Information

1. Install MySQL and MySQL client

Log into MySQL as a root admin user: 
```
mysql -u root -p
```
Enter your root user password.   
Create database:
```
CREATE DATABASE useraccounts;
```
Create the new JourneyGenius user referenced in your .env file:
```
CREATE USER 'JourneyGenius'@'localhost' IDENTIFIED BY 'WanderDeezNutz';
```
Grant JourneyGenius user ability to create:
```
GRANT CREATE ON *.* TO 'JourneyGenius'@'localhost';
```
Flush privileges:
```
FLUSH PRIVILEGES;
```
Exit MySQL CLI:
```
exit
```
Run JourneyGenius to initialize database models from code:
```
./run_dev.sh
```
Use ^C to cancel because things won't work yet.   
Log into MySQL as a root admin user again: 
```
mysql -u root -p
```
Enter your root password.   
Run the following commands:
```
USE useraccounts;
GRANT ALL PRIVILEGES ON useraccounts.user TO 'JourneyGenius'@'localhost';
GRANT ALL PRIVILEGES ON useraccounts.super_user TO 'JourneyGenius'@'localhost';
GRANT ALL PRIVILEGES ON useraccounts.trip TO 'JourneyGenius'@'localhost';
GRANT ALL PRIVILEGES ON useraccounts.admin_change_log_entry TO 'JourneyGenius'@'localhost';
GRANT SELECT ON alembic_version TO 'JourneyGenius'@'localhost';
FLUSH PRIVILEGES;
```
Exit MySQL:
```
exit
```
I think this should get everything to work.   
## If you make changes to the database structure or pull code that changed database structure
### First setup migration system
In  terminal, install flask migrate:
```
pip install Flask-Migrate
```
Initialize Migrations folders by typing into terminal:
```
flask db init
```
### To use migration system:
After making changes or pulling code that made changes to database structure, type the following:
```
flask db migrate -m "<your change message>"
```
Apply changes:
```
flask db upgrade
```

### Other Dependencies:
```
pip3 install openai
pip3 install googlemaps
pip3 install googlemaps.exceptions
pip3 install scikit-learn
pip3 install spacy
pip3 install dotenv
pip3 install typing
pip3 install flask
pip3 install flask-cors
pip3 install flask_jwt_extended
pip3 install flask_migrate
pip3 install sendgrid
pip3 install click
pip3 install requests 

