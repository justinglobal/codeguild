"use strict";

function getReminderString() {
  return $("#reminder-input").val();
}

function createDelLink(){
  var delLink = $("<a></a>").text("X").attr("href", "");
  delLink.on("click", function (event) {
    event.preventDefault();
  });
  return deLink;
}

function createReminderElement() {
  var reminderElement = $("<li></li>").text(reminderString);
  var delLink = createDelLink();
  return reminderElement.append(delLink);
}

function addReminderElementToList(reminderElement) {
   $("reminder-list").append(reminderElement);
 }

function getReminderStringAndAddElementToList(){
  var reminderString = getReminderString()
  var reminderElement = createReminderElement(reminderString);
  addReminderElementToList(reminderElement);
}

$("form").on("submit" , function (event) {
  event.preventDefault();
  getReminderStringAndAddElementToList();
});
