var net = require('net');
var request = require('request');
var localStorage = require('localStorage');


const EVENT_AUTHENTICATION = 'authentication';
const EVENT_DATA = 'data';

var server = net.createServer(function (socket) {

    unverified_aquaponic_systems.push(socket);

    socket.on('data', function(data) {
        if(data.indexOf(EVENT_DATA) == 1) {
            //TODO: update on webapp and save in database
        }
        else if(data.indexOf(EVENT_AUTHENTICATION) == 1) {
            //TODO: verify authentication token
        }
    });


});
