from sqlalchemy import text

class UserDao():
    # 여기에서는 users, authcodes 테이블에만 액세스하도록 한다.
    def __init__(self, db):
        self.db = db

    def get_authcode(self, stdid:int):
        # stdid(학번 등 개인고유번호)를 받아 DB에서 해당 학번의 인증번호를 인출.
        # 해당하는 인증번호가 없으면 None, 있으면 해당 인증번호를 반환.
        pass

    def insert_user(self, email:str, hashed_pwd:str, nickname:str, stdid:int):
        # 새 유저를 생성.
        # 실패시 None, 성공시 전체 유저의 수 반환.
        pass

    def delete_user(self, uid:str):
        # 유저를 삭제.
        # 실패시 None, 성공시 Transaction 이후 전체 유저의 수 반환.
        pass

    def get_user(self, email:str, uid:int = -1):
        # 유저 정보(학번, 이메일, 해시된 패스워드, 닉네임)를 인출.
        # 실패시 None, (성공시 학번, 이메일, 해시된 패스워드, 닉네밈):tuple을 반환.
        pass

    def update_user_info(self, uid:int, email:str, nickname:str):
        # uid에 해당하는 유저 정보(email, nickname)를 parameter로 들어온 email, nickname으로 업데이트.
        # 실패시 None, 성공시 전체 유저 수 반환
        pass

    def update_pwd(self, uid:int, hashed_pwd:str):
        # uid에 해당하는 유저의 해시 패스워드를 업데이트.
        # 실패시 None, 성공시 전체 유저 수 반환.
        pass

    def update_privilege(self, uid:int, priv:int):
        # uid에 해당하는 유저의 권한을 변경함.
        # 실패시 None, 성공시 전체 유저 수 반환.
        pass