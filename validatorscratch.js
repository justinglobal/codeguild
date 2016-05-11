<!DOCTYPE html>
<html>
<body>

<p>This example uses the HTML DOM to assign an "onkeyup" event to an input element.</p>

<p>Press a key inside the text field and release it to set the text to uppercase.</p>

Enter your name: <input type="text" id="fname">

<script>
document.getElementById("fname").onkeyup = function() {myFunction()};

function myFunction() {
    var x = document.getElementById("fname");
    x.value = x.value.toUpperCase();
}
</script>

</body>
</html>


*change color of input field:
style="background-color:orange;"
*


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



<form name="myForm" action="demo_form.asp" onsubmit="return validateForm()" method="post">
Name: <input type="text" name="fname">
<input type="submit" value="Submit">
</form>

function validateForm() {
    var x = document.forms["myForm"]["fname"].value;
    if (x == null || x == "") {
        alert("Name must be filled out");
        return false;
    }
}
