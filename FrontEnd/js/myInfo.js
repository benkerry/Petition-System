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

function performChangeInfo(){

}

function performChangePwd(){
    
}