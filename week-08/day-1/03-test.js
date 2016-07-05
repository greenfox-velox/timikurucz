'use strict';

var rectangle = require('./03');
var tape = require('tape');

var square = new rectangle.Rectangle(4, 4);

tape(function(t) {
  t.deepEqual(square.getArea(), 16);
  t.deepEqual(square.getCircumference(), 16);
  t.deepEqual(square.a, 4);
  t.deepEqual(square.b, 4);
  t.end();

});
