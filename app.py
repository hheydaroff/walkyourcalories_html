import os
from flask import Flask, render_template, request, flash, redirect, url_for
import logging

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'fallback_secret_key')  # Use environment variable

# Set up logging
app.logger.handlers.clear()
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

def calculate_steps(calories: float, weight: float, pace: str) -> int:
    # MET values for different paces
    met_values = {
        "Slow": 2.8,
        "Moderate": 3.3,
        "Brisk": 4.0
    }

    # Steps per minute (assumed constant)
    steps_per_minute = 100

    # Get MET value based on pace
    met = met_values[pace]

    # Calculate calories burned per minute
    kcal_per_minute = (met * 3.5 * weight) / 200

    # Calculate calories burned per step
    kcal_per_step = kcal_per_minute / steps_per_minute

    # Calculate total steps
    steps = int(calories / kcal_per_step)

    return steps

def validate_input(calories, weight, pace):
    errors = []
    
    try:
        calories = float(calories)
        if calories < 0:
            errors.append("Calories must be a positive number")
    except ValueError:
        errors.append("Invalid calories value")

    try:
        weight = float(weight)
        if weight < 1 or weight > 500:
            errors.append("Weight must be between 1 and 500 kg")
    except ValueError:
        errors.append("Invalid weight value")

    if pace not in ['Slow', 'Moderate', 'Brisk']:
        errors.append("Invalid pace")

    return errors

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        calories = request.form['calories']
        weight = request.form['weight']
        pace = request.form['pace']

        app.logger.info(f"Received form data: calories={calories}, weight={weight}, pace={pace}")

        errors = validate_input(calories, weight, pace)

        if errors:
            for error in errors:
                flash(error, 'error')
            app.logger.warning(f"Invalid input: {', '.join(errors)}")
            return render_template('index.html')

        try:
            steps = calculate_steps(float(calories), float(weight), pace)
            app.logger.info(f"Calculated steps: {steps} for input: calories={calories}, weight={weight}, pace={pace}")
            flash(f"Estimated steps to burn {calories} calories: {steps}", 'success')
            return render_template('index.html', steps=steps)
        except Exception as e:
            app.logger.error(f"Error calculating steps: {str(e)}")
            flash("An error occurred while calculating steps. Please try again.", 'error')
            return render_template('index.html')
    
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    app.logger.error(f"404 error: {request.url}")
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    app.logger.error(f"500 error: {str(e)}")
    return render_template('500.html'), 500

# This allows the app to be run using Flask's development server or with Gunicorn
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))
else:
    # When running with Gunicorn, this block is executed
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)