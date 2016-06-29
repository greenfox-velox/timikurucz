'use strict';

// fill every paragraph with the last one's content.
var LastP = document.querySelector('.dog');
var allP = document.querySelectorAll('p');
allP.forEach(function(e) {
  e.textContent = LastP.textContent;
})
