"""
Configuration class to handle environment variables for the Flask application.
"""

import os
from dotenv import load_dotenv  # Used to load variables from a .env file

# Load environment variables from a .env file (if present)
load_dotenv()

class Config:
    """
    Base configuration class.
    Stores configuration values such as database URI and SQLAlchemy settings.
    """
    
    # Database connection string pulled from environment or uses default PostgreSQL URL
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://tracker_user:strongpassword123@localhost:5432/financial_tracker"
    )

    # Disable event system to save resources (recommended unless explicitly needed)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Additional configuration parameters (e.g., SECRET_KEY) can be defined here
