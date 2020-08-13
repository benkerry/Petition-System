var isLoggedIn = true;
var isManager = true; // 임시

if(isLoggedIn){
    document.querySelector(".profile_infos_non_login").style.display = "none";
    document.querySelector(".profile_infos_login").style.display = "block";
}

if(isManager){
    document.querySelector(".profile").className = "profile_manager";
    document.querySelector("#logout_btn").id = "logout_btn_manager";
    document.querySelector("#profile_br_manager").style.display = "block";
    document.querySelector("#managerMenu_btn").style.display = "block";
}

document.querySelector("#login").addEventListener("click", () => {
    document.querySelector("#login_modal").style.display = "block";
});

document.querySelector("#register_btn").addEventListener("click", () => {
    document.querySelector("#login_modal").style.display = "none";
    document.querySelector("#register_modal").style.display = "block";
});

document.querySelector("#myInfo_btn").addEventListener("click", () => {
    if(isLoggedIn){
        document.querySelector("#myInfo_modal").style.display = "block";
    }
    else{
        alert("로그인이 필요합니다.");
        document.querySelector("#login_modal").style.display = "block";
    }
});

document.querySelector("#managerMenu_btn").addEventListener("click", () => {
    if(isManager){
        // 모달 만들기
    }
    else{
        alert("권한이 없습니다.");
    }
});

document.querySelector("#logout_btn").addEventListener("click", performLogout);

document.querySelector("html").addEventListener("click", closeModal);

function clearInputs(parentNode){
    var inputElements = parentNode.querySelectorAll("input");

    for(let i = 0; i < inputElements.length; i++){
        inputElements[i].value = "";
    }
}

function closeModal(e){
    if(e.target.className === "login_modal_layer"){
        var form = document.querySelector(".login_form");
        document.querySelector("#login_modal").style.display = "none";
        clearInputs(form);
    }
    else if(e.target.className === "register_modal_layer"){
        var form = document.querySelector(".register_form");
        document.querySelector("#register_modal").style.display = "none";
        clearInputs(form);
    }
    else if(e.target.className === "myInfo_modal_layer"){
        document.querySelector("#myInfo_modal").style.display = "none";
    }
}

function performLogout(){

}