
import config
from endpoints import create_endpoints

from flask import Flask, Response, request, current_app, jsonify, g
from flask_cors import CORS
from flask.json import JSONEncoder
from sqlalchemy import create_engine

class Service:
    pass

def create_app(test_config = None):
    app = Flask(__name__)

    CORS(app)
    app.config.from_pyfile("config.py")

    db = create_engine(
        app.config['DB_URL'], 
        encoding = "utf-8", 
        pool_size = 50, 
        pool_recycle = 20000, 
        max_overflow = 0
    )

    # 아직 개발되지 않은 부분은 None으로 남겨둠.
    # Persistenace Layer
    user_dao = None
    petition_dao = None
    debate_dao = None

    # Business Layer
    user_service = None
    petition_service = None
    debate_service = None

    services = Service
    services.user_service = None
    services.petition_service = None
    services.debate_service = None
    
    create_endpoints(app, services)

    return app