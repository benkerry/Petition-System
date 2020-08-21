function showPetition(petition_id){
    var petitionViewer = document.getElementById("petition_viewer_modal");
    var data2Send = {
        "petition_id":petition_id
    }
    var done = (rsp) => {
        let expire_at = new Date((new Date(rsp.created_at)).getTime() + (1000 * 60 * 60 * 24 * rsp.expire_left))
        let fullYear = String(expire_at.getFullYear());
        let fullMonth = (String(expire_at.getMonth()).length == 1) ? "0" + String(expire_at.getMonth()) : String(expire_at.getMonth());
        let fullDate = (String(expire_at.getDate().length == 1) ? "0" + String(expire_at.getDate()) : String(expire_at.getDate()));

        document.getElementById("petition_viewer_nickname").innerHTML = rsp.author;
        document.getElementById("petition_viewer_created_at").innerHTML = rsp.created_at.replace("T", " / ");
        document.getElementById("petition_viewer_expire_at").innerHTML = // 포매팅해서 이 부분 작성 fullYear + "-"
    }

    sendApiRequest("get-petition", data2, done, false);
}