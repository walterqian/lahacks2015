var express = require('express');
var app = express();
var http = require('http').Server(app);
var port = process.env.PORT || 8080;
//var stream = twit.stream('statuses/filter', { locations: world });

app.use(express.static(__dirname + '/public'));

app.get('/', function(req, res){
	console.log("request for index.html");
	res.sendFile(__dirname + '/index.html');
});

app.get('/map', function(req, res){
	console.log("request for map.html");
	res.sendFile(__dirname + '/map.html');
});

http.listen(port, function(){
	console.log("listening on port " + port);
});