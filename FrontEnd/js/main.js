var done = (rsp) => {
    var table = document.querySelector("#all_petitions_list_table_tbody");
    var petitions = Array();

    for(let i = 0; i < rsp.petitions.length; i++){
        let petition = rsp.petitions[i];
        let created_timestamp = (new Date(petition.created_at)).getTime();

        petitions.push({
            "id":petition.id,
            "title":petition.title,
            "created_at":petition.created_at,
            "supports":petition.supports,
            "created_timestamp":created_timestamp,
        });
    }

    petitions.sort((a, b) => {
        if(a["created_timestamp"] < b["created_timestamp"]){
            return 1;
        }
        else if (a["created_timestamp"] < b["created_timestamp"]){
            return -1;
        }
        else{
            return 0;
        }
    });

    for(let i = 0; i < 10; i++){
        if(i == petitions.length){
            break;
        }
        let trNode = document.createElement("tr");
        trNode = appendTableData(trNode, petitions[i]["id"]);
        trNode = appendTableData(trNode, petitions[i]["title"]);
        trNode = appendTableData(trNode, petitions[i]["supports"]);
        trNode = appendTableData(trNode, petitions[i]["created_at"].replace("T", " / "));

        trNode.setAttribute("id", "petition_id:" + petitions[i]["id"]);
        trNode.addEventListener("click", clickPetition);
        table.appendChild(trNode);
    }
}

sendApiRequest("get-petition-metadatas", {}, done, false);

function appendTableData(trNode, str){
    let tdElement = document.createElement("td");
    tdElement.appendChild(document.createTextNode(str));
    trNode.appendChild(tdElement);
    return trNode;
}

function clickPetition(){
    var petition_id = Number(this.id.split(":")[1]);
    showPetition(petition_id);
}

// 청원 관련 라디오버튼 처리