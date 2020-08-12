class DebateDao():
    # 여기에서는 debate 테이블과 users(nickname)까지만 접근하도록 한다.
    def __init__(self, db):
        self.db = db

    def insert_debate(self, petition_id:int, author_id:int, contents:str):
        # petition_id에 해당하는 청원에 토론을 등록.
        # 실패시 None, 성공시 전체 청원 수 반환.
        pass