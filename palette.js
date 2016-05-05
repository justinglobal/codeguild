'use strict';

function getRawColorString() {
  return $('#color-input').val();
}

function renomalizeColor(componentValue) {
  return Math.round(componentValue * 255);
}


function convertRawColorToCSSColor(rawColor) {
  var colorComponentStrings = _.split(rawColor, ' ');
  var colorComponentNumbers = _.map(colorComponentStrings, Number);
  var normalizedColorComponents = _.map(colorComponentNumbers, renomalizeColor);
  var joinedColorComponents = _.join(normalizedColorComponents, ', ');
  return 'rgb(' + joinedColorComponents + ')';
}

function selectSwatch() {
  return $('.swatch');
}

function applyCSSColorAsBackground(selection, cssColor) {
  selection.css('background', cssColor);
}

function runUpdateColor() {
  var rawColor = getRawColorString();
  var cssColor = convertRawColorToCSSColor(rawColor);
  var swatchSelection = selectSwatch();
  applyCSSColorAsBackground(swatchSelection, cssColor);
}

function registerInitialEventHandlers() {
  $('#color-input').on('input', runUpdateColor);
}
//   $('#color-input')on('input', function (){
//     runUpdateColor();
//   });
// }

registerInitialEventHandlers();
