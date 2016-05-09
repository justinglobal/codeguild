'use strict';

function getNumOfDice() {
  return $('#numOfDice').val();
}

function getRollResult() {
  var rollResult = Math.floor(Math.random() * 6) + 1;
  return rollResult;
}

function getDiceImage(rollResult) {
  var diceImage = '';
  if (rollResult === 1) {
    diceImage = 'http://game-icons.net/icons/delapouite/dice/png/dice-six-faces-one.png';
  } else if (rollResult === 2) {
    diceImage = 'http://game-icons.net/icons/delapouite/dice/png/dice-six-faces-two.png';
  } else if (rollResult === 3) {
    diceImage = 'http://game-icons.net/icons/delapouite/dice/png/dice-six-faces-three.png';
  } else if (rollResult === 4) {
    diceImage = 'http://game-icons.net/icons/delapouite/dice/png/dice-six-faces-four.png';
  } else if (rollResult === 5) {
    diceImage = 'http://game-icons.net/icons/delapouite/dice/png/dice-six-faces-five.png';
  } else if (rollResult === 6) {
    diceImage = 'http://game-icons.net/icons/delapouite/dice/png/dice-six-faces-six.png';
  }
  return diceImage;
}

function createDiceImageElement(diceImage) {
  var diceImageElement = $('<img>').attr('src', diceImage);
  return diceImageElement;
}

function createRollResultDiv(diceImageElement) {
  // put on click stuff here
  var resultDisplay = $('<div></div>').append(diceImageElement);
  resultDisplay.on('click', function(event) {
    // event.preventDefault();
    var diceImageElement = '';
    // var rollResult = getRollResult();
    // var diceImage = getDiceImage(rollResult);
    // var diceImageElement = createDiceImageElement(diceImage);
    // $('<div></div>').replaceWith(diceImageElement);
  });
  return resultDisplay;
}

function addRollToSection(resultDisplay) {
  $('section').append(resultDisplay);
}

// function reRollDie () {
//   $('#dicedisplay').on('click', function (event) {
//     event.preventDefault();
//     var diceImageElement = '';
//     var rollResult = getRollResult();
//     var diceImage = getDiceImage(rollResult);
//     var diceImageElement = createDiceImageElement(diceImage);
//     $('<div></div>').replaceWith(diceImageElement);
//   })
// }

function getRollResultAddToSection() {
  var counter = 0;
  while (counter < getNumOfDice()) {
    var rollResult = getRollResult();
    var diceImage = getDiceImage(rollResult);
    var diceImageElement = createDiceImageElement(diceImage);
    var resultDisplay = createRollResultDiv(diceImageElement);
    addRollToSection(resultDisplay);
    counter += 1;
  }
}

function registerEventHandlers() {
  $('form').on('submit', function(event) {
    event.preventDefault();
    getRollResultAddToSection();
  });
}

$(document).ready(function() {
  registerEventHandlers();
  // reRollDie();
});
