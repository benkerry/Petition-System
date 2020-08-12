from ..dao import UserDao
from flask import g

class UserService:
    def __init__(self, dao:UserDao):
        self.dao = dao

    def regist_service(self, stdid:int, authcode:str, email:str, pwd:str, pwd_chk:str, nickname:str, root:int):
        # 회원가입 수행.
        # 실패시 오류 번호( n < 0 ), 성공시 uid 리턴
        pass

    def login_service(self, email:str, pwd:str):
        # 로그인 수행.
        # 실패시 오류 번호( n < 0 ), 성공시 JWT 리턴
        pass

    def change_info_service(self, uid:int, nickname:str, email:str):
        # 유저 정보변경 수행
        # 실패시 None, 성공시 변경된 정보 튜플(nickname, email) 반환
        pass

    def change_pwd_service(self, uid:int, pwd:str):
        # 비밀번호 변경 수행
        # 실패시 None, 성공시 200 반환
        pass

    def change_priv_service(self, uid:int, tgt_nickname:str, priv:int):
        # 권한 변경 수행
        # 실패시 None, 성공시 200 반환
        pass
