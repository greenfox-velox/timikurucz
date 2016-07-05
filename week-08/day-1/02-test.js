'use strict';

var countBooks = require('./02');
var tape = require('tape');

tape (function(t) {
  t.deepEqual(countBooks.studentsBooks(countBooks.students), 4);
  t.end();
});
