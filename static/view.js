function displayItem(data, id){
    $("#tea_info").empty();
    if (id in data){
        tea = data[id]
        let new_div = ""
        new_div += `
            <div class="row">
                <div class="col-md-5 col-sm-12">
                    <div class = "bigger"> ${tea.title} </div>
                    <img src="${tea.Image}" alt="${tea.title} picture" class = "pic img">
                </div>
                <div class="col-md-7 col-sm-12"> 
                <br><br><div>`

                rating = parseFloat(tea.rating)
                if (rating < 1){
                    rating = 1
                }
                if(rating > 5){
                    rating = 5
                }
                for (let i = 0; i < rating; i++){
                    new_div += `<img src="../static/star.png" alt="star" class = "star">`
                }

                new_div += "</div><br>"
            
                new_div += `
                    <div class = "location"> <span class = "faint"> Location:</span> <span class = "hello_div big">${tea.location}</span></div><br>
                    <div class = "address"> <span class = "faint">Address:</span> ${tea.address}</div><br>
                    <div class = "hours"> <span class = "faint">Hours:</span> ${tea.hours}</div><br>
                </div>

            </div>
            <span class = "popular_orders faint small_space"> Popular orders: </span>
        `
        $("#tea_info").append(new_div);
        let items = tea.popular_orders;
        $.each(items, function(i, value) {
            let new_item = $(`
                <button id = "${value}" class = "popular_item small_space lightgrey">${value} </button>
            `);
            $("#tea_info").append(new_item); 
        });

        let new_div2 = $(`
        <div class = "description">${tea.description}</div><br>
        `);
        $("#tea_info").append(new_div2); 

        let new_div3 = $(`
        <button type="button" class = "darkgrey" onclick="window.location.href='http://127.0.0.1:5000/edit/${id}'">Edit</button>
        `);
        $("#tea_info").append(new_div3); 

    }else{
        $("#tea_info").append("No Result")
    }
}

$(document).ready(function(){
    displayItem(data, id)
})
