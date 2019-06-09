//if condition to test ascii value of keydown event
//then change CSS background color of button using id to create light up effect on buttons

document.addEventListener('keydown', function(event) {
    if(event.keyCode == 65) {
        document.getElementById("button1").style.background='#F5FB5A';
    }
    else if(event.keyCode == 72) {
        document.getElementById("button2").style.background='#F5FB5A';
    }
    else if(event.keyCode == 76) {
        document.getElementById("button3").style.background='#F5FB5A';
    }
    else if(event.keyCode == 70) {
        document.getElementById("button4").style.background='#F5FB5A';
    }
});

//if condition to test ascii value of keyup event
//then change CSS background color to return button to original CSS style

document.addEventListener('keyup', function(event) {
	    if(event.keyCode == 65) {
	        document.getElementById("button1").style.background='#EAEAEA';
	    }
	    else if(event.keyCode == 72) {
	        document.getElementById("button2").style.background='#EAEAEA';
	    }
	    else if(event.keyCode == 76) {
	        document.getElementById("button3").style.background='#EAEAEA';
	    }
	    else if(event.keyCode == 70) {
	        document.getElementById("button4").style.background='#EAEAEA';
	    }
	});
