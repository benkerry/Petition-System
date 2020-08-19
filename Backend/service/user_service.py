import jwt
import bcrypt
from flask import g, current_app
from datetime import datetime, timedelta
from dao import UserDao
from service import Mailer

class UserService:
    def __init__(self, dao:UserDao, mailer:Mailer):
        self.dao = dao
        self.mailer = mailer

    def send_validate_mail(self, email, new_email = "", pwd = "",  mode = "send"):
        mode = mode.lower()

        if mode == "resend" or mode == "fucked":
            if email not in self.dao.get_all_email():
                return 500, "가입 시도 기록을 찾을 수 없습니다.\n뭔가 이상하다면 developerkerry@naver.com으로 메일 바랍니다."

        if mode == "fucked":
            user = self.dao.get_user(email=email)
            hashed_pwd = user["hashed_pwd"]
            if not bcrypt.checkpw(pwd.encode("UTF-8"), hashed_pwd.encode("UTF-8")):
                return 500, "비밀번호가 틀립니다."
            else:
                self.dao.update_user_email(email, new_email)
                email = new_email

        token = jwt.encode({
            'user_email': email,
            'exp': datetime.utcnow() + timedelta(seconds= 60 * 60 * 24 * 7)
        }, current_app.config["JWT_SECRET_KEY"], "HS256")

        title = "[청원 시스템] 가입 인증 메일입니다. 유효기간은 7일입니다."
        content = "링크를 클릭하세요! >>> http://localhost:5000/validate?token=" + token.decode("UTF-8")
        self.mailer.send(title, content, [email])

    def validate(self, email):
        pass

    def generate_authcode(self, stdid:tuple):
        pass

    def regist_service(self, stdid:int, authcode:str, email:str, pwd:str, pwd_chk:str, nickname:str):
        if pwd != pwd_chk:
            return "비밀번호와 비밀번호 확인 란의 값이 다릅니다.", 400
        elif len(pwd) < 8:
            return "비밀번호가 너무 짧습니다. 8자 이상이어야 합니다.", 400
        elif email in self.dao.get_all_email():
            return "이미 가입된 이메일입니다.", 400
        elif nickname in self.dao.get_all_nickname():
            return "이미 존재하는 닉네임입니다.", 400
        else:
            db_authcode = self.dao.get_authcode(stdid)

            if not db_authcode:
                return "인증번호가 틀립니다.", 401
            elif stdid != db_authcode["stdid"] or authcode != db_authcode["code"]:
                return "인증번호가 틀립니다.", 401

            hashed_pwd = bcrypt.hashpw(
                pwd.encode("UTF-8"),
                bcrypt.gensalt()
            )

            root = db_authcode["root"]

            if self.dao.insert_user(email, hashed_pwd, nickname, db_authcode["stdid"] // 1000, root):
                self.send_validate_mail(email)
                return "가입 완료", 200
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