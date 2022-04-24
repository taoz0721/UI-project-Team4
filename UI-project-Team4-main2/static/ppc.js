// options = [
//     {
//         "id" : 1,
//         "section" : "body",
//         "description" : ["Anxiety", "Aggression", "Relaxed"]
//     },
//     {
//         "id" : 2,
//         "section" : "tails",
//         "description" : ["Friendly", "Irritated", "Terrified"]
//     },
//     {
//         "id" : 3,
//         "section" : "eyes_and_ears",
//         "description" : ["Attentive", "Threatened", "Comfortable"]
//     }
// ]
options = [
    "Anxiety",
    "Aggression",
    "Relaxed"
]

let nppc = options
let ppc = []

function make_draggable(index, name) {

    let new_name = $("<div></div>")
    new_name.html((index + 1) + ": " + name)
    new_name.addClass("name")

    return new_name
}

function make_names() {

    $.each(["#nppc-list", "#ppc-list"], function (i, selector) {

        $(selector).empty()

        let name_list = [nppc, ppc][i]

        $.each(name_list, function (index, name) {

            let person = make_draggable(index, name)
            $(selector).append(person)
        })
    })

    $(".name").draggable({
        revert: true,

        start: function(event, ui){
            $("nppc").addClass("dark")
            $("ppc").addClass("dark")
        },

        stop: function(event, ui){
            $("nppc").removeClass("dark")
            $("ppc").removeClass("dark")
        }
    })

    $(".name").hover(
        function() {
            $(this).addClass("ui_highlight")
        },

        function() {
            $(this).removeClass("ui_highlight")
        }
    )
}

function update_names(name, from, to) {

    let index = eval(from).indexOf(name)
    eval(from).splice(index, 1)
    eval(to).push(name)
}

function drop_handler(event, ui, current) {

    current.removeClass("darker")
    name = ui.draggable.html().slice(3)

    let parent_id = ui.draggable.parent().attr('id')
    
    if (parent_id == "nppc-list") {
        from = "nppc"
    } 
    if (parent_id == "ppc-list") {
        from = "ppc"
    }

    update_names(name, from, current.attr('id'))

    make_names()

}

$(document).ready(function() {
    make_names()

    $("#ppc").droppable({

        over: function(event, ui){
            $(this).addClass("darker")
        },

        out: function(event, ui){
            $(this).removeClass("darker")
        },

        drop: function (event, ui) {
            drop_handler(event, ui, $(this))
        }
    });

    $("#nppc").droppable({

        over: function(event, ui){
            $(this).addClass("darker")
        },

        out: function(event, ui){
            $(this).removeClass("darker")
        },

        drop: function (event, ui) {
            drop_handler(event, ui, $(this))
        }
    });
})