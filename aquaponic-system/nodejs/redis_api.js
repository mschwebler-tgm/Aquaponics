var ioredis = require('ioredis');
var redis = new Redis();

/**
 * After receving a reply from redis, by HGETALL, the reply ( ['k1', 'v1', 'k2', 'v2'] ) will
 * be transformed into a JSON array ( { k1: 'v1', 'k2': 'v2' } )
 */
Redis.Command.setReplyTransformer('hgetall', function (result) {
	if (Array.isArray(result)) {
		var obj = {};
		for (var i = 0; i < result.length; i += 2) {
			obj[result[i]] = result[i + 1];
		}
		return obj;
	}
	return result;
});

function set(key, value) {

}

function getJSON(callback) {

}

function publish(key, value) {

}

function subscribe(topic, callback) {

}