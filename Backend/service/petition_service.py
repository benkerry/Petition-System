from ..dao import PetitionDao

class PetitionService:
    def __init__(self, dao:PetitionDao):
        self.dao = dao