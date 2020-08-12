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

    @app.route("/change-my-info", methods = ["POST"])
    @login_required
    def change_my_info():
        pass

    @app.route("/change-my-pwd", methods = ["POST"])
    @login_required
    def change_my_pwd():
        pass

    @app.route("/change-priv", methods = ["POST"])
    @login_required
    def change_priv():
        pass

    # Petition Services
    @app.route("/get-petition/<int:count>", methods = ["POST"])
    def get_petition(count):
        pass

    @app.route("/write-petition", methods = ["POST"])
    @login_required
    def write_petition():
        pass

    @app.route("/support-petition", methods = ["POST"])
    @login_required
    def support_petition():
        pass

    # Debate Services
    @app.route("/write-debate", methods = ["POST"])
    @login_required
    def write_debate():
        pass