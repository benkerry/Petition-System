import jwt
from functools import wraps
from flask import Response, request, current_app, jsonify, g

class Config:
    def __init__(self, pass_ratio, expire_left):
        self.pass_ratio = pass_ratio
        self.expire_left = expire_left
        self.pass_line = 0

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
                return "로그인이 필요합니다.", 401
        else:
            return "로그인이 필요합니다.", 401
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

        grade = payload['grade']
        authcode = payload['authcode']
        email = payload['email']
        pwd = payload['pwd']
        pwd_chk = payload['pwd_chk']
        nickname = payload['nickname']

        return services.user_service.regist_service(grade, authcode, email, pwd, pwd_chk, nickname)

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
        return services.user_service.change_info_service(g.uid, payload["nickname"])

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
        payload = request.json

        if payload.get("count", True):
            return services.petition_service.get_petition_metadata_service(petition_type = payload["petition_type"])
        else:
            return services.petition_service.get_petition_metadata_service(payload["count"], payload["petition_type"])

    @app.route("/get-petition", methods = ["POST"])
    def get_petition():
        petition_id = request.json["petition_id"]
        return services.petition_service.get_petition_service(petition_id)

    @app.route("/write-petition", methods = ["POST"])
    @login_required
    def write_petition():
        payload = request.json
        return services.petition_service.write_petition_service(g.uid, payload["title"], payload["content"])

    @app.route("/support-petition", methods = ["POST"])
    @login_required
    def support_petition():
        pid = request.json["petition_id"]
        return services.petition_service.support_petition_service(g.uid, pid)

    @app.route("/report-petition", methods = ["POST"])
    @login_required
    def report_petition():
        payload = request.json
        petition_id = payload["petition_id"]
        description = payload["description"]

        return services.petition_service.report_service(g.uid, petition_id, description)
        
    # Manager Services
    @app.route("/get-petition-status", methods = ["POST"])
    @login_required
    @priv_required
    def get_petition_status():
        return services.manager_service.get_petition_status(request.json["petition_id"])

    @app.route("/get-reports", methods = ["POST"])
    @login_required
    @priv_required
    def get_reports():
        return services.manager_service.get_report_service()

    @app.route("/deactivate-petition", methods = ["POST"])
    @login_required
    @priv_required
    def deactivate_petition():
        return services.manager_service.deactivate_petition_service(request.json["pid"])

    @app.route("/delete-user", methods = ["POST"])
    @login_required
    @priv_required
    def delete_user():
        return services.manager_service.delete_user_service(request.json["uid"])

    @app.route("/get-authcode-count", methods = ["POST"])
    @login_required
    @priv_required
    def get_authcode_count():
        return services.manager_service.get_authcode_count()

    @app.route("/generate-authcodes", methods = ["POST"])
    @login_required
    @priv_required
    def generate_authcodes():
        grade, count, priv, life = request.json["grade"], request.json["count"], request.json["priv"], request.json["life"]
        return services.manager_service.generate_authcode_service(grade, count, priv, life)

    @app.route("/truncate-authcodes", methods = ["POST"])
    @login_required
    @priv_required
    def truncate_authcodes():
        services.manager_service.truncate_authcodes_service()
        return "성공", 200

    @app.route("/open-petition", methods = ["POST"])
    @login_required
    @priv_required
    def open_petition():
        payload = request.json
        return services.manager_service.open_petition_service(payload["petition_id"])

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

    @app.route("/set-pass-ratio", methods = ["POST"])
    @login_required
    @priv_required
    def set_pass_ratio():
        set_data = int(request.json['pass_ratio'])

        if set_data > 100:
            return "100 이상의 값은 입력하실 수 없습니다.", 400
        else:
            config.pass_ratio = set_data
            config.pass_line = services.manager_service.get_pass_line()

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