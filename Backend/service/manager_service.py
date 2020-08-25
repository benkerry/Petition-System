from flask import jsonify
from endpoints import Config
from dao import UserDao, PetitionDao, ManagerDao

class ManagerService:
    def __init__(self, user_dao:UserDao, petition_dao:PetitionDao, manager_dao:ManagerDao, config:Config):
        self.user_dao = user_dao
        self.petition_dao = petition_dao
        self.manager_dao = manager_dao
        self.config = config

    def get_user_count(self):
        return self.manager_dao.get_user_count()

    def get_petition_status(self, petition_id:int):
        title, status, supports = self.petition_dao.get_petition_status(petition_id)

        if status != None:
            return jsonify({
                "title":title,
                "status":status,
                "supports":supports,
                "msg":"success!"
            })
        else:
            return "청원번호 조회에 실패했습니다.", 400

    def delete_user_service(self, uid_list:list):
        # 유저를 삭제.
        # 실패시 None, 성공시 Transaction 이후 전체 유저의 수 반환.
        pass

    def change_priv_service(self, uid:int, tgt_nickname:str):
        # 권한 변경 수행
        # 실패시 None, 성공시 200 반환
        pass

    def get_all_nicknames_service(self):
        # 모든 유저의 닉네임을 인출하여 리스트로 반환
        # 실패시 None
        pass

    def generate_authcodes_service(self, stdid_list):
        # stdid_list에 대응하는 인증번호 생성 및 이중 튜플 ( (stdid, authcode), ... )로 반환
        # 실패시 None
        pass

    def open_petition_service(self, petition_id:int):
        if self.petition_dao.reopen_petition(petition_id, self.config.expire_left) is not None:
            return "성공!", 200
        else:
            return "잘못된 접근입니다.", 403

    def add_day_service(self, petition_id:int, add_day:int):
        # 청원 만료기한을 늘림
        # add_day에 음수가 들어올 시 처리 실패로 간주한다.
        # 실패시 None, 성공시 현재로부터 만료까지 남은 날짜 반환
        # petition_dao에 있는 것 사용
        pass

    def set_support_ratio_service(self, petition_id:int):
        # 청원 동의인 비율 설정을 변경
        # 실패시 None, 변경된 비율을 적용하여 산출된 동의인 수 임곗값 리턴
        pass

    def get_add_day_request_service(self, petition_id:int):
        # 청원 만료기한 연장 요청 상황 확인,
        # 실패시 None, 성공시 ( (req_id, comment), ... ) 반환
        pass