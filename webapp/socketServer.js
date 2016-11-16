var net = require('net');

const EVENT_AUTHENTICATION = 'authentication';
const EVENT_DATA = 'data';

module.exports = function(linker, authentication) {
	var server = net.createServer(function (socket) {

		//TODO: SET TIMEOUT AND DISABLED IT AFTER SUCCESSFUL AUTHENTICATION

		socket.on('data', function (data) {
			console.log('DATA EVENT FIRED');
			data = "" + data;
			if (data.indexOf(EVENT_DATA) != -1) {
				//TODO: SAVE IN DATABASE (STATISTICS)
				var json = data.substring(data.indexOf('=')+1);
				console.log("CLIENT: " + socket._id + "\nSAYS: " + json);
				if(socket._id != undefined) {
					//linker.publishToIOClient(socket._id, json);
				}
			}
			else if (data.indexOf(EVENT_AUTHENTICATION) != -1) {
				var token = data.substring(data.indexOf('=')+1);
				authentication.verifyToken( token, function(decodedToken) {
					//TODO: DISABLE TIMEOUT
					console.log('CLIENT AUTHENTICATED WITH ID: ' + decodedToken._id);
					socket._id = decodedToken.id;
					console.log('SOCKET ID SET TO ' + socket._id);
					linker.addNETClient(decodedToken._id, socket);
				});
			}
		});


	});

	server.listen(9090, "localhost");
}
