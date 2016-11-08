var net = require('net');

var verified_aquaponic_systems = [];
var unverified_aquaponic_systems = [];

const EVENT_AUTHENTIFICATION = 'authentification';
const EVENT_DATA = 'data';

var server = net.createServer(function (socket) {

    unverified_aquaponic_systems.push(socket):

    socket.on('data', function(data) {
        if(data.indexOf(EVENT_DATA) == 1) {
            //TODO: update on webapp and save in database
        }
        else if(data.indexOf(EVENT_AUTHENTIFICATION) == 1) {
            //TODO: verify authentification token
        }
    });


});
