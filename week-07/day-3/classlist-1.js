'use strict';
// Does cat have a cat class?
// If so, alert 'YEAH CAT!'

// If dolphin has a 'dolphin' class, replace apple's content with 'pear'

// If apple has an 'apple' class, replace cat's content with 'dog'

// Make apple red
// Make balloon less balloon-like
var allP = document.querySelectorAll('p');

allP.forEach(function (e) {
  if (e.textContent === 'cat' && e.classList.contains('cat')) {
    alert('YEAH CAT!');
  }
});

var apple = document.querySelector('.apple');
allP.forEach(function (e) {
  if (e.textContent === 'dolphin' && e.classList.contains('dolphin')) {
    apple.textContent = 'pear';
  }
});

var cat = document.querySelector('.cat');
allP.forEach(function (e) {
  if (e.textContent === 'apple' && e.classList.contains('apple')) {
    cat.textContent = 'dog';
  }
});

apple.classList.add('red');

var balloon = document.querySelector('.balloon');
balloon.classList.remove('balloon');
