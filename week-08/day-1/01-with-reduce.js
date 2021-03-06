'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}


function letterCounter(string) {
  var lettersList = string.split('');
  var countedLetters = lettersList.reduce(function (acc, letter) {
    acc[letter] = acc[letter] + 1 || 1;
    return acc;
  }, {});
  return countedLetters;
}
console.log(letterCounter('apple'));
