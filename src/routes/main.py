from flask import render_template, request, jsonify
from src.services import calculate_steps
from src.utils import validate_input

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/how-it-works')
    def how_it_works():
        return render_template('how_it_works.html')

    @app.route('/benefits')
    def benefits():
        return render_template('benefits.html')

    @app.route('/faq')
    def faq():
        return render_template('faq.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/calculator')
    def calculator():
        return render_template('calculator.html')

    @app.route('/api/calculate-steps', methods=['POST'])
    def api_calculate_steps():
        data = request.json
        calories = data.get('calories')
        weight = data.get('weight')
        height = data.get('height')
        pace = data.get('pace')

        errors = validate_input(calories, weight, height, pace)

        if errors:
            return jsonify({"errors": errors}), 400

        try:
            calories = float(calories) if calories else 0
            weight = float(weight) if weight else 70
            height = float(height) if height else 170
            pace = pace if pace else 'moderate'

            steps = calculate_steps(calories, weight, height, pace)
            return jsonify({"steps": steps})
        except Exception as e:
            app.logger.error(f"Error calculating steps: {str(e)}")
            return jsonify({"error": "An error occurred while calculating steps. Please try again."}), 500

    @app.route('/health')
    def health_check():
        return jsonify({"status": "healthy"}), 200

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500