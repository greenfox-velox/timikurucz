'use strict';

var m = 'Apple';
// fill the m variable with its content 4 times
m = m + m + m + m;
console.log(m);

//second version:
m += m + m + m;
console.log(m);

//third:
m = m.repeat(4);
console.log(m);
