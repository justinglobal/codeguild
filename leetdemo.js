"use strict";

var convertWordToLeeSpeak = function(originalWord) {
  var originalCharToLeetChar = {
    "o": "0",
    "l": "1",
    "e": "3",
    "a": "4",
    "t": "7",
    "s": "Z",
  };

  for (var originalChar in originalCharToLeetChar) {
    var leetChar = originalCharToLeetChar[originalChar];
    while (originalWord.includes(originalChar)) {
      originalWord = originalWord.replace(originalChar, leetChar);
    }
  }

  var lastOriginalChar = originalWord.slice(-1);
  if (lastOriginalChar === "s"){
    originalWord = originalWord.slice(0, -1) + "Z";
  }
  return "(" + originalWord + ")";
};

console.log(convertWordToLeeSpeak("hello"));

var convertSentenceToLeetSpeak = function(sentence) {
  var originalWords = sentence.split(" ");
  var leetWords = originalWords.map(convertWordToLeeSpeak);
  return leetWords.join(" ");
}

console.log(convertSentenceToLeetSpeak("love a sentence"));
