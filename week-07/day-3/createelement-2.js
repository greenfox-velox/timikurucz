'use strict';

// Remove the king from the list.
// Add 3 list items saying 'The Fox' to the list.

var parent = document.querySelector('.asteroids');
var child = parent.querySelector('li');
parent.removeChild(child);

var newLi = document.createElement('li');
newLi.textContent = 'The Fox';
parent.appendChild(newLi);

var newLi2 = document.createElement('li');
newLi2.textContent = 'The Fox';
parent.appendChild(newLi2);

var newLi3 = document.createElement('li');
newLi3.textContent = 'The Fox';
parent.appendChild(newLi3);
