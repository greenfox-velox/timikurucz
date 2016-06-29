'use strict';
// On the click of the button,
// Count the items in the list
// And display the result in the result element.


var listUl = document.querySelectorAll('ul li');
var result = document.querySelector('.result');

// function countItems() {
//   var itemsNum = 0;
//   listUl.forEach(function (e) {
//     itemsNum++;
//   })
//   result.textContent = itemsNum;
// }
// var button = document.querySelector('button');
// button.addEventListener('click', countItems);


// 2 -shorter version:
function countItems() {
  result.textContent = listUl.length;
}

var button = document.querySelector('button');
button.addEventListener('click', countItems);
