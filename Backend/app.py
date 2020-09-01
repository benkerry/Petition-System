import config.config as cfg

from dao.user_dao import UserDao
from dao.petition_dao import PetitionDao
from dao.manager_dao import ManagerDao

from service import UserService, PetitionService, ManagerService, Mailer

from endpoints import create_endpoints, Config

from OpenSSL import SSL
from flask import Flask
from flask_cors import CORS
from flask.ext.twisted import Twisted
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

    config = Config(cfg.pass_ratio, cfg.expire_left, cfg.svr_addr)

    mailer = Mailer(cfg.mail_server, cfg.port, cfg.email, cfg.id_email, cfg.authcode)
    mailer.run()

    # Persistenace Layer
    user_dao = UserDao(db)
    petition_dao = PetitionDao(db)
    manager_dao = ManagerDao(db)

    config.pass_line = (manager_dao.get_user_count() * 100) // config.pass_ratio

    # Business Layer
    user_service = UserService(user_dao, mailer, config)
    petition_service = PetitionService(petition_dao, user_dao, config, mailer)
    manager_service = ManagerService(user_dao, petition_dao, manager_dao, mailer, config)

    services = Service
    services.user_service = user_service
    services.petition_service = petition_service
    services.manager_service = manager_service
    
    create_endpoints(app, services, config)
    return app

app = create_app()
twisted = Twisted(app)

app.run(host = "0.0.0.0", port = 80, ssl_context = (cfg.cert, cfg.pkey))