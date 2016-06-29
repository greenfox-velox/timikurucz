'use strict';

  // fill output1 with the first paragraph's content, text only.
  // fill output2 with the first paragraph's content keeping the cat strong.

var firstP = document.querySelector('p:first-of-type');
var secondP = document.querySelector('.output1');
var thirdP = document.querySelector('.output2');
secondP.textContent = firstP.textContent;
thirdP.innerHTML = firstP.innerHTML;
