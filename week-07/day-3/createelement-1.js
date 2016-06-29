'use strict';

// Add an item that says 'The Green Fox' to the asteroid list.
// Add an item that says 'The Lamplighter' to the asteroid list.
// Add a heading saying 'I can add elements to the DOM!' to the .container.
// Add an image, any image, to the container.

var asteroidsUl = document.querySelector('.asteroids');

var newLi = document.createElement('li');
newLi.textContent = 'The Green Fox';
asteroidsUl.appendChild(newLi);

var newLi2 = document.createElement('li');
newLi2.textContent = 'The Lamplighter';
asteroidsUl.appendChild(newLi2);


var newH1 = document.createElement('h1');
newH1.textContent = 'I can add elements to the DOM!';
var container = document.querySelector('.container');
container.appendChild(newH1);

var picture = document.createElement('img');
picture.setAttribute('src', 'https://a1-images.myspacecdn.com/images03/28/ab870fd34c3e426584fd0b9e9b69423a/300x300.jpg');
container.appendChild(picture);
