from functools import wraps
from flask import Response, request, current_app, jsonify, g

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # JWT 검증 절차 수행
        return f(*args, *kwargs)

    return decorated_function

def priv_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # 관리자가 맞는지 검증 수행
        return f(*args, **kwargs)

    return decorated_function

def create_endpoints(app, services, expire_left:int, pass_ratio:int):
    # User Services
    @app.route("/register", methods = ["POST"])
    def register():
        payload = request.json

        stdid = payload['stdid']
        authcode = payload['authcode']
        email = payload['email']
        pwd = payload['pwd']
        pwd_chk = payload['pwd_chk']
        nickname = payload['nickname']

        return services.user_service.regist_service(stdid, authcode, email, pwd, pwd_chk, nickname)

    @app.route("/login", methods = ["POST"])
    def login():
        pass

    @app.route("/get-user-info", methods = ["POST"])
    @login_required
    def get_user_info():
        pass

    @app.route("/change-my-info", methods = ["POST"])
    @login_required
    def change_my_info():
        pass

    @app.route("/change-my-pwd", methods = ["POST"])
    @login_required
    def change_my_pwd():
        pass

    @app.route("/withdraw", methods = ["POST"])
    @login_required
    def withdraw():
        pass

    # Petition Services
    @app.route("/get-petition-metadatas", methods = ["POST"])
    def get_petition_metadatas():
        pass

    @app.route("/get-petition", methods = ["POST"])
    def get_petition():
        pass

    @app.route("/write-petition", methods = ["POST"])
    @login_required
    def write_petition():
        pass

    @app.route("/support-petition", methods = ["POST"])
    @login_required
    def support_petition():
        pass

    @app.route("/add-day-request", methods = ["POST"])
    @login_required
    def add_day_request():
        pass

    # Debate Services
    @app.route("/write-debate", methods = ["POST"])
    @login_required
    def write_debate():
        pass

    @app.route("/get-debate", methods = ["POST"])
    def get_debate():
        pass

    # Manager Services
    @app.route("/delete-user", methods = ["POST"])
    @login_required
    @priv_required
    def delete_user():
        pass

    @app.route("/change-priv", methods = ["POST"])
    @login_required
    @priv_required
    def change_priv():
        pass

    @app.route("/get-all-nicknames", methods = ["POST"])
    @login_required
    @priv_required
    def get_all_nicknames():
        pass

    @app.route("/generate-authcodes", methods = ["POST"])
    @login_required
    @priv_required
    def generate_authcodes():
        pass

    @app.route("/close-petition", methods = ["POST"])
    @login_required
    @priv_required
    def close_petition():
        pass

    @app.route("/open-petition", methods = ["POST"])
    @login_required
    @priv_required
    def open_petition():
        pass

    @app.route("/set-expire-left", methods = ["POST"])
    @login_required
    @priv_required
    def set_expire_left():
        set_data = request.json['expire_left']
        expire_left = set_data

        fp = open(".config/config.expire_left", 'w')
        fp.write(set_data)
        fp.close()

        return '', 200

    @app.route("/add-day", methods = ["POST"])
    @login_required
    @priv_required
    def add_day():
        pass

    @app.route("/set-pass-ratio", methods = ["POST"])
    @login_required
    @priv_required
    def set_pass_ratio():
        set_data = request.json['pass_ratio']
        pass_ratio = set_data

        fp = open(".config/config.pass_ratio", 'w')
        fp.write(set_data)
        fp.close()

        return '', 200

    @app.route("/get-settings", methods = ["POST"])
    @login_required
    @priv_required
    def get_settings():
        # expire_left와 pass_ratio 및 현 전체 유저 수 반환
        pass

    @app.route("/get-add-day-request", methods = ["POST"])
    @login_required
    @priv_required
    def get_add_day_request():
        pass

    ##### 답변 작성
    ##### 신고 및 처리 기능
    ##### 임의 답변 및 처리 기능
    ##### 이메일 인증 기능(gmail, naver, korea, daum, hanmail 제한) -> 이메일 인증 디비 만들자