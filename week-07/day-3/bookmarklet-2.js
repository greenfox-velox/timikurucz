'use strict';
// Create a script that replaces every image
// with this: http://bit.ly/lpgreenfox
// Create a bookmarklet that does that on any website.

var photoList = document.querySelectorAll('img');

photoList.forEach(function (e) {
  e.setAttribute('src', 'https://s-media-cache-ak0.pinimg.com/736x/aa/00/40/aa0040a22096c2fc2d35a91b5fad1d04.jpg');
});
