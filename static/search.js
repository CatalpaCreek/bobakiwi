
function Check(){
    let search_val = $("#search").val();
    let trimmed = $.trim(search_val);

    console.log(trimmed);

    if(!trimmed){
        $("#search").empty();
        $("#search").focus();
        $("#search").val("");
        return;
    }

    console.log(trimmed)
    $("#search").empty();
    $("#search").val("");
    find_tea(trimmed);
}

function find_tea(search_name){
    let data_to_search = {"search_name": search_name}         
    $.ajax({
        type: "POST",
        url: "../search_name",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_search),
        success: function(result){
            let tea_found = result["result_tea"]
            result_tea = tea_found
            let name_found = result["search_name"]
            search_name = name_found
            console.log(result_tea)
            console.log(search_name)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
    window.location.replace("/search_results");
}

$(document).ready(function(){
    
    $('#search').keydown((e)=>{
        if(e.keyCode==13){
            Check();
        }
    });  

    $("#submit").click(function(){
        Check();
    });

})