from dao import DebateDao

class DebateService:
    def __init__(self, dao:DebateDao):
        self.dao = dao

    def write_debate_service(self, uid:int, petition_id:int, contents:str):
        # 토론을 등록
        # 실패시 None, 성공시 200
        pass

    def get_debate_service(self, petition_id:int):
        # petition_id에 해당하는 토론들을 모두 인출.
        # 실패시 None, 성공시 다음과 같은 형태의 이중 딕셔너리 반환
        # {
        #   id:{
        #       'nickname':nickname,
        #       'contents':contents,
        #       'created_at':created_at
        #   },
        #   .
        #   .
        #   .
        # ]
        pass