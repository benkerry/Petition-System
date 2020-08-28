document.querySelector("#system_setting").addEventListener("click", () => {
    var done = (rsp) => {
        document.getElementById("user_count").value = rsp.user_count;
        document.getElementById("current_pass_ratio").value = rsp.pass_ratio;
        if(rsp.user_count < 30){
            document.getElementById("current_pass_support").value = "청원 동의 기능 사용 불가능";
        }
        else{
            document.getElementById("current_pass_support").value =  Math.floor(rsp.user_count * (rsp.pass_ratio / 100)) + "명";
        }
        document.getElementById("current_expire_left").value = rsp.expire_left + "일";
    };

    openManagerFunctionModal(document.querySelector("#system_setting_modal"));
    sendApiRequest("get-settings", {}, done, true);
});

document.querySelector("#pass_ratio_to_set").addEventListener("change", () => {
    var user_count = document.getElementById("user_count").value;
    var pass_ratio = document.getElementById("pass_ratio_to_set").value.replaceAll(" ", "");
    document.getElementById("pass_ratio_to_set").value = pass_ratio;

    document.getElementById("pass_support_when_setted").value = Math.floor(user_count * (pass_ratio / 100));
});

document.querySelector("#set_pass_ratio").addEventListener("click", performSetPassRatio);
document.querySelector("#set_expire_day").addEventListener("click", performSetExpireDay);

function performSetPassRatio(){
    var pass_ratio = document.getElementById("pass_ratio_to_set").value.replace(" ", "");
    document.getElementById("pass_ratio_to_set").value = pass_ratio

    if(!$.isNumeric(pass_ratio)){
        alert("숫자만 입력해주세요.");
    }
    else{
        sendApiRequest("set-pass-ratio", {"pass_ratio":pass_ratio}, () => {
            let user_count = document.getElementById("user_count").value;

            document.getElementById("current_pass_ratio").value = pass_ratio;
            if(user_count < 30){
                document.getElementById("current_pass_support").value = "청원 동의 기능 사용 불가능";
            }
            else{
                document.getElementById("current_pass_support").value =  Math.floor(user_count * (pass_ratio / 100)) + "명";
            }
            document.getElementById("pass_ratio_to_set").value = "";
            alert("변경 성공!");
        }, true);
    }
}

function performSetExpireDay(){
    var expire_left = document.getElementById("expire_left_to_set").value.replaceAll(" ", "");
    document.getElementById("expire_left_to_set").value = expire_left;

    if(!$.isNumeric(expire_left)){
        alert("숫자만 입력해주세요.");
    }
    else{
        var data2send = {
            "expire_left":expire_left
        };

        sendApiRequest("set-expire-left", data2send, () => {
            document.getElementById("expire_left_to_set").value = "";
            document.getElementById("current_expire_left").value = expire_left + "일";
        }, true);
    }
}