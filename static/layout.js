function progress(section){
    $(".nav-item").css("background-color","cornflowerblue"); 

    id=""+section+"_section";
    $("#"+id+"").css("background-color","sea blue");
}

$(document).ready(function(){
    progress(section)
})