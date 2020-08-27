document.querySelector("#view_report").addEventListener("click", () => {
    openManagerFunctionModal(document.querySelector("#view_report_modal"));
    showReports();
});

function showReports(){
    var performShowReports = (rsp) => {
        var table = document.getElementById("report_list_table_tbody");
        table.innerHTML = "";
        
        for(let i = 0; i < rsp.reports.length; i++){
            let pid = rsp.reports[i]["pid"];
            let authorId = rsp.reports[i]["author_id"]
            let description = rsp.reports[i]["description"];
            let tr = document.createElement("tr");
                
            if(description.length > 20){
                description = description.substring(0, 20) + "......";
            }

            tr = appendTableData(tr, pid, "class", "report_list_td_pid");
            tr = appendTableData(tr, description);
            tr.addEventListener("click", () => {
                var confirmStr = "신고 누적 수: " + rsp.reports[i]["reports"] +
                                "\n신고 내용:\n" + 
                                rsp.reports[i]["description"] +
                                "\n\n 게시물을 비활성화 처리하시겠습니까?";

                if(confirm(confirmStr)){
                    deactivatePetition(pid);
                    if(confirm("해당 유저에 대한 회원 삭제 처리도 진행하시겠습니까?")){
                        deleteUser(authorId);
                    }
                }
                showReports();
            });
            table.appendChild(tr);
        }
    }
    sendApiRequest("get-reports", {}, performShowReports, true);
}

function deactivatePetition(pid){
    sendApiRequest("deactivate-petition", { "pid":pid }, () => {
        alert("성공!");
    }, true);
}

function deleteUser(authorId){
    sendApiRequest("delete-user", { "uid":authorId }, () => {
        alert("성공!");
    }, true);
}