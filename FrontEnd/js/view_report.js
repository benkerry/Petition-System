document.querySelector("#view_report").addEventListener("click", () => {
    openManagerFunctionModal(document.querySelector("#view_report_modal"));
    showReports();
});

function showReports(){
    var performShowReports = (rsp) => {
        var table = document.getElementById("report_list_table_tbody");
        table.innerHTML = "";

        for(let i = 0; i < rsp.reports.length; i++){
            if(rsp.reports[i]["reports"] >= 10){
                let pid = rsp.reports[i]["pid"];
                let description = rsp.reports[i]["description"];
                let tr = document.createElement("tr");
                
                if(description.length > 20){
                    description = description.substring(0, 20) + "......";
                }

                tr = appendTableData(tr, pid, "class", "report_list_td_pid");
                tr = appendTableData(tr, description);
                tr.setAttribute("id", "petition_id:" + pid);
                tr.addEventListener("click", () => {
                    var confirmStr = "신고 누적 수: " + rsp.reports[i]["reports"] +
                                    "\n신고 내용:\n" + 
                                    rsp.reports[i]["description"] +
                                    "\n\n 처리하시겠습니까?";

                    if(confirm(confirmStr)){
                        // 비워둠
                    }
                    else{
                        // 비워둠
                    }
                });
                table.appendChild(tr);
            }
        }
    }

    sendApiRequest("get-reports", {}, performShowReports, true);
}