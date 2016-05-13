'use strict';

// 1. Input fucitons (2)
// gets setup-text using jquery by ajax_index element id
function getSetupText() {
  return $('#setup-text').val();
}
// gets punchline-text using jquery by ajax_index element id
function getPunchlineText() {
  return $('#punchline-text').val();
}

// 2. Transform Functions - n/a setup and punchline text defined as needed from input

// 3. Create Functions (2)
// defines variable blockquote using jquery element assignment as <blockquote>
// inserts setupText into blockquote
// appends new blockquote element to body element
function appendSetup(setupText) {
  var blockquote = $('<blockquote></blockquote>');
  blockquote.text(setupText);
  $('body').append(blockquote);
}
// defines variable blockquote using jquery element assignment as <blockquote>
// inserts punchlineText into blockquote
// appends new blockquote element to body element
function appendPunchline(punchlineText) {
  var blockquote = $('<blockquote></blockquote>');
  blockquote.text(punchlineText);
  $('body').append(blockquote);
}

// this function wants to make a hide button and define it's behavior on click
// function makeHideButton() {
//   var hideButton = $('<button></button>');
//   $('body').append.(hideButton);
// }

// 4. Modify Function - posts setup and puncline text using .get on /ajax/submit url
function postJokeText(setupText , punchlineText) {
  var data = {
    'setup_text': setupText,
    'punchline_text': punchlineText,
  };
  $.get('/ajax/submit', data, function() {
    appendSetup(setupText);
    appendPunchline(punchlineText);
    makeHideButton();
  });
}
// reset setup-text and punchine-text fields
function resetInputs() {
  $('#setup-text').val('enter setup');
  $('#punchline-text').val('enter punchline');
}


// 5. Main function - submits comment
function submitComment() {
  var setupText = getSetupText();
  var punchlineText = getPunchlineText();
  postJokeText(setupText, punchlineText);
  resetInputs();
}

// 6. Register Functions
function registerInitialEventHandlers() {
  $('#joke-form').on('submit', function(event) {
    event.preventDefault();
    submitComment();
  });
}

// call to document
$(document).ready(registerInitialEventHandlers);
