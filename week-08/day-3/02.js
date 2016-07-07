'use strict';

// create a function takes three parameters:
//  - fileName: the name of the file
//  - letter: a character
//  - cb: callback (with two parameters: error and the result)
//
// it should read the file and count the letters in the content
// and it should call the callback with the counted number
// if there is some error it should call the callback with the error
//

var fs = require('fs');

function countLetters(filename, letter, cb) {
  fs.readFile(filename, function (err, content) {
    if (err) {
      return cb(err);
    }
    var lettersList = String(content).split('');
    var letterNum = 0;
    lettersList.forEach(function (e) {
      if (e === letter) {
        letterNum ++;
      }
    });
    cb(null, letterNum);
  });
}

countLetters('korte.txt', 'a', function (err, letterNum) {
  console.log(letterNum);
});
