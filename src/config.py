import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback_secret_key')
    PORT = int(os.environ.get('PORT', 5001))
    DEBUG = os.environ.get('FLASK_ENV') == 'development'
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')

    # MET values for different paces
    MET_VALUES = {
        "Slow": 2.8,
        "Moderate": 3.3,
        "Brisk": 4.0
    }

    # Steps per minute (assumed constant)
    STEPS_PER_MINUTE = 100

    # Weight range for validation
    MIN_WEIGHT = 1
    MAX_WEIGHT = 200

    # Calories range for validation
    MIN_CALORIES = 1
    MAX_CALORIES = 10000