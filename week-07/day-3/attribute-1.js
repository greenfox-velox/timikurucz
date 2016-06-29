'use strict';
// Write the image's url to the console.
// Replace the image with a picture of yourself.
// Make the link point to the Green Fox Academy website.
// Disable the second button.
// Replace its text with 'Don't click me!'.

var photo = document.querySelector('img');
var photoSrc = photo.getAttribute('src');
console.log(photoSrc);

photo.setAttribute('src', 'https://a1-images.myspacecdn.com/images03/28/ab870fd34c3e426584fd0b9e9b69423a/300x300.jpg');

var linkPoint = document.querySelector('a');
linkPoint.setAttribute('href', 'http://www.greenfoxacademy.com/');

var button2 = document.querySelector('.this-one');
button2.disabled = true;

button2.textContent = "Don't click me!";
