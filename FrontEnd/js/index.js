var isLoggedIn = true;
var isManager = true; // 임시

if(isLoggedIn){
    document.querySelector(".profile_non_login").className = "profile_login";
    document.querySelector(".profile_infos_non_login").style.display = "none";
    document.querySelector(".profile_infos_login").style.display = "block";
}

if(isLoggedIn && isManager){
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

document.querySelector("html").addEventListener("click", closeModal);

document.querySelector("#login").addEventListener("click", () => {
    recentModal = document.querySelector("#login_modal");
    recentModal.style.display = "block";
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
        recentModal = document.querySelector("#manager_menu_modal");
        recentModal.style.display = "block";
    }
    else{
        alert("권한이 없습니다.");
    }
});

document.querySelector("#system_setting").addEventListener("click", () => {
    if(isManager){
        document.querySelector("#manager_menu_modal").style.display = "none";
        document.querySelector("#system_setting_modal").style.display = "block";
    }
    else{
        alert("권한이 없습니다.");
    }
});

document.querySelector("#change_petition_status").addEventListener("click", () => {
    if(isManager){
        document.querySelector("#manager_menu_modal").style.display = "none";
        document.querySelector("#change_petition_status_modal").style.display = "block";
    }
    else{
        alert("권한이 없습니다.");
    }
});

document.querySelector("#add_expire_day").addEventListener("click", () => {
    if(isManager){
        document.querySelector("#manager_menu_modal").style.display = "none";
        document.querySelector("#add_expire_day_modal").style.display = "block";
    }
    else{
        alert("권한이 없습니다.");
    }
});

function clearInputs(parentNode){
    var inputElements = parentNode.querySelectorAll("input");

    for(let i = 0; i < inputElements.length; i++){
        inputElements[i].value = "";
    }
}

function closeModal(e){
    if(e.target.className === "modal_layer"){
        var modals = document.querySelectorAll(".modal");
        var forms = document.querySelectorAll(".form");

        for(let i = 0; i < modals.length; i++){
            modals[i].style.display = "none";
        }

        for(let i = 0; i < forms.length; i++){
            clearInputs(forms[i]);
        }
    }
}

function performLogout(){

}