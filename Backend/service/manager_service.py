from ..dao import UserDao, PetitionDao, DebateDao, ManagerDao

class ManagerService:
    def __init__(self, user_dao:UserDao, petition_dao:PetitionDao, debate_dao:DebateDao, manager_dao:ManagerDao):
        self.user_dao = user_dao
        self.petition_dao = petition_dao
        self.debate_dao = debate_dao
        self.manager_dao = manager_dao

    def delete_user_service(self, uid_list:list):
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

    def close_petition_service(self, petition_id:int):
        # 청원을 직권으로 닫음.(expire_left는 유지)
        # 직권으로 닫힌 청원은 작성자와 관리자만 열람 가능
        # 실패시 None, 성공시 200 반환
        # user_dao에 있는 것 사용
        pass

    def open_petition_service(self, petition_id:int):
        # 닫힌 청원을 직권으로 엶.(expire_left는 유지)
        # 실패시 None, 성공시 200 반환
        # user_dao에 있는 것 사용
        pass

    def add_day_service(self, petition_id:int, add_day:int):
        # 청원 만료기한을 늘림
        # add_day에 음수가 들어올 시 처리 실패로 간주한다.
        # 실패시 None, 성공시 현재로부터 만료까지 남은 날짜 반환
        # petition_dao에 있는 것 사용
        pass

    def set_support_ratio_service(self, petition_id:int):
        # 청원 동의인 비율 설정을 변경
        # 실패시 None, 변경된 비율을 적용하여 산출된 동의인 수 임곗값 리턴
        pass

    def get_add_day_request_service(self, petition_id:int):
        # 청원 만료기한 연장 요청 상황 확인,
        # 실패시 None, 성공시 ( (req_id, comment), ... ) 반환
        pass