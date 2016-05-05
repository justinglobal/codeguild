"use strict";

function getUrl () {
  return $("#url-input").val();
}

function createImgElem () {
  var imgElement = $("<img>").attr("src", getUrl());
  return imgElement;
}

function createImgLink () {
  var imgLink = $("<a></a>").text("Image Source").attr("href", getUrl());
  return imgLink;
}

function createTile () {
  var imgElement = createImgElem();
  var imgLink = createImgLink();
  var newTile = $("<div></div>").append(imgElement, imgLink);
  return newTile;
}

function createDelLink (newTile) {
  var delLink = $("<button></button>").text("remove").attr("href", "");
  delLink.on("click", function (event) {
    event.preventDefault();
    newTile.remove("div");
    var tileCount = $("div").length;
    $("#counter").text("Total number of tiles: " + tileCount);
  });
  return newTile.append(delLink);
}

function addDivToGallery (newTile) {
  $("#gallery").append(newTile)
}

function createTileAddToGallery () {
  var newTile = createDelLink(createTile());
  addDivToGallery(newTile);
}

function countTiles () {
  var tileCount = $("div").length;
  $("#counter").text("Total number of tiles: " + tileCount);
  return tileCount;
}

// function Clear () {
//   document.getElementById("#url-input").value= "";
// }

function registerEventHandlers () {
  $("form").on("submit", function (event) {
    event.preventDefault ();
    createTileAddToGallery ();
    countTiles ();
    $("#url-input").val("");
    // ("#url-input").Clear();
    // boxoftext.Clear();
  })
}

$(document).ready(function () {
  registerEventHandlers();
});
