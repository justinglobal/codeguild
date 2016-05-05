'use strict';

function getNameFromNameBox() {
  return $('#idname').val();
}
function getPhoneFromPhoneBox() {
  return $('#idphone').val();
}
function getAgeFromAgeBox() {
  return $('#idage').val();
}
function isNameValid(nameInput) {
  if (nameInput.includes(' ') === true) {
    return true;
  } else {
    return false;
  }
}
function isPhoneValid(phoneInput) {
  var phoneSplit = phoneInput.split('-');
  if (phoneSplit.length !== 3 || phoneInput.length !== 12) {
    return false;
  } else {
    for (var i = 0; i < phoneSplit.length; i += 1) {
      var textGroup = phoneSplit[i];
      if (isNaN(textGroup) === true) {
        return false;
      }
    }
    return true;
  }
}
function isAgeValid(ageInput) {
  var ageSplit = ageInput.split('-');
  if (ageSplit.length !== 3 || ageInput.length !== 10) {
    return false;
  } else {
    for (var i = 0; i < ageSplit.length; i += 1) {
      var textGroup = ageSplit[i];
      if (isNaN(textGroup) === true) {
        return false;
      }
    }
    return true;
  }
}

function setNameBoxColor(isNameBoxValid) {
  if (isNameBoxValid === false) {
    $('#idname').css('background-color', 'yellow');
  } else {
    $('#idname').css('background-color', 'white');
  }
}
function setPhoneBoxColor(isPhoneBoxValid) {
  if (isPhoneBoxValid === false) {
    $('#idphone').css('background-color', 'yellow');
  } else {
    $('#idphone').css('background-color', 'white');
  }
}
function setAgeBoxColor(isAgeBoxValid) {
  if (isAgeBoxValid === false) {
    $('#idage').css('background-color', 'yellow');
  } else {
    $('#idage').css('background-color', 'white');
  }
}
function checkName() {
  var nameInput = getNameFromNameBox();
  var isNameBoxValid = isNameValid(nameInput);
  setNameBoxColor(isNameBoxValid);
}
function checkPhone() {
  var phoneInput = getPhoneFromPhoneBox();
  var isPhoneBoxValid = isPhoneValid(phoneInput);
  setPhoneBoxColor(isPhoneBoxValid);
}
function checkAge() {
  var ageInput = getAgeFromAgeBox();
  var isAgeBoxValid = isAgeValid(ageInput);
  setAgeBoxColor(isAgeBoxValid);
}

function registerInitialEventHandlers() {
  $('#idname').on('input', checkName);
  $('#idage').on('input', checkAge);
  $('#idphone').on('input', checkPhone);
}

registerInitialEventHandlers();

// document.getElementById('iname').onkeyup = function() {validateUpper()};
//
// function validateUpper() {
//     var letter = document.getElementById('iname');
//     letter.value = letter.value.toUpperCase();
// }
//
// document.getElementById('iphone').onkeyup = function () {validatePhone()};
//
// function validatePhone() {
//   var input = document.getElementById('iphone');
//   if (input === null || input === '') {
//         style='background-color:orange;'
//         // alert('Name must be filled out');
//         return false;
//   }
// }
