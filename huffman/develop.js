/* NODE.JS */

var http = require("http");

http.createServer(function (req, res) {
  //Send the HTTP header
  //HTTP status : 200 : OK
  //Content type : text/plain
  res.writeHead(200, {'Content-Type': 'text/plain'});
  
  //Send the response body - a message 'hello world'
  res.end('Hello World\n');
}).listen(8081);

console.log('Server running at 127.0.0.1:8081 http');

