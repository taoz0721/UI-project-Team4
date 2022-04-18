
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
           if(radioValue=="False"){
           }
        }
        else{
            alert("You have to choose an option!")
        }
    });
});