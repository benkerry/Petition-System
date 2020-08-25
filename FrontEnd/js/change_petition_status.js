document.querySelector("#change_petition_status").addEventListener("click", () => {
    openManagerFunctionModal(document.querySelector("#change_petition_status_modal"));
});

document.querySelector("#petition_id_for_get_status").addEventListener("keydown", getPetitionStatus);
document.querySelector("#change_status_btn").addEventListener("click", performPetitionStatusChange);

var lstPetitionTitle = null;

function getPetitionStatus(event){
    var btn = document.getElementById("change_status_btn");

    if(event.keyCode == 13){
        var petition_id = Number(document.getElementById("petition_id_for_get_status").value);
        var data = {
            "petition_id":petition_id
        };
        var done = (rsp) => {
            if(rsp.msg === "success!"){
                if(rsp.status == 0){
                    if(rsp.supports >= 5){
                        alert("동의 수가 다섯 개 이상인 청원은 직권으로도 닫을 수 없습니다!");
                        return;
                    }
                    else{
                        lstPetitionTitle = rsp.title;
                        btn.innerHTML = "관리자 직권 닫기";
                        btn.setAttribute("value", "close");
                        btn.style.display = "block";
                    }
                }
                else if(rsp.status == 1){
                    alert("통과된 청원은 조작할 수 없습니다.");
                    return;
                }
                else{
                    lstPetitionTitle = rsp.title;
                    btn.innerHTML = "관리자 직권 열기";
                    btn.setAttribute("value", "open");
                    btn.style.display = "block";
                }
                document.getElementById("set_petition_id").setAttribute("value", petition_id);
            }
        };

        if(!$.isNumeric(petition_id)){
            alert("숫자만 입력하세요.");
            return;
        }

        sendApiRequest("get-petition-status", data, done, true);
    }
    btn.style.display = "none";
}

function performPetitionStatusChange(){
    if(confirm("청원 [" + lstPetitionTitle + "]의 상태를 변경하시겠습니까?")){
        var petition_id = document.getElementById("set_petition_id").value;
        var btnValue = document.getElementById("change_status_btn").getAttribute("value");
        var data = {
            "petition_id":petition_id
        };
        var done = (rsp) => {
            alert(rsp);
            document.getElementById("petition_id_for_get_status").value = "";
            document.getElementById("change_status_btn").style.display = "none";
        };

        if(btnValue == "open"){
            sendApiRequest("open-petition", data, done, true);
        }
        else if(btnValue == "close"){
            sendApiRequest("close-petition", data, done, true);
        }
    }
}