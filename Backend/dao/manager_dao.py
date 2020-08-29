from sqlalchemy import text

class ManagerDao:
    def __init__(self, db):
        self.db = db

    def get_user_count(self):
        return self.db.execute(text("""
            SELECT COUNT(*) FROM users
        """)).fetchone()[0]

    def get_reports(self):
        data = self.db.execute(text("""
            SELECT
                u.nickname,
                a.author_id,
                a.petition_id,
                a.description,
                a.reports,
                a.status,
                a.id
            FROM users AS u
            LEFT JOIN
            (
                SELECT
                    p.author_id,
                    p.reports,
                    r.petition_id, 
                    r.description,
                    p.status,
                    r.id
                FROM reports AS r
                LEFT JOIN petitions AS p ON r.petition_id = p.id
            ) AS a ON a.author_id = u.id
            WHERE status = 0 AND reports >= 10
            ORDER BY id DESC
        """))

        result = []

        for i in data:
            result.append(
                {
                    "nickname":i[0],
                    "author_id":i[1],
                    "pid":i[2],
                    "description":i[3]
                }
            )

        return result

    def get_authcode_count(self):
        result = dict()
        data = self.db.execute(text("""
            SELECT 
                priv,
                COUNT(priv) AS cnt
            FROM authcodes
            GROUP BY priv
        """)).fetchall()

        if data:
            for i in data:
                result["manager" if i[0] == 2 else "general"] = i[1]
        
        return result

    def insert_authcode(self, grade:int, authcodes:tuple, priv:int, life:int):
        sql = "INSERT INTO authcodes(grade, code, priv, expire_at) VALUES"

        for authcode in authcodes:
            sql += f"(:grade, \"{authcode}\", :priv, DATE_ADD(NOW(), INTERVAL :life DAY)),"

        sql = sql[:-1]

        return self.db.execute(text(sql),{
            "grade":grade,
            "priv":priv,
            "life":life
        }).lastrowid

    def truncate_authcodes(self):
        self.db.execute(text("""TRUNCATE authcodes"""))

    def insert_notice(self, uid:int, title:str, content:str):
        return self.db.execute(text("""
            INSERT INTO notices(
                author_id,
                title,
                contents
            )
            VALUES(
                :uid,
                :title,
                :contents
            )
        """), {
            "uid":uid,
            "title":title,
            "contents":content
        }).lastrowid

    def get_notice_metadata(self):
        data = self.db.execute(text("""
            SELECT 
                id,
                title,
                date_format(created_at, "%Y-%m-%dT%H:%i:%S")
            FROM notices
            ORDER BY created_at DESC
        """))

        result = []
        for i in data:
            result.append({
                "id":i[0],
                "title":i[1],
                "created_at":i[2]
            })

        return result

    def get_notice(self, nid:int):
        data = self.db.execute(text("""
            SELECT 
                title,
                date_format(created_at, "%Y-%m-%dT%H:%i:%S"),
                contents
            FROM notices
            WHERE id = :nid
        """), {
            "nid":nid
        }).fetchone()

        if data:
            return {
                "title":data[0],
                "created_at":data[1],
                "content":data[2]
            }
        else:
            return None