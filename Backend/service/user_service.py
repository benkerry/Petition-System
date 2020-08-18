import jwt
import bcrypt
from ..dao import UserDao
from flask import g

class UserService:
    def __init__(self, dao:UserDao):
        self.dao = dao

    def regist_service(self, stdid:int, authcode:str, email:str, pwd:str, pwd_chk:str, nickname:str, root:int):
        if pwd != pwd_chk:
            return "비밀번호와 비밀번호 확인 란의 값이 다릅니다.", 400
        elif len(pwd) < 8:
            return "비밀번호가 너무 짧습니다. 8자 이상이어야 합니다.", 400
        elif email in self.dao.get_all_email():
            return "이미 가입된 이메일입니다.", 400
        elif nickname in self.dao.get_all_nickname():
            return "이미 존재하는 닉네임입니다."
        else:
            db_authcode = self.dao.get_authcode(stdid)

            if not db_authcode:
                return "인증번호가 틀립니다.", 401
            elif stdid != db_authcode[0] or authcode != db_authcode[1]:
                return "인증번호가 틀립니다.", 401

            hashed_pwd = bcrypt.hashpw(
                pwd.encode("UTF-8"),
                bcrypt.gensalt()
            )
            if self.dao.insert_user(email, hashed_pwd, nickname, db_authcode[0] // 1000, root):
                return "가입 성공!", 200
            else:
                return "Internal Server Error", 500

    def login_service(self, email:str, pwd:str):
        # 로그인 수행.
        # 실패시 오류 번호( n < 0 ), 성공시 JWT 리턴
        pass

    def get_user_info_service(self, uid:int):
        # 유저의 정보 인출
        # 실패시 None, 성공시 유저 정보를 다음 형태의 딕셔너리로 반환.
        # {
        #   'stdid':stdid,
        #   'email':email,
        #   'nickname':nickname
        # }
        pass

    def change_info_service(self, uid:int, nickname:str, email:str):
        # 유저 정보변경 수행
        # 실패시 None, 성공시 변경된 정보를 다음과 같은 형태의 딕셔너리로 반환
        # { 
        #   'nickname':nickname,
        #   'email':email
        # }
        pass

    def change_pwd_service(self, uid:int, pwd:str):
        # 비밀번호 변경 수행
        # 실패시 None, 성공시 200 반환
        pass

    def withdraw_service(self, uid:int, pwd:str):
        # 비밀번호 먼저 검증 후 탈퇴 수행
        # 실패시 None, 성공시 200 반환
        pass

    def promote(self):
        # 매년 3월, 모든 유저의 grade를 1씩 증가
        pass