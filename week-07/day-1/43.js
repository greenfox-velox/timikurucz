'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function grabOddNumbers(numbers) {
  var odd_numbers = [];
  for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
      odd_numbers.push(numbers[i]);
    }
  }
  return odd_numbers;
}

console.log(grabOddNumbers(numbers));
