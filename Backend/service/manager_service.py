import random
from datetime import datetime
from flask import jsonify, send_file
from openpyxl import Workbook
from openpyxl.styles.borders import Border, Side

from endpoints import Config
from dao import UserDao, PetitionDao, ManagerDao

class ManagerService:
    def __init__(self, user_dao:UserDao, petition_dao:PetitionDao, manager_dao:ManagerDao, config:Config):
        self.user_dao = user_dao
        self.petition_dao = petition_dao
        self.manager_dao = manager_dao
        self.config = config

    def get_user_count(self):
        return self.manager_dao.get_user_count()

    def get_petition_status(self, petition_id:int):
        title, status, supports = self.petition_dao.get_petition_status(petition_id)

        if status != None:
            return jsonify({
                "title":title,
                "status":status,
                "supports":supports,
                "msg":"success!"
            })
        else:
            return "청원번호 조회에 실패했습니다.", 400

    def get_report_service(self):
        return jsonify({ "reports":self.manager_dao.get_reports() })

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

    def get_authcode_count(self):
        data = self.manager_dao.get_authcode_count()

        if "manager" not in data.keys():
            data["manager"] = 0
        if "general" not in data.keys():
            data["general"] = 0

        return jsonify(data)

    def generate_authcodes_service(self, grade = 0, count = 0, priv = 0, life = 0):
        charset = "AB1CD3E2FG4HI5JK6LMN7OP8QR9STU0WXYZ"
        old_authcodes = self.user_dao.get_all_authcodes()
        authcodes = []

        if grade > 0:
            count *= 30

        while len(authcodes) < count:
            authcode = ""
            for i in range(6):
                authcode += random.choice(charset)

            if authcode not in authcodes and authcode not in old_authcodes:
                authcodes.append(authcode)

        self.manager_dao.insert_authcode(grade, tuple(authcodes), priv, life)

        wb = Workbook()
        ws = wb.active
        border = Border(
            left = Side(style="thin"),
            right = Side(style="thin"),
            top = Side(style="thin"),
            bottom = Side(style="thin")
        )

        for i in len(authcodes):
            rowidx = str((i % 30) + 3)

            if rowidx == "3":
                ws["B2"] = "학년"
                ws["C2"] = "인증번호"
                ws["D2"] = "권한"

                ws["B2"].border = border
                ws["C2"].border = border
                ws["D2"].border = border
                if not i < 30:
                    ws = wb.create_sheet()

            ws["B" + rowidx] = grade
            ws["C" + rowidx] = authcodes[i]
            ws["D" + rowidx] = "일반" if priv == 0 else "관리자"

            ws["B" + rowidx].border = border
            ws["C" + rowidx].border = border
            ws["D" + rowidx].border = border

        timestamp = datetime.now().timestamp()
        wb.save(f"{timestamp}.xlsx")

        return send_file(
            filename_or_fp = f"{timestamp}.xlsx",
            attachment_filename = "인증번호.xlsx",
            as_attachment= True
        )

    def open_petition_service(self, petition_id:int):
        if self.petition_dao.reopen_petition(petition_id, self.config.expire_left) is not None:
            return "성공!", 200
        else:
            return "잘못된 접근입니다.", 403

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