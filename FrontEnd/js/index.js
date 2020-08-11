document.querySelector("#login").addEventListener("click", () => {
    document.querySelector("#login_modal").style.display = "block";
});

document.querySelector("html").addEventListener("click", (e) => {
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
});

document.querySelector("#login_btn").addEventListener("click", () => {

});

document.querySelector("#register_btn").addEventListener("click", () => {
    document.querySelector("#login_modal").style.display = "none";
    document.querySelector("#register_modal").style.display = "block";
});

function clearInputs(parentNode){
    var inputElements = parentNode.querySelectorAll("input");

    for(let i = 0; i < inputElements.length; i++){
        inputElements[i].value = "";
    }
}