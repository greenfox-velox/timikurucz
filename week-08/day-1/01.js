'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

function newLetterCounter(string) {
  var lettersList = string.split('');
  var letters = {};
  lettersList.forEach(function (e) {
    letters[e] = letters[e] + 1 || 1;
  });
  return letters;
}
console.log(newLetterCounter('apple'));


// // with for loop:
// function letterCounter(string) {
//   var lettersList = string.split('');
//   var letters = {};
//
//   for (var i = 0; i< lettersList.length; i++) {
//     var item = lettersList[i];
//     letters[item] = (letters[item] +1) || 1;
//   }
//   return letters;
// }
// console.log(letterCounter('apple'));


// first version:
// function countLetters(string) {
//   var lettersList = (string.split(''));
//   var letters = {};
//   lettersList.forEach(function (e) {
//     if (!(e in letters)) {
//       letters[e] = 1;
//     } else {
//       letters[e]++;
//     }
//   });
//   return letters;
// }
//
// console.log(countLetters('apple'));

module.exports.newLetterCounter = newLetterCounter;
