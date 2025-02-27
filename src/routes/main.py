from flask import render_template, request, flash, jsonify
from src.services.calculator import calculate_steps
from src.utils.validators import validate_input

def register_routes(app):
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

    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "healthy"}), 200

    @app.errorhandler(404)
    def page_not_found(e):
        app.logger.error(f"404 error: {request.url}")
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        app.logger.error(f"500 error: {str(e)}")
        return render_template('500.html'), 500