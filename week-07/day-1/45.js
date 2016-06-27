'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

function shortestElement(names) {
  var shortest = names[0];
  for (var i = 0; i < names.length; i++) {
    if ((names[i]).length < shortest.length) {
      shortest = names[i];
    }
  }
  return shortest;
}

console.log(shortestElement(names));
