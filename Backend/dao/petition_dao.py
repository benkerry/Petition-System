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
                contents
            ) VALUES(
                :uid,
                :title,
                :contents
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

    def get_petition_metadatas(self, count):
        result = []
        data = None
        sql = """
            SELECT
                id,
                title,
                date_format(created_at, "%Y-%m-%dT%H:%i:%S"),
                supports
            FROM petitions
            WHERE status = 0
            ORDER BY id DESC
        """

        if count:
            sql += " LIMIT :count"
            data = self.db.execute(text(sql), {
                "count":count
            })
        else:
            data = self.db.execute(text(sql))

        for i in data:
            result.append({
                "id":i[0],
                "title":i[1],
                "created_at":i[2],
                "supports":i[4]
            })

        return result

    def get_petition(self, petition_id:int):
        result = dict()
        data = self.db.execute(text("""
            SELECT
                u.nickname,
                p.title,
                p.contents,
                date_format(p.created_at, "%Y-%m-%dT%H:%i:%S"),
                p.status
            FROM petitions AS p
            LEFT JOIN users AS u ON u.id = p.author_id
            WHERE p.id = :petition_id
        """), {
            "petition_id":petition_id
        })

        result["author"] = data[0]
        result["title"] = data[1]
        result["contents"] = data[2]
        result["created_at"] = data[3]
        result["status"] = data[3]

        return result

    def insert_add_day_request(self, uid:int, petition_id:int, comment:str):
        # 만료기한 연장 요청을 삽입
        # 실패시 None, 성공시 모든 만료 연장 요청 수 반환
        pass

    def update_expire_at(self, petition_id:int, add_day:int):
        # petition_id에 해당하는 청원의 만료일을 add_day만큼 추가함.
        # 실패시 None, 성공시 만료일 반환
        pass