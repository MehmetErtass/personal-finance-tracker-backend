"""
Application factory for Flask backend.
Creates and configures the Flask app instance.
"""

import os
from flask import Flask, render_template
from flask_cors import CORS  # Enables Cross-Origin Resource Sharing
from dotenv import load_dotenv  # Loads environment variables from a .env file

from config import Config       # Configuration settings for the Flask app
from models import db           # SQLAlchemy database instance
from routes import register_routes  # Custom route registrations

# Load environment variables from the .env file
load_dotenv()

def create_app():
    """
    Application factory function.
    Initializes Flask app, configures it, enables CORS, and sets up the database and routes.
    """
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    # Load configuration from the Config class
    app.config.from_object(Config)

    # Enable CORS for API requests
    CORS(app)

    # Initialize database with the app
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Create all database tables

    # Register custom application routes
    register_routes(app)

    @app.route("/")
    def home():
        # Default route rendering a template
        return render_template("index.html")

    return app

# If this script is run directly, start the development server
if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5000))  # Get port from environment or use default 5000
    app.run(debug=True, port=port)
