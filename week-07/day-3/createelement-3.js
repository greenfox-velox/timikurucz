'use strict';
// Remove the king from the list.
// Add list items that have the following text contents:
// ['apple', 'bubble', 'cat', 'green fox']

var parent = document.querySelector('.asteroids');
var child = parent.querySelector('li');
parent.removeChild(child);


var elementList = ['apple', 'bubble', 'cat', 'green fox'];
elementList.forEach(function (e) {
  var newLi = document.createElement('li');
  newLi.textContent = e;
  parent.appendChild(newLi);
});


//with for loop:

// for (var i = 0; i < elementList.length; i++) {
//   var newLi = document.createElement('li');
//   parent.appendChild(newLi);
//   newLi.innerHTML = elementList[i];
// }
