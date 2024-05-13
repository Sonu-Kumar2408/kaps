

$('.plus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var b = this.parentNode.children[2]
    console.log("pid=",id)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data =",data);
            b.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
    })
})