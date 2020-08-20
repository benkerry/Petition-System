from sqlalchemy import text

class UserDao:
    def __init__(self, db):
        self.db = db

    def get_authcode(self, stdid:int):
        data = self.db.execute(text("""
            SELECT stdid, code, root
            FROM authcodes
            WHERE stdid = :stdid
        """), {
            "stdid":stdid
        }).fetchone()

        if data != None:
            return {
                "stdid":data[0],
                "code":data[1],
                "root":data[2]
            }
        else:
            return None

    def delete_authcode(self, authcode:str):
        return self.db.execute(text("""
            DELETE FROM authcodes WHERE code = :authcode
        """),{
            "code":authcode
        }).lastrowid

    def insert_user(self, email:str, hashed_pwd:str, nickname:str, grade:int, priv:str):
        return self.db.execute(text("""
            INSERT INTO users(
                email,
                hashed_pwd,
                nickname,
                grade,
                root,
                validated
            )
            VALUES(
                :email,
                :hashed_pwd,
                :nickname,
                :grade,
                :root,
                0
            )
        """), {
            "email":email,
            "hashed_pwd":hashed_pwd,
            "nickname":nickname,
            "grade":grade,
            "root":priv
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

    def delete_withdrawed_user(self):
        return self.db.execuet(text("""
            DELETE users
            WHERE TIMESTAMPDIFF(day, withdraw_at, NOW()) > 13
        """)).lastrowid

    def update_withdraw(self, uid:int):
        return self.db.execute(text("""
            UPDATE users
            SET withdraw_at = NOW()
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
                    root,
                    validated
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
                    root,
                    validated
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
                "root":data[4],
                "validated":data[5]
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
            WHERE root > 0
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

    def update_user_email(self, uid:int, new_email:str):
        return self.db.execute(text("""
            UPDATE users
            SET email = :new_email
            WHERE id = :uid
        """), {
            "new_email":new_email,
            "uid":uid
        }).lastrowid

    def update_privilege(self, uid:int, priv:int):
        # uid에 해당하는 유저의 권한을 변경함.
        # 실패시 None, 성공시 전체 유저 수 반환.
        pass

    def process_promote(self):
        # 모든 유저의 grade 값을 1씩 올린다.
        # 실패시 None, 성공시 1
        pass