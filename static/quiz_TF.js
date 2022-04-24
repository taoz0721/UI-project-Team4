

function makeDraggable(){
    $(".draggable_tag").mouseover(function(){
		$(this).addClass("hover");
	});
    $(".draggable_tag").mouseout(function(){
		$(this).removeClass("hover");
	});
    $(".draggable_tag").draggable({
        revert: true,
        stack:".draggable_tag",
    })
}
function dropTag(){
    $(".drop_div").droppable({
        tolerance:"touch",
        drop: function(event,ui){
            let dropped_tag=ui.draggable;
            let dropped_value=$(dropped_tag).data("value");

            let drop_div_text= $(this).text();
            if (drop_div_text!=""){
                $(".tag_div[data-value='"+drop_div_text+"']").html("<div class='draggable_tag' data-value='"+drop_div_text+"'>"+drop_div_text+"</div>");
            }
            $(".draggable_tag[data-value='"+dropped_value+"']").remove();
            $(this).attr("class","drop_div");
            $(this).html("<div class='draggable_tag' data-value='"+dropped_value+"'>"+dropped_value+"</div>");

            makeDraggable();
        },
        over: function(event,ui){
            let text=$(this).text();
            // if(text=="")
            // {
                $(this).attr("class", "over");
                console.log("over empty");
            // }
            // else{
            //     $(this).attr("class","hover");
            //     console.log("over text");
            // }
        },
        out: function(event, ui){
            let text=$(this).text();
            // if(text!=""){
            //     console.log("out text")
            // }
            //else{
                $(this).attr("class","drop_div");
                console.log("out empty");
            //}
        }
        
    });
}

function checkDragandDrop(data, idx){
    $(".next").click(function(){
        $(".check_div").empty();
        var count=0;
        $.each(data["tags"],function(index, value){
            var drop_div_content=$(".drop_div[data-answer='"+value+"']").text();
            console.log(drop_div_content);
            if(drop_div_content==""){
                //alert("You have to match all pictures with the corresponding words!");
                $(".check_div[data-answer='"+value+"']").html("Cannot Leave It Blank!");
                count+=1;
            }
        });

        if(count==0){
            $.ajax({
                type: "POST",
                url: "/quiz_check_save",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(idx),
                success:function(result) {
                    var HasSaved=result["save"];
                    if(HasSaved){
                        if(parseInt(idx)!=4){
                            num=parseInt(idx)
                            num+=1;
                            let link="/quiz/"+""+num+"";
                            window.location.href=link;
                        }
                        else{
                            window.location.href='/result';
                        }   
                    }
                    else{
                        alert("You haven't saved you answer!");
                    }
                }
            })
            
        }
       
    });
}

function checkTF(data,idx){
    $(".next").click(function(){
        $.ajax({
            type: "POST",
            url: "/quiz_check_save",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(idx),
            success:function(result) {
                var HasSaved=result["save"];
                var radioValue = $("input[name='TF']:checked").val();
            if(radioValue){
                if(HasSaved){
                    if(parseInt(idx)!=4){
                        num=parseInt(idx)
                        num+=1;
                        let link="/quiz/"+""+num+"";
                        window.location.href=link;
                    }
                    else{
                        window.location.href='/result';
                    }   
                }
                else{
                    alert("You haven't saved you answer!");
                }
               
            }
            else{
                alert("You have to choose an option!")
            }
            }
        })
        
    });
}

function saveTF(data, idx){
    
    $("#save").click(function(){
        $(".check_div_TF").empty();

        var radioValue = $("input[name='TF']:checked").val();
        console.log(radioValue);
        if(radioValue){
            let answer = {"score":0, "idx":idx, "save":true, "type": "TF", "answer":radioValue};
            if(radioValue==data["answer"]){
                answer = {"score":1, "idx":idx, "save":true, "type": "TF", "answer":radioValue};
            }
            $("#review_btn").html("<button id='review'>Review</button>");
                    $("#review").click(function(){
                        var area=data["area"]
                        var link="/"+""+area+"";
                        window.location.href=link;
                    });
           $.ajax({
                type: "POST",
                url: "/quiz_get_result",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(answer),
                success:function(result) {
                    let answer=result["answer"];
                    console.log(answer);
                    let data_id=$("input[name='TF']:checked").data("id");
                    if(answer==1){
                        $(".check_div_TF[data-id='"+data_id+"']").html("<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3mYBIRnyLDSh0OYf4pS2fd0xid0HVP81NysKqcOYPg0FOth7K7VUNpxmtJ_cyV8NQAaA&usqp=CAU' width='30%'>");
                    }
                    else{
                        $(".check_div_TF[data-id='"+data_id+"']").html("<img src='https://us.123rf.com/450wm/vectora/vectora1704/vectora170401047/75817847-red-cross-symbol-icon-as-delete-remove-fail-failure-or-incorrect-answer-icon.jpg' width='30%'>");
                    }
                    
                    //HasSaved=true;
                }
            })
        }
        else{
            alert("You have to choose an option!")
        }
    });
}

function saveDrop(data, idx){
    $("#save").click(function(){
        $(".check_div").empty();
        var count=0;
        //var final_answer='';
        $.each(data["tags"],function(index, value){
            console.log(value);
            let final_answer=$(".drop_div[data-answer='"+value+"']").children().length;
            console.log(final_answer);
            if(final_answer>0){
                //alert("You have to match all pictures with the corresponding words!");
                count+=1;
            }
            else{
                $(".check_div[data-answer='"+value+"']").html("Cannot Leave It Blank!");
                
            }
        });
        
        
        if(count==3){
            let right_num=0;
            let answer={"score":0, "idx":idx, "save":true, "type": "Drag", "answer":{}};
            let final_check='';
            console.log("all checked");
            $.each(data["tags"],function(index, value){
                final_check=$(".drop_div[data-answer='"+value+"']").children().text();
                answer["answer"][value]=final_check;
                console.log(final_check);   
                if(final_check==value){
                    right_num+=1;
                    $(".check_div[data-answer='"+value+"']").html("<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3mYBIRnyLDSh0OYf4pS2fd0xid0HVP81NysKqcOYPg0FOth7K7VUNpxmtJ_cyV8NQAaA&usqp=CAU' width='30%'>");
                }
                else{
                    $(".check_div[data-answer='"+value+"']").html("<img src='https://us.123rf.com/450wm/vectora/vectora1704/vectora170401047/75817847-red-cross-symbol-icon-as-delete-remove-fail-failure-or-incorrect-answer-icon.jpg' width='30%'>");
                }       
            });
            if(right_num==3){
                answer["score"]=1;
            }
            $("#review_btn").html("<button id='review'>Review</button>");
                    $("#review").click(function(){
                        var area=data["area"]
                        var link="/"+""+area+"";
                        window.location.href=link;
                    });
            $.ajax({
                type: "POST",
                url: "/quiz_get_result",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(answer),
                success:function(result) {
                }
            });
        }
    });
}

$(document).ready(function(){
    makeDraggable();
    dropTag();

    $(".previous").click(function(){
        var index=parseInt(idx)
        if(index==1){
            window.location.href='/earsandeyes';
        }
        else{
            index-=1;
            let link="/quiz/"+""+index+"";
            window.location.href=link;
        }
    });

    
    //TF
    if(data["type"]=="TF"){
        //save, next button
        saveTF(data, idx);
        checkTF(data, idx,HasSaved);
    }
    else{
        //Drag and Drop
        //next button
        saveDrop(data, idx);
        checkDragandDrop(data, idx,HasSaved);
    }
  
        

   
});