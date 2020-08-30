import threading
from dao import PetitionDao, UserDao
from .mail_service import Mailer
from endpoints import Config
from flask import jsonify

class PetitionService:
    def __init__(self, dao:PetitionDao, udao:UserDao, config:Config, mailer:Mailer):
        self.dao = dao
        self.udao = udao
        self.config = config
        self.mailer = mailer
        self.check_petitions()

    def get_petition_metadata_service(self, count = 0, petition_type = "newest"):
        return jsonify({"petitions":self.dao.get_petition_metadatas(count, petition_type)})

    def get_petition_service(self, petition_id:int):
        result = self.dao.get_petition(petition_id, self.config.pass_ratio)
        if not result:
            return "열람할 수 없는 청원입니다.", 403
        else:
            return jsonify(result)

    def write_petition_service(self, uid:int, title:str, contents:str):
        if title != "" and contents != "":
            return jsonify({"id":self.dao.insert_petition(uid, title, contents.replace("\n", "<br>"), self.config.expire_left)})
        else:
            return "빈칸을 모두 채워주세요.", 200
    
    def support_petition_service(self, uid:int, petition_id:int):
        if self.dao.insert_support(uid, petition_id) is not None:
            return f"{petition_id}번 청원에 동의하셨습니다!", 200
        else:
            return "이미 동의한 청원이거나, 동의할 수 없는 청원입니다.", 400

    def report_service(self, uid:int, petition_id:int, description:str):
        if description:
            if self.dao.insert_report(uid, petition_id, description) is not None:
                return "신고가 접수되었습니다.", 200
            else:
                return "이미 신고하신 청원입니다.", 400
        else:
            return "빈칸을 모두 채워주세요.", 200

    def check_petitions(self):
        passed_petitions = self.dao.check_petitions(self.config.pass_line)
        print("All petitions checked!")

        for i in passed_petitions:
            title = "[청원 시스템 | 통과된 청원 안내] " + i["title"]
            contents = "제목: " + i["title"] + "<br>통과일시: " + i["passed_at"] + "<br>내용<br><br>" + i["contents"].replace("<br>", "\n")
            to = self.udao.get_all_email()
            self.mailer.send(title, contents, to)

        if passed_petitions:
            print("Passed Petition Sended to all users.")

        threading.Timer(600, self.check_petitions).start()