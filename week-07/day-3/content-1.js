'use strict';


  // 1. Alert the content of the header.
  // 2. Write the content of the first paragraph to the console.
  // 3. Alert the content of the second paragraph.
  // 4. Replace the heading's content with 'New content'.
  // 5. Replace the last paragraph's content with the first paragraph's content.


//1:
var h1Text = document.querySelector('h1');
alert(h1Text.innerHTML);

// //1-refactor:
// alert((document.querySelector('h1')).innerHTML);

//2:
var contentOfFirstP = document.querySelector('p');
console.log(contentOfFirstP);

//2-2:
var contentOfFirstP = document.querySelector('p:first-of-type');
console.log(contentOfFirstP);

//3:
var contentOf2P = document.querySelector(':nth-child(3)');
alert(contentOf2P);

//3-2:
var contentOf2P = document.querySelector('.other');
alert(contentOf2P);

// 4. Replace the heading's content with 'New content'.
var h1Text = document.querySelector('h1');
h1Text.textContent = 'New content';

// 5. Replace the last paragraph's content with the first paragraph's content.
var contentOfLastP = document.querySelector('.result');
contentOfLastP.textContent = contentOfFirstP.textContent;
