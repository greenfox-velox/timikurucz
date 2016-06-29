'use strict';
// Create a script that replaces every h1 headline's content
// with 'Green Fox Academy Conquers the World'.
// Create a bookmarklet that does that on any website.

var allH1 = document.querySelectorAll('h1');

allH1.forEach(function (e) {
  e.textContent = 'Green Fox Academy Conquers the World';
});
