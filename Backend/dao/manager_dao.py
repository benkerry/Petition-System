from sqlalchemy import text

class ManagerDao:
    def __init__(self, db):
        self.db = db

    def get_user_count(self):
        return self.db.execute(text("""
            SELECT COUNT(*) FROM users
        """)).fetchone()[0]

    def insert_authcode(self, authcode:tuple):
        # ( (stdid, authcode), ... ) 형태로 들어온 인증번호 insert
        # 실패시 None, 성공시 1
        pass

    def get_all_authcode(self, stdid:tuple):
        # stdid(학번 등 개인고유번호)의 튜플을 받아 DB에서 해당 학번의 인증번호를 인출.
        # 해당하는 모든 인증번호를 2차원 튜플 ( (stdid, authcode), ... ) 형태로 반환
        pass

    def get_add_day(self, petition_id:int):
        # 해당 청원 만료기한 연장 요청 상황 확인,
        # 실패시 None, 성공시 ( (req_id, comment), ... ) 반환
        pass