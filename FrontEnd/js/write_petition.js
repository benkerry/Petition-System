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
    else if(confirm("청원을 한 번 작성하면 삭제할 수 없으며, 문제 소지가 있는 게시물 작성 시 이용정지 등 제재를 받을 수 있습니다. 시스템적으로 관리자도 회원님의 정보를 알 수 없도록 철저히 익명보장을 하고 있으나, 법적 분쟁 발생시에는 개발자가 회원님의 정보를 관련 기관에 제공할 수 있습니다. 회원탈퇴를 진행하더라도 회원님의 정보는 14일 후에 파기된다는 점, 명심하십시오.\n\n정말 청원을 올리시겠습니까?")){
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