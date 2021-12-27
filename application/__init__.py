"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from application.errors import error_templates

from flask import render_template, make_response

# Globally accessible libraries
db = SQLAlchemy()

def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    db.init_app(app)

    error_templates(app)

# maybe create an errors template

    with app.app_context():
        # Import parts of our application
        from .home import routes
        # from .errors import routes

        # Register Blueprints
        app.register_blueprint(home.routes.home_bp)
        # app.register_blueprint(errors.routes.errors_bp)

        return app