function Linker () {
    this.IOCLIENTS = {};
    this.NETCLIENTS = {};
}

Linker.prototype.addIOClient = function(id, object) {
    this.IOCLIENTS[id] = object;
}

Linker.prototype.removeIOClient = function(id) {
    delete this.IOCLIENTS[id];
}

Linker.prototype.addNETClient = function(id, object) {
    this.NETCLIENTS[id] = object;
}

Linker.prototype.removeNETClient = function(id) {
    delete this.NETCLIENTS[id];
}

Linker.prototype.publishToNETClient = function(id, key, value) {
    //TODO: CHECK IF CONNECTION IS AVAILABLE
    this.NETCLIENTS[id].write(key+ ':' + value);
}

Linker.prototype.publishToIOClient = function(id, json) {
    //TODO: CHECK IF CONNECTION IS AVAILABLE
    this.IOCLIENTS[id].emit('updateJSON', json);
}

module.exports = new Linker();