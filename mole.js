'use strict';

function getRandIntForId() {
  var randIntId = Math.floor(Math.random() * 20) + 1;
  return randIntId;
}
function getImgToChange(randIntId) {
  var imgToChange = document.getElementById(randIntId);
  return imgToChange;
}

function changeImg(imgToChange) {
  $(imgToChange).attr('src', 'http://thumbs.dreamstime.com/m/illustrator-mole-cartoon-isolated-62124898.jpg');
  $(imgToChange).on('click', function() {
    alert('You cliked the mole!');
  });
}

function changeRandHoleToMole() {
  $('.gameImage').off('click');
  $('.gameImage').attr('src', 'http://emojipedia-us.s3.amazonaws.com/cache/04/a8/04a80422dae419411d68d431c3c8ae49.png');
  var randIntId = getRandIntForId();
  var imgToChange  = getImgToChange(randIntId);
  changeImg(imgToChange);
}

function setMoleDisplayInterval() {
  window.setInterval(changeRandHoleToMole, 2000);
}
function registerEventHandlers() {
  // this does not do anything b/c I use .off in changeRandHoleToMole() function
  $('.gameImage').on('click', function(event) {
    event.preventDefault();
    $(event.target).attr('src', 'https://static2.fjcdn.com/thumbnails/comments/It+_4c5b4023_c642_5845.jpg');
  });
  setMoleDisplayInterval();
}

$(document).ready(registerEventHandlers);


// function getNewImage() {
//   $('img').attr('src', 'http://emojipedia-us.s3.amazonaws.com/cache/04/a8/04a80422dae419411d68d431c3c8ae49.png');
// }
// function showIntervalTestImage() {
//   $('#6').attr('src', 'http://thumbs.dreamstime.com/m/illustrator-mole-cartoon-isolated-62124898.jpg');
// }
// function testChangeImage() {
//   window.setInterval(showIntervalTestImage, 1000);
// }
