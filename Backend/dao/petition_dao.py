from sqlalchemy import text

class PetitionDao:
    # 여기서는 petition, supports 테이블만 다룬다.
    def __init__(self, db):
        self.db = db

    def insert_petition(self, uid:int, title:str, contents:str, expire_left:int):
        return self.db.execute(text("""
            INSERT INTO petitions(
                author_id,
                title,
                contents,
                expire_at
            ) VALUES(
                :uid,
                :title,
                :contents,
                DATE_ADD(NOW(), INTERVAL :expire_left DAY)
            )
        """), {
            "uid":uid,
            "title":title,
            "contents":contents,
            "expire_left":expire_left
        }).lastrowid

    def insert_support(self, uid:int, petition_id:int):
        count = self.db.execute(text("""
            SELECT COUNT(*) FROM supports 
            WHERE uid = :uid AND petition_id = :petition_id
        """), {
            "uid":uid,
            "petition_id":petition_id
        }).fetchone()[0]

        status = self.db.execute(text("""
            SELECT status FROM petitions WHERE id = :petition_id
        """), {
            "petition_id":petition_id
        }).fetchone()[0]

        if count == 1 or status != 0:
            return None
        else:
            self.db.execute(text("""
                INSERT INTO supports
                VALUES(
                    :uid,
                    :petition_id
                )
            """), {
                "uid":uid,
                "petition_id":petition_id
            })

            return self.db.execute(text("""
                UPDATE petitions
                SET supports = supports + 1
                WHERE id = :petition_id
            """), {
                "petition_id":petition_id
            }).lastrowid

    def update_petition_status(self, petition_id:int, status_code:int):
        # 청원의 상태 코드를 갱신한다.
        # 실패시 None, 성공시 전체 청원의 갯수를 반환한다.
        pass

    def get_petition_metadatas(self, count:int, petition_type:str):     
        result = []
        data = None
        sql = """
            SELECT
                id,
                title,
                date_format(created_at, "%Y-%m-%dT%H:%i:%S"),
                supports,
                contents
            FROM petitions
        """

        if petition_type == "newest":
            sql += " WHERE status = 0 ORDER BY id DESC"
        elif petition_type == "oldest":
            sql += " WHERE status = 0 ORDER BY id ASC"
        elif petition_type == "supportest":
            sql += " WHERE status = 0 ORDER BY supports DESC, id DESC"
        elif petition_type == "newest_passed":
            sql += " WHERE status = 1 ORDER BY passed_at DESC"
        else:
            sql += " WHERE status <= 1 ORDER BY id DESC"

        if count:
            sql += " LIMIT :count"
            data = self.db.execute(text(sql), {
                "count":count
            })
        else:
            data = self.db.execute(text(sql))

        for i in data:
            if petition_type == "all_for_search":
                result.append({
                    "id":i[0],
                    "title":i[1],
                    "created_at":i[2],
                    "supports":i[3],
                    "content":i[4]
                })
            else:
                result.append({
                    "id":i[0],
                    "title":i[1],
                    "created_at":i[2],
                    "supports":i[3]
                })

        return result

    def get_petition(self, petition_id:int, pass_ratio:int):
        result = dict()
        data = self.db.execute(text("""
            SELECT
                title,
                contents,
                date_format(created_at, "%Y-%m-%dT%H:%i:%S"),
                date_format(expire_at, "%Y-%m-%dT%H:%i:%S"),
                supports,
                status
            FROM petitions
            WHERE id = :petition_id
        """), {
            "petition_id":petition_id
        }).fetchone()

        result["title"] = data[0]
        result["contents"] = data[1]
        result["created_at"] = data[2]
        result["expire_at"] = data[3]
        result["supports"] = str(data[4])
        result["status"] = data[5]

        data = self.db.execute(text("""
            SELECT COUNT(*) FROM users
        """)).fetchone()[0]

        if data < 30:
            result["supports"] = "회원 수 부족으로 청원 동의 시스템이 정지 상태입니다."
        else:
            result["supports"] += " / " + str((data * pass_ratio) // 100)

        return result

    def get_petition_status(self, petition_id:int):
        data = self.db.execute(text("""
            SELECT status FROM petitions WHERE id = :petition_id
        """), {
            "petition_id":petition_id
        })

        return data.fetchone()[0] if data else None