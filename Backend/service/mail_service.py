import smtplib
import threading
from email.mime.text import MIMEText

class Mailer:
    def __init__(self, mail_server:str, port:int, email:str, id_email:str, authcode:str):
        self.email = email
        self.send_list = []

        self.smtp = smtplib.SMTP(mail_server, port)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.login(id_email, authcode)

    def run(self):
        self.send_process()
        threading.Timer(5, self.run).start()

    def send(self, title:str, content:str, to:tuple):
        self.send_list.append({
            "title":title,
            "content":content,
            "to":to
        })

    def send_process(self):
        while True:
            try:
                i = self.send_list.pop()
            except IndexError:
                break

            msg = MIMEText(i["content"])
            msg["Subject"] = i["title"]
            msg["From"] = self.email

            for k in i["to"]:
                msg["To"] = k
                self.smtp.sendmail(self.email, k, msg.as_string())