
import config.config as config

from dao.user_dao import UserDao
from dao.petition_dao import PetitionDao
from dao.debate_dao import DebateDao
from dao.manager_dao import ManagerDao

from service import UserService, PetitionService, DebateService, ManagerService, Mailer

from endpoints import create_endpoints

from flask import Flask
from flask_cors import CORS
from flask.json import JSONEncoder
from sqlalchemy import create_engine

class Service:
    pass

def create_app(test_config = None):
    app = Flask(__name__)

    CORS(app)

    db = create_engine(
        config.DB_URL, 
        encoding = "utf-8", 
        pool_size = 50, 
        pool_recycle = 20000, 
        max_overflow = 0
    )

    mailer = Mailer(config.mail_server, config.port, config.email, config.id_email, config.authcode)

    # Persistenace Layer
    user_dao = UserDao(db)
    petition_dao = PetitionDao(db)
    debate_dao = DebateDao(db)
    manager_dao = ManagerDao(db)

    # Business Layer
    user_service = UserService(user_dao)
    petition_service = PetitionService(petition_dao, config.expire_left, config.pass_ratio)
    debate_service = DebateService(debate_dao)
    manager_service = ManagerService(user_dao, petition_dao, debate_dao, manager_dao)

    services = Service
    services.user_service = user_service
    services.petition_service = petition_service
    services.debate_service = debate_service
    services.manager_service = manager_service
    
    create_endpoints(app, services, config.expire_left, config.pass_ratio)
    return app