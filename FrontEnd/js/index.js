document.querySelector("#login").addEventListener("click", () => {
    document.querySelector("#login_modal").style.display = "block";
});

document.querySelector("html").addEventListener("click", (e)=>{
    if(e.target.className === "login_modal_layer"){
        document.querySelector("#login_modal").style.display = "none";
    }
});