'use strict';

// create a function that returns it's input factorial

function factorial(number) {
  var factor = 1;
  for (var loop = 1; loop < number + 1; loop++) {
    factor *= loop;
  }
  return factor;
}

console.log(factorial(5));
