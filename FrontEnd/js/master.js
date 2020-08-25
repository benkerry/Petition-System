var priv = sessionStorage.getItem("priv");

if(priv == null){
    priv = 0;
}

if(priv > 0){
    document.getElementById("profile_img").setAttribute("src", "resources/login_profile.png")
    document.getElementById("name").innerHTML = sessionStorage.getItem("nickname");
    document.getElementById("write_petition").style.display = "block";
}

if(priv){
    document.querySelector(".profile_non_login").className = "profile_login";
    document.querySelector(".profile_infos_non_login").style.display = "none";
    document.querySelector(".profile_infos_login").style.display = "block";
}

if(priv > 1){
    document.querySelector(".profile_login").className = "profile_manager";
    document.querySelector(".profile_manager").className = "profile_manager";
    document.querySelector("#logout_btn").id = "logout_btn_manager";
    document.querySelector("#profile_br_manager").style.display = "block";
    document.querySelector("#managerMenu_btn").style.display = "block";
    document.querySelector("#logout_btn_manager").addEventListener("click", performLogout);
}
else{
    document.querySelector("#logout_btn").addEventListener("click", performLogout);
}

var goBackBtns = document.querySelectorAll(".go_back");
var recentModal = null;

for(let i = 0; i < goBackBtns.length; i++){
    goBackBtns[i].addEventListener("click", () => {
        var managerModal = document.querySelectorAll(".manager_modal");
        
        for(let i = 0; i < managerModal.length; i++){
            managerModal[i].style.display = "none";
        }
        recentModal.style.display = "block";
    });
}

var modalLayers = document.querySelectorAll(".modal_layer");

for(let i = 0; i < modalLayers.length; i++){
    modalLayers[i].addEventListener("click", closeModal);
}

document.querySelector("#managerMenu_btn").addEventListener("click", () => {
    if(priv > 1){
        recentModal = document.querySelector("#manager_menu_modal");
        recentModal.style.display = "block";
    }
    else{
        alert("권한이 없습니다.");
    }
});

document.querySelector("#view_report").addEventListener("click", () => {
    openManagerFunctionModal(document.querySelector("#view_report_modal"));
});

// add_expire_day_req_modal은 마지막에 만들자

function clearInputs(parentNode){
    var inputElements = parentNode.querySelectorAll("input");

    for(let i = 0; i < inputElements.length; i++){
        inputElements[i].value = "";
    }
}

function closeModal(){
    var modals = document.querySelectorAll(".modal");
    var forms = document.querySelectorAll(".form");

    for(let i = 0; i < modals.length; i++){
        modals[i].style.display = "none";
    }

    for(let i = 0; i < forms.length; i++){
        clearInputs(forms[i]);
    }
}

function openManagerFunctionModal(modal){
    if(priv > 1){
        document.querySelector("#manager_menu_modal").style.display = "none";
        modal.style.display = "block";
    }
    else{
        alert("권한이 없습니다.");
    }
}

function commFail(msg){
    if(msg.status != 0){
        alert("[오류] " + msg.responseText);
    }
    else{
        alert("서버와의 통신에 문제가 생겼습니다! 잠시 후 다시 시도해보시고,\n문제가 지속되면 developerkerry@naver.com으로 메일 바랍니다.");   
    }
}

function performLogout(){
    sessionStorage.clear();
    location.reload();
}

function sendApiRequest(endpoint, data2send, done, isLoginRequirAction){
    if(isLoginRequirAction){
        $.ajax({
            url: "http://localhost:5000/" + endpoint,
            type: "POST",
            contentType: "application/json",
            beforeSend: (xhr) => { xhr.setRequestHeader("token", sessionStorage.getItem("token")) },
            data: JSON.stringify(data2send)
        }).done(done)
        .fail((msg) =>{
            commFail(msg);
        });
    }
    else{
        $.ajax({
            url: "http://localhost:5000/" + endpoint,
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(data2send)
        }).done(done)
        .fail((msg) =>{
            commFail(msg);
        });
    }
}