
import config.config as cfg

from dao.user_dao import UserDao
from dao.petition_dao import PetitionDao
from dao.debate_dao import DebateDao
from dao.manager_dao import ManagerDao

from service import UserService, PetitionService, DebateService, ManagerService, Mailer

from endpoints import create_endpoints, Config

from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine

class Service:
    pass

def create_app(test_config = None):
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = cfg.JWT_SECRET_KEY

    CORS(app)

    db = create_engine(
        cfg.DB_URL, 
        encoding = "utf-8", 
        pool_size = 50, 
        pool_recycle = 20000, 
        max_overflow = 0
    )

    config = Config(cfg.pass_ratio, cfg.expire_left)

    mailer = Mailer(cfg.mail_server, cfg.port, cfg.email, cfg.id_email, cfg.authcode)
    mailer.run()

    # Persistenace Layer
    user_dao = UserDao(db)
    petition_dao = PetitionDao(db)
    debate_dao = DebateDao(db)
    manager_dao = ManagerDao(db)

    # Business Layer
    user_service = UserService(user_dao, mailer)
    petition_service = PetitionService(petition_dao, config)
    debate_service = DebateService(debate_dao)
    manager_service = ManagerService(user_dao, petition_dao, debate_dao, manager_dao)

    services = Service
    services.user_service = user_service
    services.petition_service = petition_service
    services.debate_service = debate_service
    services.manager_service = manager_service
    
    create_endpoints(app, services, config)
    return app