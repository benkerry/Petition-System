from ..dao import UserDao

class UserService:
    def __init__(self, dao:UserDao):
        self.dao = dao