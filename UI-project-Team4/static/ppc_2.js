var employees = [
"Phyllis",
"Angela",
"Dwight",
"Oscar",
"Creed",
"Pam",
"Jim",
"Stanley",
"Michael",
"Kevin",
"Kelly"
];

var pplist = [];
function changecolor(item){
	item.addClass("drag-blue");
}
function colorback(item){
	item.removeClass("drag-blue");
}

function drage(data){
	$.each(data, function (index, value) {
		//$("#sale-person"x).prepend('<dt>'+value.salesperson+'</dt>');
		$('#nppc').append('<div class="row drag np border" id="'+value+'">' + (index+1) +': '+value + '</div>');
		$('#'+value).draggable({
			cursor:"move", revert: "invalid",
			drag: function() {
				changecolor($("#label-ppc"))
			},
			stop: function() {
		        colorback($("#label-ppc"))
		    }
		});
	}); 
}

function dragp(data){
	$.each(data, function (index, value) {
		//$("#sale-person"x).prepend('<dt>'+value.salesperson+'</dt>');
		$('#ppc').append('<div class="row drag pp border" id="'+value+'">' + (index+1) +': '+value + '</div>');
		$('#'+value).draggable({
			cursor:"move", revert: "invalid",
			drag: function() {
				changecolor($("#label-nppc"))
			},
			stop: function() {
		        colorback($("#label-nppc"))
		    }
		});
	}); 
}

$(document).ready(function(){
	drage(employees);
	$("#label-ppc").droppable({
		accept: function(d) { 
	        if(d.hasClass("np")){ 
	            return true;
	        }
	    },
		drop:function(event, ui){
			$('#ppc').empty();
			$('#nppc').empty();
			$("#label-ppc").removeClass("over-blue");
			let name = $(ui.draggable).prop('id');
			employees.splice( $.inArray(name, employees), 1 );
			pplist.push(name);
			dragp(pplist);
			drage(employees);
		},
		over: function(event, ui) {
	    	$("#label-ppc").addClass("over-blue");
	    },

	    out: function(event, ui) {
	        $("#label-ppc").removeClass("over-blue");
	    },

	})
	$("#label-nppc").droppable({
		accept: function(d) { 
	        if(d.hasClass("pp")){ 
	            return true;
	        }
	    },
	    over: function(event, ui) {
	    	$("#label-nppc").addClass("over-blue");
	    },

	    out: function(event, ui) {
	        $("#label-nppc").removeClass("over-blue");
	    },
		drop:function(event, ui){
			$('#ppc').empty();
			$('#nppc').empty();
			$("#label-nppc").removeClass("over-blue");
			let name = $(ui.draggable).prop('id');
			pplist.splice( $.inArray(name, pplist), 1 );
			employees.push(name);
			dragp(pplist);
			drage(employees);
		}
	})
});