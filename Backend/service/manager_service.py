from ..dao import ManagerDao

class ManagerService:
    def __init__(self, dao:ManagerDao):
        self.dao = dao

    def delete_user(self, uid_list:list):
        # 유저를 삭제.
        # 실패시 None, 성공시 Transaction 이후 전체 유저의 수 반환.
        pass

    def change_priv_service(self, uid:int, tgt_nickname:str):
        # 권한 변경 수행
        # 실패시 None, 성공시 200 반환
        pass

    def get_all_nicknames_service(self):
        # 모든 유저의 닉네임을 인출하여 리스트로 반환
        # 실패시 None
        pass

    def generate_authcodes_service(self, stdid_list):
        # stdid_list에 대응하는 인증번호 생성 및 이중 튜플 ( (stdid, authcode), ... )로 반환
        # 실패시 None
        pass

