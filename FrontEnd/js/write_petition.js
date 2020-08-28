document.querySelector("#write_petition").addEventListener("click", () => {
    document.querySelector("#write_petition_modal").style.display = "block";
});

document.querySelector("#send_petition").addEventListener("click", performSendPetition);

function performSendPetition(){
    var title = document.getElementById("petition_title").value;
    var content = document.getElementById("petition_content").value;

    if(!title || !content){
        alert("빈칸을 모두 채워주세요.")
    }
    else if(title.length < 2){
        alert("제목이 너무 짧습니다.\n최소 길이는 두 글자입니다.");
    }
    else if(confirm("청원은 한 번 작성하면 삭제할 수 없으며, 문제 소지가 있는 게시물 작성 시 이용정지 등 제재를 받을 수 있습니다.\n\n정말 청원을 올리시겠습니까?")){
        let data = {
            "title":title,
            "content":content
        }
    
        let done = (rsp) => {
            document.querySelector("#write_petition_modal").style.display = "none";
            document.getElementById("petition_title").value = "";
            content = document.getElementById("petition_content").value = "";
            alert("작성 완료!");
            location.reload();
        }
    
        sendApiRequest("write-petition", data, done, true);
    }
}