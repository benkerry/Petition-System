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
                a.reports,
                a.petition_id,
                a.description
            FROM users AS u
            LEFT JOIN
            (
                SELECT
                    p.author_id,
                    p.reports,
                    r.petition_id, 
                    r.description 
                FROM reports AS r
                LEFT JOIN petitions AS p ON r.petition_id = p.id
            ) AS a ON a.author_id = u.id
        """))

        result = []

        for i in data:
            result.append(
                {
                    "nickname":i[0],
                    "reports":i[1],
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
        sql = "INSERT INTO authcodes(grade, code, root, expire_at) VALUES"

        for authcode in authcodes:
            sql += f"(:grade, {authcode}, :priv, DATE_ADD(NOW(), INTERVAL :life DAY)),"

        sql = sql[:-1]

        return self.db.execute(text(sql),{
            "grade":grade,
            "priv":priv,
            "life":life
        }).lastrowid

    def get_all_authcode(self, stdid:tuple):
        # stdid(학번 등 개인고유번호)의 튜플을 받아 DB에서 해당 학번의 인증번호를 인출.
        # 해당하는 모든 인증번호를 2차원 튜플 ( (stdid, authcode), ... ) 형태로 반환
        pass

    def get_add_day(self, petition_id:int):
        # 해당 청원 만료기한 연장 요청 상황 확인,
        # 실패시 None, 성공시 ( (req_id, comment), ... ) 반환
        pass