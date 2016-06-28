'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 2, p: 2, l: 1}

function countLetters(string) {
  var lettersList = (string.split(''));
  var letters = {};
  lettersList.forEach(function (e) {
    if (!(e in letters)) {
    letters[e] = 1;
  } else {
    letters[e]++;
  }
  });
  return letters;
}

console.log(countLetters('apple'));
