'use sttict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)

function minNumber(numbers) {
  var minNum = numbers[0];
  for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] < minNum) {
      minNum = numbers[i];
    }
  }
  return minNum;
}

console.log(minNumber(numbers));
