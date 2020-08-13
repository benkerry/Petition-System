from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # JWT 검증 절차 수행
        return f(*args, *kwargs)

    return decorated_function

def create_endpoints(app, services):
    # User Services
    @app.route("/register", methods = ["POST"])
    def register():
        pass

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

    @app.route("/withdraw", methodes = ["POST"])
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
    def delete_user():
        pass

    @app.route("/change-priv", methods = ["POST"])
    @login_required
    def change_priv():
        pass

    @app.route("/get-all-nicknames", methods = ["POST"])
    @login_required
    def get_all_nicknames():
        pass

    @app.route("/generate-authcodes", methods = ["POST"])
    @login_required
    def generate_authcodes():
        pass

    @app.route("/close-petition", methods = ["POST"])
    @login_required
    def close_petition():
        pass

    @app.route("/open-petition", methods = ["POST"])
    @login_required
    def open_petition():
        pass

    @app.route("/add-day", methods = ["POST"])
    @login_required
    def add_day():
        pass

    @app.route("/set-support-ratio", methods = ["POST"])
    @login_required
    def set_support_ratio():
        pass

    @app.route("/get-add-day-request", methods = ["POST"])
    @login_required
    def get_add_day_request():
        pass

    ##### 답변 작성
    ##### 신고 및 처리 기능
    ##### 임의 답변 및 처리 기능
    ##### 날짜, 동의인 비율 설정
    ##### 이메일 인증 기능(gmail, naver, korea, daum, hanmail 제한) -> 이메일 인증 디비 만들자