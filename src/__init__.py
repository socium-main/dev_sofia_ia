from flask import Flask
from src.api.routes import register_blueprints

def create_app():
    app = Flask(__name__)

    # Registrar blueprints
    register_blueprints(app)

    return app