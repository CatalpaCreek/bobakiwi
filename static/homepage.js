function displayNames(data, popular_tea){
    $("#popular").empty();
    $.each(popular_tea, function(i, value) {
        let tea = data[value];
        let new_div =`
            <a class="nav-link" href="/view/${tea.id}">
            <div class="row">
                <div class="col-md-3 col-sm-12 border">
                    <img src="${tea.Image}" alt="${tea.title} picture" class = "pic">
                </div>
                <div class="col-md-2 col-sm-12 border grey_text"> 
                    <div class = "big"> ${tea.title} </div>
                </div>
                <div class="col-md-2 col-sm-12 border grey_text"> 
                    <div class = "big"> ${tea.location} </div>
                </div>
                <div class="col-md-5 col-sm-12 border"> `

        let items = tea.popular_orders;
        $.each(items, function(i, value) {
            let new_item = `
                <button id = "${value}" class = "popular_item small_space lightgrey">${value} </button>
            `
            new_div += new_item; 
        });

        new_div += `</div>
            </div>    
            </a> <br>
        `
        $("#popular").append(new_div);
        
    });
}

$(document).ready(function(){
    displayNames(data, popular_tea)                        
})