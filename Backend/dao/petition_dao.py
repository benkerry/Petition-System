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

    def reopen_petition(self, petition_id:int, expire_left = 0):
        self.db.execute(text("""
            UPDATE petitions 
            SET expire_at = DATE_ADD(NOW(), INTERVAL :expire_left DAY)
            WHERE id = :petition_id
        """), {
            "expire_left":expire_left,
            "petition_id":petition_id
        })

        return self.db.execute(text("""
            UPDATE petitions
            SET status = 0
            WHERE id = :petition_id
        """), {
            "petition_id":petition_id
        }).lastrowid

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
        elif petition_type == "expired":
            sql += " WHERE status = 2 ORDER BY expire_at DESC"
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
                u.nickname,
                p.title,
                p.contents,
                date_format(p.created_at, "%Y-%m-%dT%H:%i:%S"),
                date_format(p.expire_at, "%Y-%m-%dT%H:%i:%S"),
                p.supports,
                p.status
            FROM petitions AS p
            LEFT JOIN users AS u ON p.author_id = u.id
            WHERE p.id = :petition_id
        """), {
            "petition_id":petition_id
        }).fetchone()

        result["author"] = data[0]
        result["title"] = data[1]
        result["contents"] = data[2]
        result["created_at"] = data[3]
        result["expire_at"] = data[4]
        result["supports"] = str(data[5])
        result["status"] = data[6]

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
            SELECT title, status, supports FROM petitions WHERE id = :petition_id
        """), {
            "petition_id":petition_id
        }).fetchone()

        return data[0], data[1], data[2] if data else None

    def insert_report(self, uid:int, petition_id:int, description:str):
        exists = self.db.execute(text("""
            SELECT COUNT(*) FROM reports WHERE uid = :uid AND petition_id = :petition_id
        """), {
            "uid":uid,
            "petition_id":petition_id
        }).fetchone()[0]

        if exists or self.get_petition_status(petition_id)[1] != 0:
            return None
        else:
            self.db.execute(text("""
                UPDATE petitions
                SET reports = reports + 1
                WHERE id = :petition_id
            """), {
                "petition_id":petition_id
            })

            return self.db.execute(text("""
                INSERT INTO reports(
                    uid, 
                    petition_id, 
                    description
                )
                VALUES(
                    :uid,
                    :petition_id,
                    :description
                )
            """), {
                "uid":uid,
                "petition_id":petition_id,
                "description":description
            }).lastrowid