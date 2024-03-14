# Load environment variables from .env file
export $(grep -v '^#' .env | xargs)

# Run Flask application
python app.py