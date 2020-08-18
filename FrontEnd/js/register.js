document.querySelector("#request_register_btn").addEventListener("click", performRegister);

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
        $.ajax({
            url: "http://localhost:5500/register",
            type: "POST",
            data: JSON.stringify({
                "stdid": stdid,
                "authcode": authcode,
                "email": email,
                "pwd": pwd,
                "pwd_chk": pwd_chk,
                "nickname": nickname
            })
        }).done((msg) => {
            console.log(msg);
        }).fail((msg) =>{
            alert("[" + msg.status + "] 서버와의 통신에 문제가 생겼습니다!\n다시 시도해보시고, 문제가 지속되면 오류 코드를 첨부하여\ndeveloperkerry@naver.com으로 메일 바랍니다.");
        });
    }
}