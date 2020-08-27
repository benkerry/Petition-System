from sqlalchemy import text
from datetime import datetime,timedelta

class UserDao:
    def __init__(self, db):
        self.db = db

    def get_all_authcodes(self):
        result = []
        data = self.db.execute(text("""
            SELECT code FROM authcodes
        """)).fetchall()

        for i in data:
            result.append(i[0])

        return tuple(result)

    def get_authcode(self, authcode:str):
        data = self.db.execute(text("""
            SELECT grade, code, priv
            FROM authcodes
            WHERE code = :authcode
        """), {
            "authcode":authcode
        }).fetchone()

        if data != None:
            return {
                "grade":data[0],
                "code":data[1],
                "priv":data[2]
            }
        else:
            return None

    def delete_authcode(self, authcode:str):
        return self.db.execute(text("""
            DELETE FROM authcodes WHERE code = :authcode
        """),{
            "authcode":authcode
        }).lastrowid

    def insert_user(self, email:str, hashed_pwd:str, nickname:str, grade:int, priv:str):
        expire_at = None
        grade = int(grade)

        if grade > 0:
            expire_at = str(int(datetime.now().strftime("%Y")) + 4 - grade) + "-04-01 00:00:00"
        else:
            expire_at = str(int(datetime.now().strftime("%Y")) + 5) + "-04-01 00:00:00"

        return self.db.execute(text("""
            INSERT INTO users(
                email,
                hashed_pwd,
                nickname,
                grade,
                priv,
                validated,
                expire_at
            )
            VALUES(
                :email,
                :hashed_pwd,
                :nickname,
                :grade,
                :priv,
                0,
                :expire_at
            )
        """), {
            "email":email,
            "hashed_pwd":hashed_pwd,
            "nickname":nickname,
            "grade":grade,
            "priv":priv,
            "expire_at":expire_at
        }).lastrowid

    def delete_user(self, uid = -1, email = None):
        if uid > -1:
            return self.db.execute(text("""
                DELETE FROM users
                WHERE id = :uid
            """), {
                "uid":uid
            }).lastrowid
        elif email:
            return self.db.execute(text("""
                DELETE FROM users
                WHERE email = :email
            """), {
                "email":email
            }).lastrowid
        else:
            return None

    def update_withdraw(self, uid:int):
        self.db.execute(text("""
            UPDATE users
            SET withdrawed = 1
            WHERE id = :uid
        """), {
            "uid":uid
        })

        return self.db.execute(text("""
            UPDATE users
            SET expire_at = DATE_ADD(NOW(), INTERVAL 14 DAY)
            WHERE id = :uid
        """),{
            "uid":uid
        }).lastrowid

    def get_user(self, email:str = None, uid:int = None):
        user = None
        
        if email:
            data = self.db.execute(text("""
                SELECT 
                    id,
                    email,
                    hashed_pwd,
                    nickname,
                    priv,
                    validated,
                    withdrawed
                FROM users
                WHERE email = :email
            """), {
                "email":email
            }).fetchone()
        elif uid:
            data = self.db.execute(text("""
                SELECT 
                    id,
                    email,
                    hashed_pwd,
                    nickname,
                    priv,
                    validated,
                    withdrawed
                FROM users
                WHERE id = :id
            """), {
                "id":uid
            }).fetchone()
        else:
            return None

        if data != None:
            return {
                "uid":data[0],
                "email":data[1],
                "hashed_pwd":data[2],
                "nickname":data[3],
                "priv":data[4],
                "validated":data[5],
                "withdrawed": data[6]
            }
        else:
            return None

    def update_user_nickname(self, uid:int, nickname:str):
        return self.db.execute(text("""
            UPDATE users
            SET nickname = :nickname
            WHERE id = :uid
        """), {
            "nickname":nickname,
            "uid":uid
        }).lastrowid

    def update_pwd(self, uid:int, hashed_pwd:str):
        return self.db.execute(text("""
            UPDATE users
            SET hashed_pwd = :hashed_pwd
            WHERE id = :uid
        """), {
            "hashed_pwd":hashed_pwd,
            "uid":uid
        }).lastrowid

    def get_all_email(self):
        data = self.db.execute(text("""
            SELECT email
            FROM users
        """)).fetchall()

        if data != None:
            rtn = []
            for i in data:
                rtn.append(i[0])
            return tuple(rtn)
        else:
            return None

    def get_all_manager_email(self):
        data = self.db.execute(text("""
            SELECT email
            FROM users
            WHERE priv > 1
        """))

        if data != None:
            rtn = []
            for i in data:
                rtn.append(i[0])    
            return tuple(rtn)
        else:
            return None

    def get_all_nickname(self):
        data = self.db.execute(text("""
            SELECT nickname
            FROM users
        """)).fetchall()

        if data != None:
            rtn = []
            for i in data:
                rtn.append(i[0])
            return tuple(rtn)
        else:
            return None

    def process_validate(self, email:str):
        return self.db.execute(text("""
            UPDATE users
            SET validated = 1
            WHERE email = :email
        """), {
            "email":email
        }).lastrowid

    def delete_expired_user(self):
        self.db.execute(text("""
            DELETE FROM users
            WHERE TIMESTAMPDIFF(SECOND, expire_at, NOW()) > 0
        """))

    def delete_expired_authcode(self):
        self.db.execute(text("""
            DELETE FROM authcodes
            WHERE TIMESTAMPDIFF(SECOND, expire_at, NOW()) > 0
        """))