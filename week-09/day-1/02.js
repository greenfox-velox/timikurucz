// Create a webserver that can receive any request to any path. It should respond the path name,
// the request methos and the current time.
var express = require('express');
var app = express();


app.get('*', function(req, res) {
  var today = new Date();
  // console.log(req.path);
  // console.log(today);
  // console.log(req.method);
  res.send(req.path + ' ' + req.method + ' ' + today);
})

app.listen(3000);
