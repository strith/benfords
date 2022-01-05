"""Initialize Flask app."""
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

from application.errors import error_templates

from flask import render_template, make_response

# Globally accessible libraries
# db = SQLAlchemy()

def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.ProdConfig')

    # db.init_app(app)

    error_templates(app)

    with app.app_context():
        # Import parts of our application
        from .home import routes
        from .benford_eval import routes

        # Register Blueprints
        app.register_blueprint(home.routes.home_bp)
        app.register_blueprint(benford_eval.routes.benford_eval_bp)

        return app