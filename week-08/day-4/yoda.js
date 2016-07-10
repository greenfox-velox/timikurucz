'use strict';

var h1 = document.querySelector('h1');
var inputField = document.querySelector('.input-text');
var button = document.querySelector('.button');


// button.addEventListener('click', function(){
//   h1.textContent = inputField.value;
//   console.log(inputField.value);
// });



function getYodaSentence () {
  var xhr = new XMLHttpRequest();
  debugger;
  var host = 'https://yoda.p.mashape.com/yoda';
  var text = encodeURIComponent(inputField.value);
  var urlToSend = host + '?sentence=' + text;
  var accessToken = "92lgHzFLWDmsh8q0bMWy4VVGmfayp1oPR3gjsnRDHDH0Yo8JAr";

  xhr.open('GET', urlToSend);
  xhr.setRequestHeader('X-Mashape-Key', accessToken);
  xhr.onload = function() {
    h1.textContent = xhr.response;
    };
  xhr.send();
}

button.addEventListener('click', getYodaSentence);
