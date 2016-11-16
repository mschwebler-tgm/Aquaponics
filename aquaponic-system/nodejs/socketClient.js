var net = require('net');
var request = require('requestify');
var REDISAPI = require('./redis_api');
var Redis = new REDISAPI();
//var localStorage = require('localStorage');


const EVENT_AUTHENTICATION = 'authentication';
const EVENT_DATA = 'data';

module.exports = function() {

	var client = new net.Socket();
	var redis_connection = Redis.createConnection();
	//TODO: INIT OF CLIENT EVENTS

	request.post('http://localhost:8080/authenticate', {
		username: "test",
		password: "test123"
	}).then(function (response) {
		var body = response.getBody();
		console.log(body);
		if (body.indexOf('ERROR') == -1) {
			console.log('AUTHENTICATED!!');
			client.connect(9090, "localhost", function () {
					console.log('Connected To Server');
				client.write(EVENT_AUTHENTICATION + '=' + body);
			});
			Redis.subscribe('system', function(channel, message) {
				Redis.getJSON(redis_connection, function(result) {
					console.log(result);
					client.write(EVENT_DATA + '=' + JSON.stringify(result));
				});
			});

		}
	});

}
