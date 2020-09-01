from app import twisted, ssl_data
from OpenSSL import SSL
from twisted.python import log
from twisted.application.service import Application

app = Application('twisted-flask')
twisted.run(host = "0.0.0.0", port = 80, ssl_context = ssl_data)
log.startLogging(open("log", "w"))