'use strict';

var numbers = [2, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function isPrime(inputArray) {
  return inputArray.every(function (e) {
    if (e < 2) {
      return false;
    }
    for (var i = 3; i < e; i++) {
      if (e % i === 0) {
        return false;
      }
    }
    return true;
  });
}

console.log(isPrime(numbers));
