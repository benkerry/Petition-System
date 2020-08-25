from dao import PetitionDao
from .mail_service import Mailer
from endpoints import Config
from flask import jsonify

class PetitionService:
    def __init__(self, dao:PetitionDao, config:Config, mailer:Mailer):
        self.dao = dao
        self.config = config
        self.mailer = mailer

    def get_petition_metadata_service(self, count = 0, petition_type = "newest"):
        return jsonify({"petitions":self.dao.get_petition_metadatas(count, petition_type)})

    def get_petition_service(self, petition_id:int):
        result = self.dao.get_petition(petition_id, self.config.pass_ratio)
        result["expire_left"] = self.config.expire_left
        return jsonify(result)

    def write_petition_service(self, uid:int, title:str, contents:str):
        if title != "" and contents != "":
            return jsonify({"id":self.dao.insert_petition(uid, title, contents.replace("\n", "<br>"), self.config.expire_left)})
        else:
            return "빈칸을 모두 채워주세요.", 200
    
    def support_petition_service(self, uid:int, petition_id:int):
        if self.dao.insert_support(uid, petition_id) is not None:
            return "{petition_id}번 청원에 동의하셨습니다!", 200
        else:
            return "이미 동의한 청원이거나, 동의할 수 없는 청원입니다.", 400

    def report_service(self, uid:int, petition_id:int, description:str):
        if self.dao.insert_report(uid, petition_id, description) is not None:
            return "신고가 접수되었습니다.", 200
        else:
            return "이미 신고하신 청원입니다.", 400

    def check_petitions(self):
        # 매일 실행되어, 동의 수가 일정 이상인 청원의 Status Code를 갱신.
        # 동의 수 미달성 상태로 일정 기간 지난 청원의 Status Code도 갱신.(열린 청원만)
        # Status Code: 0 - 열림, 1 - 기간 만료 닫힘, 2 - 동의 목표 달성, 3 - 답변 완료, 4 - 관리자 직권 닫힘, 5 - 자동 신고 처리로 닫힘
        # 통과된 청원들을 모든 유저에게 이메일로 보냄.
        pass