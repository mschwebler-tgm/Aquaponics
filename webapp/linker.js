var IOCLIENTS = {};
var NETCLIENTS = {};

var publishToNET = function(id, key, value) {
	NETCLIENTS.id.write(key+ ':' + value);
}

var publishToIO = function(id, json) {
	IOCLIENTS.id.emit('updateJSON', json);
}