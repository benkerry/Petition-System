from ..dao import UserDao
from flask import g

class UserService:
    def __init__(self, dao:UserDao):
        self.dao = dao

    def regist_service(self, grade:int, authcode:str, email:str, pwd:str, pwd_chk:str, nickname:str, root:int):
        # 회원가입 수행.
        # 실패시 오류 번호( n < 0 ), 성공시 200 리턴
        pass

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