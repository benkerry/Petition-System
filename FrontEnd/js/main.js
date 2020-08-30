var allPetitions = null;
var petitionOrderRdos = document.getElementsByName("petition_order");

for(let i = 0; i < petitionOrderRdos.length; i++){
    petitionOrderRdos[i].addEventListener("change", () => {
        var newest = document.getElementById("newest");
        var oldest = document.getElementById("oldest");
        var newest_passed = document.getElementById("newest_passed");
        var supportest = document.getElementById("supportest");
        var expired = document.getElementById("expired");

        if(newest.checked){
            performNewestOrder();
        }
        else if(oldest.checked){
            performOldestOrder();
        }
        else if(newest_passed.checked){
            performNewestPassedOrder();
        }
        else if(supportest.checked){
            performSupportestOrder();
        }
        else if(expired.checked){
            performShowExpired();
        }
    });
}

sendApiRequest("get-petition-metadatas", { "petition_type":"newest" }, performNewestOrder, false);

document.querySelector("#petition_search_checkbox").addEventListener("change", performReady2Search);
document.querySelector("#search_token").addEventListener("keydown", searchPetition);
document.querySelector("#manual_and_privacy_policy").addEventListener("click", () => {
    document.getElementById("petitions").style.display = "none";
    document.getElementById("manual").style.display = "block";
    document.querySelector(".sidebar").style.height = "1500px";
});
document.querySelector("#privacy_policy_btn").addEventListener("click", () => {
    document.getElementById("privacy_policy_modal").style.display = "block";
    document.getElementById("register_next_btn").style.display = "none";
});
document.querySelector("#back_to_petition_list").addEventListener("click", () => {
    document.getElementById("petitions").style.display = "block";
    document.getElementById("manual").style.display = "none";
    document.querySelector(".sidebar").style.height = "1100px";
})

var petittionSearchByRdos = document.getElementsByName("petition_search_by");

for(let i = 0; i < petittionSearchByRdos.length; i++){
    petittionSearchByRdos[i].addEventListener("change", searchPetition);
}

function clickPetition(){
    var petition_id = Number(this.id.split(":")[1]);
    showPetition(petition_id);
}

function addPetitions2List(petitions, mode){
    var table = document.querySelector("#all_petitions_list_table_tbody");

    table.innerHTML = "";

    for(let i = 0; i < 10; i++){
        if(i == petitions.length){
            break;
        }

        if(mode === "direct" || (mode === "searching" && petitions[i]["display"] === "block")){
            let trNode = document.createElement("tr");
            trNode = appendTableData(trNode, petitions[i]["id"]);
            trNode = appendTableData(trNode, petitions[i]["title"]);
            trNode = appendTableData(trNode, petitions[i]["supports"]);
            trNode = appendTableData(trNode, petitions[i]["created_at"].replace("T", " / "));

            trNode.setAttribute("id", "petition_id:" + petitions[i]["id"]);
            trNode.addEventListener("click", clickPetition);
            table.appendChild(trNode);
        }
        else{
            continue;
        }
    }
}

function addPetitions2ListForDirect(rsp){
    addPetitions2List(rsp.petitions, "direct");
}

function performNewestOrder(rsp){
    sendApiRequest("get-petition-metadatas", { "petition_type":"newest" }, addPetitions2ListForDirect, false);
}

function performOldestOrder(){
    sendApiRequest("get-petition-metadatas", { "petition_type":"oldest" }, addPetitions2ListForDirect, false);
}

function performNewestPassedOrder(){
    sendApiRequest("get-petition-metadatas", { "petition_type":"newest_passed" }, addPetitions2ListForDirect, false);
}

function performSupportestOrder(){
    sendApiRequest("get-petition-metadatas", { "petition_type":"supportest" }, addPetitions2ListForDirect, false);
}

function performShowAllPetitions(){
    sendApiRequest("get-petition-metadatas", { "petition_type":"all_for_search" }, (rsp) => { addPetitions2ListForDirect(rsp); allPetitions = rsp.petitions; }, false);
}

function performShowExpired(){
    sendApiRequest("get-petition-metadatas", { "petition_type":"expired" }, addPetitions2ListForDirect, false);
}

function performReady2Search(){
    if(this.checked){
        performShowAllPetitions();
        document.getElementById("petition_type_radios").style.display = "none";
        document.getElementById("petition_search_form").style.display = "block";
    }
    else{
        location.reload();
    }
}

function searchPetition(event){
    var byTitle = document.getElementById("by_title").checked;
    var byId = document.getElementById("by_id").checked;
    var byContent = document.getElementById("by_content").checked;
    var by;

    var token = document.getElementById("search_token").value;
    var petitions = JSON.parse(JSON.stringify(allPetitions));

    if(byTitle){
        by = "title";
    }
    else if(byId){
        by = "id"
    }
    else if(byContent){
        by = "content"
    }

    for(let i = 0; i < petitions.length; i++){
        if(String(petitions[i][by]).toLowerCase().indexOf(token.toLowerCase()) > -1){
            petitions[i]["display"] = "block";
        }
        else{
            petitions[i]["display"] = "none";
        }
    }

    addPetitions2List(petitions, "searching");
}