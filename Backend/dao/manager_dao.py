from sqlalchemy import text

class ManagerDao:
    def __init__(self, db):
        self.db = db

    def get_all_nickname(self):
        # DB상 존재하는 모든 닉네임을 리스트로 리턴
        # 실패시 None
        pass

    def update_privilege(self, uid:int, priv:int):
        # uid에 해당하는 유저의 권한을 변경함.
        # 실패시 None, 성공시 전체 유저 수 반환.
        pass

    def delete_user(self, uid:str):
        # 실패시 None, 성공시 Transaction 이후 전체 유저의 수 반환.
        pass

    def insert_authcode(self, stdid:int, authcode:str):
        # 인증번호 insert
        # 실패시 None, 성공시 1
        pass

    def get_authcode(self, stdid:int):
        # stdid(학번 등 개인고유번호)를 받아 DB에서 해당 학번의 인증번호를 인출.
        # 해당하는 인증번호가 없으면 None, 있으면 해당 인증번호를 반환.
        pass