//init and assign variables

var today = new Date();
var hour = today.getHours();
var greetuser;

//if condition to assign a string to greetuser variable based upon current time

if (hour > 18) {
	greetuser = "Good Evening J.A.R.V.I.S. User";
}
else if (hour > 12) {
	greetuser = "Good Afternoon J.A.R.V.I.S. User";
}
else if (hour > 0) {
	greetuser = "Good Morning J.A.R.V.I.S. User";
}
else {
	greetuser = "Welcome J.A.R.V.I.S. User";
}

//print greetuser to file as a header

document.write('<h3 class="header-text">' + greetuser + '</h3>');