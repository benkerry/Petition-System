document.querySelector("#generate_authcode").addEventListener("click", () => {
    openManagerFunctionModal(document.querySelector("#generate_authcode_modal"));
    var general = document.getElementById("general_authcode");
    var manager = document.getElementById("manager_authcode");
    var done = (rsp) => {
        document.getElementById("current_general_authcodes_count").value = rsp.general;
        document.getElementById("current_manager_authcodes_count").value = rsp.manager;
    }

    sendApiRequest("get-authcode-count", {}, done, true);

    if(general.checked){
        document.getElementById("authcode_count").setAttribute("placeholder", "인증번호 수량 입력(단위: 반)");
    }
    else{
        document.getElementById("authcode_count").setAttribute("placeholder", "인증번호 수량 입력(단위: 개)");
    }
});

document.querySelector("#generate").addEventListener("click", performGenerateAuthcode);

function performGenerateAuthcode(){
    var count = document.getElementById("authcode_count").value;
    var life = document.getElementById("authcode_life").value;

    if($.isNumeric(count) && $.isNumeric(life)){
        let general = document.getElementById("general_authcode");
        let manager = document.getElementById("manager_authcode");
        let data = null;

        if(general.checked){
            data = {

            };
        }
        else if(manager.checked){
            data = {
                "grade":0,
                "count":count,
                "priv":2,
                "life":life
            };
        }
    }
    else{
        alert("숫자만 입력 가능합니다.");
    }
}