'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10];
// write your own sum function

function sum_numbers(inputList) {
  var summa = 0;
  for (var i = 0; i < inputList.length; i++) {
    summa += inputList[i];
  }
  return summa;
}
console.log(sum_numbers(numbers));
