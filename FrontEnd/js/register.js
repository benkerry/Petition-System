document.querySelector("#register_btn").addEventListener("click", () => {
    document.querySelector("#login_modal").style.display = "none";
    document.querySelector("#register_modal").style.display = "block";
});

document.querySelector("#register_modal").addEventListener("keydown", (event) => {
    if(event.keyCode == 13){
        performRegister();
    }
});

document.querySelector("#dont_get_validate_mail").addEventListener("click", () => {
    document.querySelector("#register_modal").style.display = "none";
    document.querySelector("#validate_mail_resend_modal").style.display = "block";
});

document.querySelector("#validate_is_fucked").addEventListener("click", () => {
    if(document.getElementById("validate_is_fucked").checked){
        document.getElementById("resend_pwd").style.display = "block";
        document.getElementById("resend_new_email").style.display = "block";
    }
    else{
        document.getElementById("resend_pwd").style.display = "none";
        document.getElementById("resend_new_email").style.display = "none";
    }
});

document.querySelector("#request_register_btn").addEventListener("click", performRegister);
document.querySelector("#resend_validate_mail").addEventListener("click", performResend);

function performRegister(){
    var email = document.getElementById("register_email").value;
    var pwd = document.getElementById("register_pwd").value;
    var pwd_chk = document.getElementById("register_pwd_chk").value;
    var nickname = document.getElementById("register_nickname").value;
    var stdid = document.getElementById("register_stdid").value;
    var authcode = document.getElementById("register_authcode").value;

    if(email.indexOf("@naver.com") == -1 && email.indexOf("@daum.net") == -1 && email.indexOf("@hanmail.net") == -1 
    && email.indexOf("@korea.kr") == -1 && email.indexOf("@gmail.com") == -1 && email.indexOf("@kakao.com") == -1){
        alert("이메일 형식이 잘못되었거나, 지원하지 않는 이메일입니다.\n네이버, 다음, 카카오, 구글, 공직메일만 사용 가능합니다.");
    }
    else if(pwd !== pwd_chk){
        alert("비밀번호와 비밀번호 확인란의 값이 다릅니다.")
    }
    else if(pwd.length < 8){
        alert("비밀번호가 너무 짧습니다. 8자 이상이어야 합니다.")
    }
    else if(stdid > 3999){
        alert("학번 입력값을 확인해 주세요.");
    }
    else if(authcode.length != 6){
        alert("인증번호를 확인해 주세요.\n인증번호는 6자리 문자입니다.");
    }
    else{
        var data2send = {
            "stdid": stdid,
            "authcode": authcode,
            "email": email,
            "pwd": pwd,
            "pwd_chk": pwd_chk,
            "nickname": nickname
        };

        var done = () => {
            console.log(msg);
            alert("가입 성공!\n가입 시 작성한 이메일로 인증 메일을 발송하였습니다.\n서비스는 메일 인증 후 사용 가능합니다.\n인증을 완료해주세요.\n");

            document.getElementById("validate_mail_resend_modal").style.display = "none";
            document.getElementById("login_modal").style.display = "block";
        };

        sendApiRequest("register", data2send, done, false);
    }
}

function performResend(){
    var email = document.querySelector("#resend_email").value;
    var isValidateFucked = document.getElementById("validate_is_fucked").checked

    if(email){
        if(!isValidateFucked){
            var data2send = {
                "email":email,
                "isValidateFucked":0
            };
    
            var done = (msg) => {
                console.log(msg);
                alert("메일함과 스팸 메일함을 다시 확인해보세요!");
            };

            sendApiRequest("validate-mail-resend", data2send, done, false);
        }
        else{
            var newEmail = document.getElementById("resend_new_email").value;
            var pwd = document.getElementById("resend_pwd").value
            
            if(!newEmail){
                alert("빈칸을 채워주세요!(볼빨사 아님 ㅎ)");
            }
            else if(newEmail.indexOf("@naver.com") == -1 && newEmail.indexOf("@daum.net") == -1 && newEmail.indexOf("@hanmail.net") == -1 
                && newEmail.indexOf("@korea.kr") == -1 && newEmail.indexOf("@gmail.com") == -1 && newEmail.indexOf("@kakao.com") == -1){
                alert("이메일 형식이 잘못되었거나, 지원하지 않는 이메일입니다.\n네이버, 다음, 카카오, 구글, 공직메일만 사용 가능합니다.");
            }
            else{
                var data2send = {
                    "email":email,
                    "new_email":new_email,
                    "pwd":pwd,
                    "isValidateFucked":1
                };

                var done = (msg) => {
                    console.log(msg);
                    alert("새로 입력한 메일주소로 이메일이 왔는지 확인해보세요!");
                };

                sendApiRequest("validate-mail-resend", data2send, done, false);
            }  
        }
    }
    else{
        alert("빈칸을 채워주세요!(볼빨사 아님 ㅎ)");
    }
}