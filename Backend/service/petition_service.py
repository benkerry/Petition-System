from ..dao import PetitionDao
from flask import g

class PetitionService:
    def __init__(self, dao:PetitionDao, expire_left:int, pass_ratio:int):
        self.dao = dao
        self.expire_left = expire_left
        self.pass_ratio = pass_ratio

    def get_petition_metadata_service(self, count:int, type:str = "all"):
        # count만큼의 type 청원을 꺼낸다.
        # type의 종류: "all", "newest", "hottest", "oldest", "answered"
        # 각각 가장 최신의 청원, 가장 동의가 많은 청원, 가장 기간종료와 가까운 청원, 가장 최근에 답변이 달린 청원을 count개 인출한다.
        # 실패시 None, 성공시 다음과 같은 형태의 이중 딕셔너리로 데이터 반환
        # {
        #   id:{
        #       'status':status,
        #       'title':title,
        #       'answer_exists':0 or 1(답변 존재 여부),
        #       'support_count':support_count(동의 갯수)
        #   },
        #   .
        #   .
        #   .
        # }
        pass

    def get_petition_service(self, petition_id:int):
        # petition_id에 해당하는 청원의 정보를 반환.
        # 실패시 None, 성공시 다음과 같은 형태의 딕셔너리 반환
        # {
        #   'status':status,
        #   'created_at':created_at(YYYY-MM-DD HH:MM),
        #   'title':title,
        #   'contents':contents,
        #   'answer':answer,
        #   'expire_left':expire_left
        # }
        pass

    def write_petition_service(self, author_id:int, title:str, contents:str, expire_left:int):
        # 청원 등록
        # 실패시 None, 성공시 200 반환
        pass
    
    def support_petition_service(self, uid:int, petition_id:int):
        # 청원 동의, 닫힌 청원에는 불가능하도록.
        # 실패시 None, 이미 동의한 청원일 시 -1, 청원의 Status Code가 1인 경우 0, 성공시 200 반환
        pass

    def add_day_request_service(self, uid:int, petition_id:int, comment:str):
        # 청원 만료기한 연장 요청
        # 실패시 None, 성공시 200 반환
        pass

    def check_petitions(self):
        # 매일 실행되어, 동의 수가 일정 이상인 청원의 Status Code를 갱신.
        # 동의 수 미달성 상태로 일정 기간 지난 청원의 Status Code도 갱신.
        # Status Code: 0 - 열림, 1 - 기간 만료 닫힘, 2 - 동의 목표 달성, 3 - 답변 완료, 4 - 관리자 직권 닫힘
        # 통과된 청원들을 모든 유저에게 이메일로 보냄.
        pass