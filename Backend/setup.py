import sys
from app import create_app, cfg

from flask_script import Manager, Server
from flask_twisted import Twisted
from twisted.python import log
from OpenSSL import SSL

if __name__ == "__main__":
    app = create_app()
    twisted = Twisted(app)
    log.startLogging(sys.stdout)

    manager = Manager(app)
    manager.add_command('runserver', Server(host = "0.0.0.0", port = 80, ssl_crt = cfg.cert, ssl_key = cfg.pkey))
    manager.run()