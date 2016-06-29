'use strict';

// 1. store the element that says 'The King' in the 'king' variable.
// console.log it.

// 2. store the element that contains the text 'The Conceited Man'
// in the 'conceited' variable.
// show the result in an 'alert' window.

// 3. store 'The Businessman' and 'The Lamplighter'
// in the 'businessLamp' variable.
// console.log each of them.

// 4. store 'The King' and 'The Conceited Man'
// in the 'conceitedKing' variable.
// alert them one by one.

// 5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
// in the 'noBusiness' variable.
// console.log each of them.

// 6. store 'The Businessman' in the 'allBizniss' variable.
// show the result in an 'alert' window.

//1:
var king = document.querySelector('.asteroid');
console.log(king);

//2:
var conceited = document.querySelector('.b326');
alert(conceited);

//3:
var businessLamp = document.querySelectorAll('.big');
businessLamp.forEach(function (e) {
  console.log(e);
});

//4:
var conceitedKing = document.querySelectorAll('.container div');
conceitedKing.forEach(function (e) {
  alert(e);
});

//5:
var noBusiness = document.querySelectorAll('div.asteroid');
noBusiness.forEach(function (e) {
  console.log(e);
});

//6:
var allBizniss = document.querySelector('p');
alert(allBizniss);
