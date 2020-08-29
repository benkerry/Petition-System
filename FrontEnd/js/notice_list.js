document.querySelector("#toggle_main_content").addEventListener("click", () => {
    var toggleBtn = document.getElementById("toggle_main_content");
    var val = toggleBtn.getAttribute("value");

    if(val === "notice"){
        document.getElementById("petitions").style.display = "none";
        document.getElementById("notices").style.display = "block";
        toggleBtn.innerHTML = "청원 리스트 보기";
        toggleBtn.setAttribute("value", "petition");

        sendApiRequest("get-notice-metadata", {}, setNoticeList, false);
    }
    else if(val === "petition"){
        document.getElementById("petitions").style.display = "block";
        document.getElementById("notices").style.display = "none";
        toggleBtn.innerHTML = "공지사항";
        toggleBtn.setAttribute("value", "notice");
    }
});

function setNoticeList(rsp){
    var table = document.getElementById("notice_list_table_tbody");
    table.innerHTML = "";

    for(let i = 0; i < rsp.notices.length; i++){
        let trNode = document.createElement("tr");
        let id = rsp.notices[i]["id"];
        let title = rsp.notices[i]["title"];
        let createdAt = rsp.notices[i]["created_at"];

        trNode = appendTableData(trNode, id);
        trNode = appendTableData(trNode, title);
        trNode = appendTableData(trNode, createdAt.replace("T", " "));
        trNode.setAttribute("value", id);
        trNode.addEventListener("click", showNotice);
        table.appendChild(trNode);
    }
}

function showNotice(){
    var nid = this.getAttribute("value");
    var done = (rsp) => {
        var titlePlace = document.getElementById("notice_viewer_title");
        var createdAtPlace = document.getElementById("notice_viewer_created_at");
        var contentPlace = document.getElementById("notice_viewer_content");

        titlePlace.innerHTML = rsp.title;
        createdAtPlace.innerHTML = "작성시간: " + rsp.created_at.replace("T", " ");
        contentPlace.innerHTML = rsp.content;

        document.getElementById("notice_viewer_modal").style.display = "block";
    }

    sendApiRequest("get-notice", { "nid":nid }, done, false);
}