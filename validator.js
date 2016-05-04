"use strict"

function

object.onsubmit=function(){myScript};

object.addEventListener("submit", myScript);

document.getElementById("myBtn").addEventListener("click", function(){
    document.getElementById("demo").innerHTML = "Hello World";
});

// example html
// <form id="hello-world" action="sayhello">
//     <input type="submit" value="Hello!">
// </form>

$('#hello-world').submit(function(ev) {
    ev.preventDefault(); // to stop the form from submitting
    /* Validations go here */
    this.submit(); // If all the validations succeeded
});
