'use strict';
// Turn the party on and off by clicking the button.

function getThePartyStarted() {
  var button = document.querySelector('div');
  button.classList.toggle('party');
};

var button = document.querySelector('button');
button.addEventListener('click', getThePartyStarted);
