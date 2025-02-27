from flask import Flask
from src.config import Config
from src.routes.main import register_routes
import logging

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)

    # Set up logging
    app.logger.handlers.clear()
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(app.config['LOGGING_LEVEL'])

    # Register routes
    register_routes(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'])
else:
    # When running with Gunicorn, this block is executed
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)