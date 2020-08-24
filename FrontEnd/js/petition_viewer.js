document.querySelector("#support_petition_btn").addEventListener("click", performSupportPetition);

function showPetition(petition_id){
    var data2Send = {
        "petition_id":petition_id
    }

    var done = (rsp) => {
        document.getElementById("petition_viewer_title").innerHTML = "[청원번호-" + petition_id + "] " + rsp.title;
        document.getElementById("petition_viewer_created_at").innerHTML = "작성시: " + rsp.created_at.replace("T", " / ");
        document.getElementById("petition_viewer_expire_at").innerHTML = "만료일: " + rsp.expire_at.split("T")[0];
        document.getElementById("petition_viewer_supports").innerHTML = "동의 현황: " + rsp.supports
        document.getElementById("petition_viewer_content").innerHTML = rsp.contents;
        document.getElementById("support_petition_btn").setAttribute("value", petition_id);
        document.getElementById("petition_viewer_modal").style.display = "block";
    }

    sendApiRequest("get-petition", data2Send, done, false);
}

function performSupportPetition(){
    var petition_id = document.getElementById("support_petition_btn").getAttribute("value");

    var data2Send = {
        "petition_id":petition_id,
    }

    var done = (rsp) => {
        alert(rsp);
        location.reload();
    }

    sendApiRequest("support-petition", data2Send, done, true);
}