"""Utility to initialize the SQLite database for local development."""
from app import create_app, db


def init_db():
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Database initialized at:", app.config.get('SQLALCHEMY_DATABASE_URI'))


if __name__ == '__main__':
    init_db()
