function Redis_API() {
    this.ioredis = require('ioredis');
    this.redis = new Redis();
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

function getJSON(callback) {
    redis.hgetall('system');
    redis.exec(function(err, result) {
       callback(result);
    });
}

function publish(key, value) {

}

function subscribe(topic, callback) {
    redis.subscribe(topic);
    redis.on('message', callback);
}
