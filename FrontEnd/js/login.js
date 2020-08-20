document.querySelector("#login_btn").addEventListener("click", performLogin);

function performLogin(){
    var email = document.getElementById("login_email").value;
    var pwd = document.getElementById("login_pwd").value;

    if(!email || !pwd){
        alert("아이디와 비밀번호를 모두 입력해 주세요.");
    }
    else{
        var data2send = {
            "email":email,
            "pwd":pwd
        };

        var done = (rsp) => {
            sessionStorage.setItem("email", rsp.email);
            sessionStorage.setItem("nickname", rsp.nickname);
            sessionStorage.setItem("priv", rsp.priv);
            sessionStorage.setItem("token", rsp.token);

            location.reload();
        };

        sendApiRequest("login", data2send, done, false);
    }
}