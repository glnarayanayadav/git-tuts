from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    """Application factory for the Flask app."""
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)
    # Load default config
    app.config.from_object('config.Config')

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    # Initialize extensions
    db.init_app(app)

    # Register blueprints / routes
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Import models so they are registered with SQLAlchemy
    with app.app_context():
        from . import models
        db.create_all()

    return app
