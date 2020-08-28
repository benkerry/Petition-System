document.querySelector("#write_notice").addEventListener("click", () => {
    openManagerFunctionModal(document.querySelector("#write_notice_modal"));
});

document.querySelector("#send_notice").addEventListener("click", sendNotice);

function sendNotice(){
    var title = document.getElementById("notice_title").value;
    var content = document.getElementById("notice_content").value;

    if(title && content){
        let data = {
            "title":title,
            "content":content
        }
        let done = () => {
            alert("작성 성공!");
            document.getElementById("notice_title").value = "";
            document.getElementById("notice_content").value = "";
            document.getElementsByClassName("go_back")[0].click();
        }
        
        sendApiRequest("write-notice", data, done, true);
    }
    else{
        alert("빈칸을 모두 채워주세요.");
    }
}