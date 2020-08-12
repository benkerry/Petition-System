class PetitionDao():
    # 여기서는 petition 테이블만 다룬다.
    def __init__(self, db):
        self.db = db

    def insert_petition(self, author_id:int, title:str, contents:str):
        # 
        pass
        