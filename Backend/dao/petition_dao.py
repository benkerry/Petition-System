from sqlalchemy import text

class PetitionDao:
    # 여기서는 petition, supports 테이블만 다룬다.
    def __init__(self, db):
        self.db = db

    def insert_petition(self, uid:int, title:str, contents:str):
        return self.db.execute(text("""
            INSERT INTO petitions(
                author_id,
                title,
                contents,
                created_at,
                status
            ) VALUES(
                :uid,
                :title,
                :contents,
                NOW(),
                0
            )
        """), {
            "uid":uid,
            "title":title,
            "contents":contents,
        }).lastrowid

    def insert_support(self, stdid:int, petition_id:int):
        # 청원에 대한 동의를 등록한다.
        # 실패시 None, 이미 동의한 기록이 있는 경우 -1, 성공시 전체 동의의 갯수를 반환한다.
        pass

    def update_petition_answer(self, petition_id:int, answer:str):
        # 청원에 답변을 등록한다.
        # 실패시 None, 성공시 전체 청원의 갯수를 반환한다.
        pass

    def update_petition_status(self, petition_id:int, status_code:int):
        # 청원의 상태 코드를 갱신한다.
        # 실패시 None, 성공시 전체 청원의 갯수를 반환한다.
        pass

    def get_petition_supports(self, petition_id:int):
        # 해당 청원의 만료일 이전에 찍힌 동의의 수를 리턴한다.
        # 실패시 None, 성공시 동의자 수를 반환한다.
        pass

    def get_petition_metadatas(self, count):
        result = dict()
        data = self.db.execute(text("""
            SELECT 
                id, 
                title, 
                created_at, 
                status, 
                answer
            FROM petitions 
            ORDER BY id DESC
            LIMIT :count
        """), {
            "count":count
        })

        for i in data:
            result[i[0]] = {
                "title":i[1],
                "created_at":i[2],
                "status":i[3],
                "answer":i[4] != ""
            }

        return result

    def insert_add_day_request(self, uid:int, petition_id:int, comment:str):
        # 만료기한 연장 요청을 삽입
        # 실패시 None, 성공시 모든 만료 연장 요청 수 반환
        pass

    def update_expire_at(self, petition_id:int, add_day:int):
        # petition_id에 해당하는 청원의 만료일을 add_day만큼 추가함.
        # 실패시 None, 성공시 만료일 반환
        pass

    def get_petition(self, petition_id:int):
        # 청원 정보를 id로 인출
        # 실패시 None, 성공시 (id, title, contents, created_at, status, answer, expire_left) 형태로 반환한다.
        pass