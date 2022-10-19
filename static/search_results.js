function displayNames(data, result_tea, search_name){
    $("#result_tea").empty();

    let len = result_tea.length

    let search_div = $(`
                <div class = "big dark"> ${len} Search Results for "${search_name}":</div> <br>
            `);

    $("#result_tea").append(search_div);
    
    if (result_tea.length == 0){
        let new_div = $(`
                <div>No results found</div> <br>
            `);
            $("#result_tea").append(new_div);

    }else{
        $.each(result_tea, function(i, value) {
            let tea = data[value];
            let new_div =`
                <a class="nav-link" href="/view/${tea.id}">
                <div class="row">
                    <div class="col-md-3 col-sm-12 border">
                        <img src="${tea.Image}" alt="${tea.title} picture" class = "pic">
                    </div>
                    <div class="col-md-2 col-sm-12 border grey_text searcharea"> 
                        <div class = "big"> ${tea.title} </div>
                    </div>
                    <div class="col-md-2 col-sm-12 border grey_text searcharea"> 
                        <div class = "big"> ${tea.location} </div>
                    </div>
                    <div class="col-md-5 col-sm-12 border"> `
    
            let items = tea.popular_orders;
            $.each(items, function(i, value) {
                let new_item = `
                    <button id = "${value}" class = "popular_item small_space lightgrey searcharea">${value} </button>
                `
                new_div += new_item; 
            });
    
            new_div += `</div>
                </div>    
                </a> <br>
            `

            $("#result_tea2").append(new_div);
        });
    }

    replaceText(search_name)
}

function replaceText(search_name) {

    $("body").find(".highlight").removeClass("highlight");

    let searchword = search_name;

    let custfilter = new RegExp(searchword, "ig");
    let repstr = "<span class='highlight'>" + searchword + "</span>";

    if (searchword != "") {
        $('.searcharea').each(function() {
            $(this).html($(this).html().replace(custfilter, repstr));
        })
    }
}

$(document).ready(function(){
    displayNames(data, result_tea, search_name)                        
})


