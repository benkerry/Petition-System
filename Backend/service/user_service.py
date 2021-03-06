import jwt
import bcrypt
from threading import Thread, Timer
from flask import current_app, jsonify
from datetime import datetime, timedelta
from dao import UserDao
from .mail_service import Mailer
class UserService:
    def __init__(self, dao:UserDao, mailer:Mailer, config):
        self.dao = dao
        self.mailer = mailer
        self.config = config
        self.tr = Thread(target = self.check_expired_users_n_authcodes)
        self.tr.start()

    def is_valid_email(self, email:str):
        support_mails = ["@korea.kr", "@daum.net", "@hanmail.net", "@naver.com", "@gmail.com", "@kakao.com"]

        for i in support_mails:
            if email.find(i) != -1:
                return True

        return False

    def send_validate_mail(self, email, new_email = "", pwd = "",  mode = "send"):
        mode = mode.lower()
        user = self.dao.get_user(email=email)

        if mode == "resend" or mode == "fucked":
            if email not in self.dao.get_all_email():
                return "가입 시도 기록을 찾을 수 없습니다.\n뭔가 이상하다면 developerkerry@naver.com으로 메일 바랍니다.", 500

        if mode == "fucked":
            hashed_pwd = user["hashed_pwd"]
            if not bcrypt.checkpw(pwd.encode("UTF-8"), hashed_pwd.encode("UTF-8")):
                return "비밀번호가 틀립니다.", 401
            else:
                self.dao.update_user_email(user["uid"], new_email)
                email = new_email

        if user['validated']:
            return "이미 인증된 사용자입니다.", 403

        token = jwt.encode({
            'user_email': email,
            'exp': datetime.utcnow() + timedelta(seconds= 60 * 60 * 24 * 7)
        }, current_app.config["JWT_SECRET_KEY"], "HS256")

        title = "[청원 시스템] 가입 인증 메일입니다. 유효기간은 7일입니다."
        content = f"""
        링크를 클릭하세요! >>> https://{self.config.svr_addr}/validate?token={token.decode("UTF-8")}
        링크 클릭 후 성공 메시지를 꼭 확인하시길 바랍니다.
        여러 번 인증을 시도해도 성공 메시지가 보이지 않는다면 먼저 서비스 로그인을 시도해 보시고,
        로그인이 되지 않는다면 developerkerry@naver.com으로 도움을 요청하세요."""

        self.mailer.send(title, content, [email])
        return "재전송 성공!", 200

    def validate(self, email):
        self.dao.process_validate(email)
        return "<script>alert(\"인증 성공!\");</script>"

    def regist_service(self, grade:int, authcode:str, email:str, pwd:str, pwd_chk:str, nickname:str):
        if not self.is_valid_email(email):
            return "지원하지 않는 이메일이거나, 이메일 형식이 잘못되었습니다.", 400
        elif pwd != pwd_chk:
            return "비밀번호와 비밀번호 확인 란의 값이 다릅니다.", 400
        elif len(pwd) < 8:
            return "비밀번호가 너무 짧습니다. 8자 이상이어야 합니다.", 400
        elif email in self.dao.get_all_email():
            return "이미 가입된 이메일입니다.", 400
        elif nickname in self.dao.get_all_nickname():
            return "이미 존재하는 닉네임입니다.", 400
        else:
            db_authcode = self.dao.get_authcode(authcode)

            if not db_authcode:
                return "인증번호가 틀립니다.", 401
            elif int(grade) != db_authcode["grade"] or authcode.upper() != db_authcode["code"].upper():
                return "인증번호가 틀립니다.", 401

            hashed_pwd = bcrypt.hashpw(
                pwd.encode("UTF-8"),
                bcrypt.gensalt()
            )

            priv = db_authcode["priv"]

            try:
                self.dao.insert_user(email, hashed_pwd, nickname, grade, priv)
            except:
                return "이미 가입된 사용자입니다.", 400

            self.dao.delete_authcode(authcode)
            self.send_validate_mail(email)
            return "가입 완료", 200

    def login_service(self, email:str, pwd:str):
        user = self.dao.get_user(email)

        if user == None:
            return "아이디 또는 비밀번호가 틀립니다.", 401
        else:
            if bcrypt.checkpw(pwd.encode("UTF-8"), user["hashed_pwd"].encode("UTF-8")):
                if not user["validated"]:
                    return "이메일 인증을 진행하지 않으셨습니다.", 401
                elif user["withdrawed"]:
                    return "탈퇴한 회원이거나, 신고로 인해 삭제된 유저입니다.", 401
                else:
                    response = {
                        "email":user["email"],
                        "nickname":user["nickname"],
                        "priv":user["priv"],
                        "token":self.generate_access_token(user['uid'], user["priv"])
                    }
                    return jsonify(response)
            else:
                return "아이디 또는 비밀번호가 틀립니다.", 401

    def generate_access_token(self, uid:int, priv:int) -> str:
        return jwt.encode({
            "uid":uid,
            "priv":priv,
            'exp': datetime.utcnow() + timedelta(seconds= 60 * 60 * 24)
        }, current_app.config['JWT_SECRET_KEY'], "HS256").decode("UTF-8")

    def change_info_service(self, uid:int, nickname:str):
        self.dao.update_user_nickname(uid, nickname)
        return "정보 변경 성공", 200

    def change_pwd_service(self, uid:int, pwd:str, pwd_chk:str, old_pwd:str):
        if pwd != pwd_chk:
            return "비밀번호와 비밀번호 확인 란의 값이 다릅니다.", 400
        elif len(pwd) < 8:
            return "비밀번호가 너무 짧습니다. 비밀번호는 8자 이상이어야 합니다.", 400
        else:
            user = self.dao.get_user(uid=uid)
            hashed_pwd = user["hashed_pwd"]

            if bcrypt.checkpw(old_pwd.encode("UTF-8"), hashed_pwd.encode("UTF-8")):
                hashed_pwd = bcrypt.hashpw(pwd.encode("UTF-8"), bcrypt.gensalt())
                self.dao.update_pwd(uid, hashed_pwd)
                return "비밀번호 변경 성공", 200
            else:
                return "현재 비밀번호를 잘못 입력하셨습니다.", 401

    def withdraw_service(self, uid:int, pwd:str):
        hashed_pwd = self.dao.get_user(uid = uid)["hashed_pwd"]
        
        if bcrypt.checkpw(pwd.encode("UTF-8"), hashed_pwd.encode("UTF-8")):
            self.dao.update_withdraw(uid)
            return "성공!", 200
        else:
            return "비밀번호가 틀렸습니다.", 401

    def check_expired_users_n_authcodes(self):
        self.dao.delete_expired_user()
        self.dao.delete_expired_authcode()
        print("Expired Users and Authcodes Checked!")
        Timer(600, self.check_expired_users_n_authcodes).start()