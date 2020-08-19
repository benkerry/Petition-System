import smtplib
from email.mime.text import MIMEText

class Mailer:
    def __init__(self, mail_server:str, port:int, email:str, id_email:str, authcode:str):
        self.mail_server = mail_server
        self.port = port
        self.email = email
        self.id_email = id_email
        self.authcode = authcode

    def Send(self, title:str, content:str, to:tuple):
        self.smtp = smtplib.SMTP(self.mail_server, self.port)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.login(id_email, authcode)

        msg = MIMEText(content)
        msg['Subject'] = title
        msg['From'] = email
        msg['To'] = ",".join(to)

        self.smtp.sendmail(email, to, msg.as_string())