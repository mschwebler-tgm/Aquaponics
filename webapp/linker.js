function Linker () {
    this.IOCLIENTS = {};
    this.NETCLIENTS = {};
}

Linker.prototype.addIOClient = function(id, object) {
    this.IOCLIENTS.add(id,object);
}

Linker.prototype.removeIOClient = function(id) {
    this.IOCLIENTS.remove(id);
}

Linker.prototype.addNETClient = function(id, object) {
    this.NETCLIENTS.add(id,object);
}

Linker.prototype.removeNETClient = function(id) {
    this.NETCLIENTS.remove(id);
}

Linker.prototype.publishToNETClient = function(id, key, value) {
    NETCLIENTS.id.write(key+ ':' + value);
}

Linker.prototype.publishToIOClient = function(id, json) {
    IOCLIENTS.id.emit('updateJSON', json);
}