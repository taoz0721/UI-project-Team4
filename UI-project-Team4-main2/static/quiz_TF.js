
$(document).ready(function(){

    $(".previous").click(function(){
        window.location.href='/earsandeyes';
    })
    $(".next").click(function(){
        var radioValue = $("input[name='TF']:checked").val();
        if(radioValue){
           if(radioValue=="False"){
           }
        }
        else{
            alert("You have to choose an option!")
        }
        window.location.href='/result';
    })

    $("#save").click(function(){
        var radioValue = $("input[name='TF']:checked").val();
        if(radioValue){
            let data = 0;
            if(radioValue=="False"){
                data = 1;
            }
           $.ajax({
                type: "POST",
                url: "/quiz_get_result",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(data),
                success:function(result) {
                    window.location= "/result";
                }
            })
        }
        else{
            alert("You have to choose an option!")
        }
    });
});