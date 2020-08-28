document.querySelector("#generate_authcode").addEventListener("click", () => {
    openManagerFunctionModal(document.querySelector("#generate_authcode_modal"));
    setCurrentAuthcodeCount();
    authcodeGenerateRdosSetting();
});

document.querySelector("#truncate_authcode").addEventListener("click", performTruncateAuthcodes);

var rdos = document.getElementsByName("authcode_priv_rdo");

for(let i = 0; i < rdos.length; i++){
    rdos[i].addEventListener("change", () => {
        authcodeGenerateRdosSetting();
    });
}

document.querySelector("#generate").addEventListener("click", performGenerateAuthcode);

function setCurrentAuthcodeCount(){
    var done = (rsp) => {
        document.getElementById("current_general_authcodes_count").value = rsp.general;
        document.getElementById("current_manager_authcodes_count").value = rsp.manager;
    }

    sendApiRequest("get-authcode-count", {}, done, true);
}

function authcodeGenerateRdosSetting(){
    var general = document.getElementById("general_authcode");
    var manager = document.getElementById("manager_authcode");

    if(general.checked){
        document.getElementById("authcode_grade").style.display = "block";
        document.getElementById("authcode_count").setAttribute("placeholder", "인증번호 수량 입력(단위: 반)");
        document.getElementById("generate_authcode_form").style.height = "600px";
    }
    else if(manager.checked){
        document.getElementById("authcode_grade").style.display = "none";
        document.getElementById("authcode_count").setAttribute("placeholder", "인증번호 수량 입력(단위: 개)");
        document.getElementById("generate_authcode_form").style.height = "550px";
    }
}

function performTruncateAuthcodes(){
    sendApiRequest("truncate-authcodes", {}, () => {
        alert("성공!");
        setCurrentAuthcodeCount();
    }, true);
}

function performGenerateAuthcode(){
    var count = document.getElementById("authcode_count").value;
    var life = document.getElementById("authcode_life").value;

    if($.isNumeric(count) && $.isNumeric(life) && count > 0 && life > 0 && count % 1 == 0 && life % 1 == 0 && count && life){
        let general = document.getElementById("general_authcode");
        let manager = document.getElementById("manager_authcode");
        let data = null;
        let done = (rsp) => {
            var file = atob(rsp.file);
            var url = null;
            var length = file.length;
            var arr = new Uint8Array(length);
            var a = document.createElement("a");

            alert("발급 성공!");
            setCurrentAuthcodeCount();

            document.getElementById("authcode_grade").value = "";
            document.getElementById("authcode_count").value = "";
            document.getElementById("authcode_life").value = "";

            a.style.display = "none";
            document.body.appendChild(a);

            while(length--){
                arr[length] = file.charCodeAt(length);
            }

            file = new Blob([arr], {
                type:"octet/stream",
            });

            url = URL.createObjectURL(file);
            a.href = url;
            a.download = "authcode.xlsx";
            a.click();
            URL.revokeObjectURL(url);
        }

        if(general.checked){
            let grade = document.getElementById("authcode_grade").value;

            if(!$.isNumeric(grade) || grade < 1 || grade > 3){
                alert("학년 값에는 1~3 사이 숫자만 입력 가능합니다.");
                return;
            }

            data = {
                "grade":grade,
                "count":count,
                "priv":1,
                "life":life
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
        sendApiRequest("generate-authcodes", data, done, true);
    }
    else{
        alert("양의 정수만 입력 가능합니다.");
    }
}