var Redis = require('ioredis');


module.exports = function() {
	/**
	 * Should not be used for 'SUBSCRIBE'-commands.
	 */
	this.createConnection = function () {
		return new Redis(6379, '192.168.0.16');
	}

	/**
	 * After receving a reply from redis, by HGETALL, the reply ['k1', 'v1', 'k2', 'v2'] will
	 * be transformed into { k1: 'v1', 'k2': 'v2' }
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

	this.getJSON = function (connection, callback) {
		connection.hgetall('system').then(function (result) {
			callback(result);
		});
	}

	/**
	 *
	 * @param key
	 * @param value
	 */
	this.publish = function (key, value) {

	}

	/**
	 * Subscribes to given topic and executes callback if message was received.
	 * Returns connection.
	 * @param topic
	 * @param callback function(channel, message)
	 */
	this.subscribe = function (topic, callback) {
		var connection = this.createConnection();
		connection.subscribe(topic);
		connection.on('message', callback);
		return connection;
	}
}
