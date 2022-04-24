function TFsaved(data, idx, user_answer){
    
    $("input[name='TF'][value='"+user_answer+"']").attr("checked",true);
    var data_id=$("input[name='TF']:checked").data("id");
    console.log(user_answer==data["answer"]);
    if(user_answer==data["answer"]){
        $(".check_div_TF[data-id='"+data_id+"']").html("<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3mYBIRnyLDSh0OYf4pS2fd0xid0HVP81NysKqcOYPg0FOth7K7VUNpxmtJ_cyV8NQAaA&usqp=CAU' width='30%'>");
    }
    else{
        $(".check_div_TF[data-id='"+data_id+"']").html("<img src='https://us.123rf.com/450wm/vectora/vectora1704/vectora170401047/75817847-red-cross-symbol-icon-as-delete-remove-fail-failure-or-incorrect-answer-icon.jpg' width='30%'>");
    }
    
}

function dropSaved(data, idx, user_answer){
    $.each(user_answer,function(key,value){
        $(".drop_div[data-answer='"+key+"']").html("<div class='draggable_tag' data-value='"+value+"'>"+value+"</div>");
        if(key==value){
            $(".check_div[data-answer='"+key+"']").html("<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3mYBIRnyLDSh0OYf4pS2fd0xid0HVP81NysKqcOYPg0FOth7K7VUNpxmtJ_cyV8NQAaA&usqp=CAU' width='30%'>");
        }
        else{
            $(".check_div[data-answer='"+key+"']").html("<img src='https://us.123rf.com/450wm/vectora/vectora1704/vectora170401047/75817847-red-cross-symbol-icon-as-delete-remove-fail-failure-or-incorrect-answer-icon.jpg' width='30%'>");
        }
    });
    
}

$(document).ready(function(){
    
    $("#review").click(function(){
        var area=data["area"]
        var link="/"+""+area+"";
        window.location.href=link;
    });
    if(data["type"]=="TF"){
        TFsaved(data, idx, user_answer);
    }
    else{
        dropSaved(data, idx, user_answer)
    }

    $(".previous").click(function(){
        index=parseInt(idx)
        if(index==1){
            window.location.href='/earsandeyes';
        }
        else{
            index-=1;
            let link="/quiz/"+""+index+"";
            window.location.href=link;
        }
    });

    $(".next").click(function(){
        index=parseInt(idx)
        if(index==4){
            window.location.href='/result';
        }
        else{
            index+=1;
            let link="/quiz/"+""+index+"";
            window.location.href=link;
        }
    });
});