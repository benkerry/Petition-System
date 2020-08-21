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
    else{
        let data = {
            "title":title,
            "content":content
        }

        let done = () => {
            document.querySelector("#write_petition_modal").style.display = "none";
            document.getElementById("petition_title").value = "";
            content = document.getElementById("petition_content").value = "";
            alert("작성 완료!");
            location.reload();
            // 여기에서 작성된 글 볼 수 있도록 처리
        }

        sendApiRequest("write-petition", data, done, true);
    }
}