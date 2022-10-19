function removeAttr(key){
    $("#"+key).removeAttr("disabled")
}

function tochanges(id){
  let r = confirm("Are you sure?")
  if (r == true){
      window.location.href = "/view/"+id
    }
}

$(document).ready(function(){
  obj = data[0]
  $("#title").val(obj.title)
  $("#Image").val(obj.Image)
  $("#description").val(obj.description)
  $("#location").val(obj.location)
  $("#address").val(obj.address)
  $("#hours").val(obj.hours)
  $("#rating").val(obj.rating)
  $("#popular_orders").val(obj.popular_orders)

})