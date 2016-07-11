// Create a webserver that can receive any request to any path. It should respond the path name,
// the request methos and the current time.
var http = require('http');
var server = http.createServer(function(req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  var today = new Date();
  res.end(req.url + ' ' + req.method + ' ' + today);
});


server.listen(3000, '127.0.0.1');
