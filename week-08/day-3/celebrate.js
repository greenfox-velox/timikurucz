'use strict';

var xhr = new XMLHttpRequest();
var h1 = document.querySelector('h1');
var h2 = document.querySelector('h2');

function getRequest (event) {
  xhr.onload = function() {
    h1.textContent = JSON.parse(xhr.response).weekday;
    h2.textContent = (JSON.parse(xhr.response).celebrations).length;
    };
  xhr.open('GET', 'http://calapi.inadiutorium.cz/api/v0/en/calendars/default/2016/7/06');
  xhr.send();
}

var button = document.querySelector('.button1');
button.addEventListener('click', function(){
  getRequest();
  });
