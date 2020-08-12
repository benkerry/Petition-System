from ..dao import DebateDao

class DebateService():
    def __init__(self, dao:DebateDao):
        self.dao = dao