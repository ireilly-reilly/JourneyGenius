from app import app
from SuperuserAccounts import superuser_accounts_bp

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)  # Run the Flask app