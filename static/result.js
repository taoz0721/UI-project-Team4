$(document).ready(function(){
    $("#back_home").click(function(){
        window.location.href='/';
    });
    $("#redo").click(function(){
        var user_score = [0,0,0,0]
        var save={
            "1": false,
            "2": false,
            "3": false,
            "4": false
        }
        var user_answer={
            "1": null,
            "2": null,
            "3": null,
            "4": null
        }
        var data={
            "user_score":user_score,
            "user_answer":user_answer,
            "save": save
        }
        $.ajax({
            type: "POST",
            url: "/quiz_redo",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(data),
            success:function(result) {
                window.location.href='/quiz/1';
            }
        })
    });
});