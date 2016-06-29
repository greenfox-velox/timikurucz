'use strict';

// replace the list items' content with items from this list:
// ['apple', 'banana', 'cat', 'dog']

var allLi = document.querySelectorAll('li');
var newElementsList = ['apple', 'banana', 'cat', 'dog'];

// with forEach:
allLi.forEach(function(e, i) {
  e.innerHTML = newElementsList[i];
})

// with for loop:
for (var i = 0; i < allLi.length; i++) {
 allLi[i].textContent = newElementsList[i]
}
