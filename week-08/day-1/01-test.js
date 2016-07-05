'use strict';

var countLetters = require('./01');
var tape = require('tape');

tape (function (t) {
  t.deepEqual(countLetters.newLetterCounter('apple'), { a: 1, p: 2, l: 1, e: 1 });
  t.end();
});
