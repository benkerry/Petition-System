from sqlalchemy import text

class PetitionDao:
    # 여기서는 petition, supports 테이블만 다룬다.
    def __init__(self, db):
        self.db = db

    def insert_petition(self, author_id:int, title:str, contents:str):
        # 청원을 등록한다.
        # 실패시 None, 성공시 전체 청원의 갯수를 반환한다.
        pass

    def insert_support(self, stdid:int, petition_id:int):
        # 청원에 대한 동의를 등록한다.
        # 실패시 None, 이미 동의한 기록이 있는 경우 -1, 성공시 전체 동의의 갯수를 반환한다.
        pass

    def update_petition_answer(self, petition_id:int, answer:str):
        # 청원에 답변을 등록한다.
        # 실패시 None, 성공시 전체 청원의 갯수를 반환한다.
        pass

    def update_petition_status(self, petition_id, status_code:int):
        # 청원의 상태 코드를 갱신한다.
        # 실패시 None, 성공시 전체 청원의 갯수를 반환한다.
        pass

    def check_petition_supports(self, petition_id):
        # 해당 청원의 동의 수를 리턴한다.
        # 실패시 None, 성공시 동의자 수를 반환한다.
        pass

    def get_petition_metadatas(self, type:str):
        # DB에 있는, 파라미터로 주어진 상태 코드에 해당하는 모든 청원을 인출한다.
        # type의 종류: "all", "newest", "hottest", "oldest", "answered"
        # 실패시 None, 성공시 2차원 튜플을 ((id, title, status, answer), ... ) 형태로 반환한다.
        pass

    def insert_add_day_request(self, uid:int, petition_id:int, comment:str):
        # 만료기한 연장 요청을 삽입
        # 실패시 None, 성공시 모든 만료 연장 요청 수 반환
        pass

    def get_petition(self, petition_id:int):
        # 청원 정보를 id로 인출
        # 실패시 None, 성공시 (id, title, contents, created_at, status, answer) 형태로 반환한다.
        pass