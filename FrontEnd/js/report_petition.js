document.querySelector("#report_petition_btn").addEventListener("click", () => {
    var petition_id = document.getElementById("report_petition_btn").getAttribute("value");
    document.getElementById("petition_viewer_modal").style.display = "none";
    document.getElementById("report_petition_modal").style.display = "block";

    document.getElementById("reporting_petition_title").innerHTML = document.getElementById("petition_viewer_title").innerHTML + " 신고하기";
});

document.querySelector("#send_report_btn").addEventListener("click", sendReport);

function sendReport(){
    var petition_id = document.getElementById("report_petition_btn").getAttribute("value");
    var description = document.getElementById("report_petition_description").value;

    if(!description){
        alert("신고 세부내용을 입력해주세요.");
    }
    else if(confirm("해당 청원을 정말 신고하시겠습니까?")){
        var data = {
            "petition_id":petition_id,
            "description":description
        }

        var done = () => {
            alert("신고가 접수되었습니다.");
            document.getElementById("report_petition_description").value = "";
            location.reload();
        }

        sendApiRequest("report-petition", data, done, true);
    }
}