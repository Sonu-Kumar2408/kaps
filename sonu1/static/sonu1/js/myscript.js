
document.addEventListener("DOMContentLoaded", function(){
    $('.plus-cart').click(function(){
        var id = $(this).attr("pid");
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
        });
    });
})

document.addEventListener("DOMContentLoaded", function(){
    $('.minus-cart').click(function(){
        var id = $(this).attr("pid");
        var b = this.parentNode.children[2]
        console.log("pid=",id)
        $.ajax({
            type:"GET",
            url:"/minuscart",
            data:{
                prod_id:id
            },
            success:function(data){
                console.log("data =",data);
                b.innerText=data.quantity
                document.getElementById("amount").innerText=data.amount
                document.getElementById("totalamount").innerText=data.totalamount
            }
        });
    });
})

document.addEventListener("DOMContentLoaded", function(){
    $('.remove-cart').click(function(){
        var id = $(this).attr("pid");
        var b = this.parentNode.children[2]
        console.log("pid=",id)
        $.ajax({
            type:"GET",
            url:"/removecart",
            data:{
                prod_id:id
            },
            success:function(data){
                console.log("data =",data);
                b.innerText=data.quantity
                document.getElementById("amount").innerText=data.amount
                document.getElementById("totalamount").innerText=data.totalamount
            }
        });
    });
})