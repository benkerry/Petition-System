import jwt
from functools import wraps
from flask import Response, request, current_app, jsonify, g

class Config:
    def __init__(self, pass_ratio, expire_left):
        self.pass_ratio = pass_ratio
        self.expire_left = expire_left

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("token")

        if token is not None:
            try:
                payload = jwt.decode(token, current_app.config["JWT_SECRET_KEY"], "HS256")

                g.uid = payload["uid"]
                g.priv = payload["priv"]
            except jwt.InvalidTokenError:
                return "잘못된 접근입니다.", 401
        else:
            return "잘못된 접근입니다.", 401
        return f(*args, *kwargs)

    return decorated_function

def priv_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.priv < 2:
            return "잘못된 접근입니다.", 401
        return f(*args, **kwargs)

    return decorated_function

def create_endpoints(app, services, config:Config):
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

    @app.route("/validate", methods = ["GET"])
    def validate():
        token = request.args.get("token")
        data = None
        
        try:
            data = jwt.decode(token, current_app.config["JWT_SECRET_KEY"], "HS256")
        except jwt.InvalidTokenError:
            return "잘못된 접근입니다.", 401

        return services.user_service.validate(data['user_email'])

    @app.route("/validate-mail-resend", methods = ["POST"])
    def validate_mail_resend():
        payload = request.json

        if payload['isValidateFucked'] == 0:
            return services.user_service.send_validate_mail(payload['email'], mode="resend")
        else:
            return services.user_service.send_validate_mail(payload['email'], payload['new_email'], payload['pwd'], mode="fucked")

    @app.route("/login", methods = ["POST"])
    def login():
        payload = request.json
        return services.user_service.login_service(payload["email"], payload["pwd"])

    @app.route("/change-my-info", methods = ["POST"])
    @login_required
    def change_my_info():
        payload = request.json
        return services.user_service.change_info_service(g.uid, payload["email"], payload["nickname"])

    @app.route("/change-my-pwd", methods = ["POST"])
    @login_required
    def change_my_pwd():
        payload = request.json
        return services.user_service.change_pwd_service(g.uid, payload["pwd"], payload["pwd_chk"], payload["old_pwd"])

    @app.route("/withdraw", methods = ["POST"])
    @login_required
    def withdraw():
        payload = request.json
        return services.user_service.withdraw_service(g.uid, payload["pwd"])

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
        payload = request.json
        return services.petition_service.write_petition_service(g.uid, payload["title"], payload["content"])

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
        config.expire_left = int(set_data)

        fp = open("config/config.expire_left", 'w')
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
        set_data = int(request.json['pass_ratio'])

        if set_data > 100:
            return "100 이상의 값은 입력하실 수 없습니다.", 400
        else:
            config.pass_ratio = set_data

            fp = open("config/config.pass_ratio", 'w')
            fp.write(str(set_data))
            fp.close()

            return '', 200

    @app.route("/get-settings", methods = ["POST"])
    @login_required
    @priv_required
    def get_settings():
        return jsonify({
            "user_count":services.manager_service.get_user_count(),
            "pass_ratio":config.pass_ratio,
            "expire_left":config.expire_left
        })

    @app.route("/get-add-day-request", methods = ["POST"])
    @login_required
    @priv_required
    def get_add_day_request():
        pass

    ##### 답변 작성
    ##### 신고 및 처리 기능
    ##### 임의 답변 및 처리 기능
    ##### 이메일 인증 기능(gmail, naver, korea, daum, hanmail 제한) -> 이메일 인증 디비 만들자