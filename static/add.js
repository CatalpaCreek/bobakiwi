function upload(){
    let title = $("#title").val()
    let Image = $("#Image").val()
    let description = $("#description").val()
    let location = $("#location").val()
    let address = $("#address").val()
    let hours = $("#hours").val()
    let rating = $("#rating").val()
    let popular_orders = $("#popular_orders").val()

    if (title == "" || Image =="" || description =="" ||location =="" ||address =="" ||hours =="" ||rating =="" ||popular_orders =="" ){
       alert("Please fill in all blanks. Make sure the rating is a number. ")
    }else{
        $.ajax({
            type:"POST",
            url:"addItem",
            dataType:"json",
            data:{"title":title,"Image":Image,"description":description,"location":location,"address":address,"hours":hours,"rating":rating,"popular_orders":popular_orders,},
            success:function(data){
                $("#main").append("<span class = 'big dark'> New item successfully created: </span> <a class = 'big' href='view/"+data.num+"'>see it here</a><br><br>")
                $("#title").val("")
                $("#Image").val("")
                $("#description").val("")
                $("#location").val("")
                $("#address").val("")
                $("#hours").val("")
                $("#rating").val("")
                $("#popular_orders").val("")
                $("#title").focus()
            },
            error:function(jqXHR){
                console.log("Error: "+jqXHR.status);
            }
        });
    }
}

