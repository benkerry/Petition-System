from sqlalchemy import text

class UserDao:
    # 여기에서는 users, authcodes 테이블에만 액세스하도록 한다.
    def __init__(self, db):
        self.db = db

    def get_authcode(self, stdid:int):
        data = self.db.execute(text("""
            SELECT stdid, code, root, validating
            FROM authcodes
            WHERE stdid = :stdid
        """), {
            "stdid":stdid
        }).fetchone()

        if data != None:
            return {
                "stdid":data[0],
                "code":data[1],
                "root":data[2],
                "validating":data[3]
            }
        else:
            return None

    def insert_user_staged(self, email:str, hashed_pwd:str, nickname:str, grade:int, priv:str):
        return self.db.execute(text("""
            INSERT INTO users_staged(
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
        # 유저를 삭제.
        # 실패시 None, 성공시 Transaction 이후 전체 유저의 수 반환.
        pass

    def get_user(self, email:str = None, uid:int = None):
        # 유저 정보(학번, 이메일, 해시된 패스워드, 닉네임, 인증여부)를 인출.
        # 이메일이 들어오면 이메일을, uid가 들어오면 uid를 사용. 둘 다 들어오면 맘대로~~
        # 실패시 None, 성공시 (학번, 이메일, 해시된 패스워드, 닉네임) 딕셔너리로 반환
        pass

    def update_user_info(self, uid:int, nickname:str):
        # uid에 해당하는 유저 정보(nickname)를 parameter로 들어온 nickname으로 업데이트.
        # 실패시 None, 성공시 전체 유저 수 반환
        pass

    def update_pwd(self, uid:int, hashed_pwd:str):
        # uid에 해당하는 유저의 해시 패스워드를 업데이트.
        # 실패시 None, 성공시 전체 유저 수 반환.
        pass

    def get_all_email(self):
        data = self.db.execute(text("""
            SELECT email
            FROM users
        """)).fetchall()

        if data != None:
            rtn = []
            for i in data:
                rtn.append(i)
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
                rtn.append(i)    
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
                rtn.append(i)
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

    def update_user_email(self, email:str, new_email:str):
        return self.db.execute(text("""
            UPDATE users
            SET email = :new_email
            WHERE email = :email
        """), {
            "new_email":new_email,
            "email":email
        }).lastrowid

    def update_privilege(self, uid:int, priv:int):
        # uid에 해당하는 유저의 권한을 변경함.
        # 실패시 None, 성공시 전체 유저 수 반환.
        pass

    def process_promote(self):
        # 모든 유저의 grade 값을 1씩 올린다.
        # 실패시 None, 성공시 1
        pass