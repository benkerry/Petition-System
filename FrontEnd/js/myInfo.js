document.querySelector("#myInfo_btn").addEventListener("click", () => {
    if(priv){
        document.getElementById("myInfo_email").placeholder = "현재 이메일: " + sessionStorage.getItem("email");
        document.getElementById("myInfo_nickname").placeholder = "현재 닉네임: " + sessionStorage.getItem("nickname");
        document.querySelector("#myInfo_modal").style.display = "block";
    }
    else{
        alert("로그인이 필요합니다.");
        document.querySelector("#login_modal").style.display = "block";
    }
});

document.querySelector("#info_input_chkbx").addEventListener("change", () => {
    var nickname = document.querySelector("#myInfo_nickname");
    var email = document.querySelector("#myInfo_email");

    if(document.getElementById("info_input_chkbx").checked){
        nickname.removeAttribute("disabled");
        email.removeAttribute("disabled");
    }
    else{
        nickname.setAttribute("disabled", "");
        email.setAttribute("disabled", "");

        nickname.value = "";
        email.value = "";
    }
});

document.querySelector("#change_info_btn").addEventListener("click", performChangeInfo);
document.querySelector("#change_pwd_btn").addEventListener("click", performChangePwd);
document.querySelector("#withdraw_btn").addEventListener("click", performWithdraw);

function performChangeInfo(){
    var email = document.getElementById("myInfo_email").value;
    var nickname = document.getElementById("myInfo_nickname").value;
    
    if(priv){
        if(!email){
            email = sessionStorage.getItem("email");
        }
        if(!nickname){
            nickname = sessionStorage.getItem("nickname");
        }

        var data2send = {
            "email":email,
            "nickname":nickname
        };

        var done = () => {
            sessionStorage.setItem("email", email);
            sessionStorage.setItem("nickname", nickname);
            alert("정보변경 성공!");
            location.reload();
        };

        sendApiRequest("change-my-info", data2send, done, true);
    }
    else{
        alert("잘못된 접근입니다.");
        location.reload();
    }
}

function performChangePwd(){
    var pwd = document.getElementById("myInfo_pwd").value;
    var pwd_chk = document.getElementById("myInfo_pwd_chk").value;
    var old_pwd = document.getElementById("myInfo_current_pwd").value;
    
    if(priv){
        if(pwd != pwd_chk){
            alert("비밀번호와 비밀번호 확인 란의 값이 다릅니다.");
        }
        else if(pwd.length < 8){
            alert("비밀번호가 너무 짧습니다. 비밀번호는 8자 이상이어야 합니다.");
        }
        else{
            var data2send = {
                "pwd":pwd,
                "pwd_chk":pwd_chk,
                "old_pwd":old_pwd
            };

            var done = () => {
                alert("비밀번호 변경 성공!");
                location.reload();
            };

            sendApiRequest("change-my-pwd", data2send, done, true);
        }
    }
    else{
        alert("잘못된 접근입니다.");
        location.reload();
    }
}

function performWithdraw(){
    var pwd = prompt("한번 탈퇴하면 14일간 재가입이 불가능 합니다.\n비밀번호를 입력하세요.");

    if(!pwd){
        alert("비밀번호를 입력하지 않았습니다.");
    }
    else{
        var done = () => {
            alert("탈퇴 성공!");
            performLogout();
        };

        sendApiRequest("withdraw", {"pwd":pwd}. done, true);
    }
}