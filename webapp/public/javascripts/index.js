var socket;

$(document).ready(function () {
    socket = io.connect('http://127.0.0.1:8080', {
        query: 'token=' + localStorage.getItem('jwt')
    });

    socket.on('failure', function (data) {
        console.log(data.message);
    });

    socket.on('success', function () {
        console.log('success!!');
    });

    socket.on('jwt', function (data) {
        localStorage.setItem('jwt', data.token);
    });

    socket.on('updateJSON', function (json) {
        console.log('json updated');
        var json = JSON.parse(json);
        console.log(json);
        $('#temperature').text("" + json.temperature);
    });

    $('#register').on('click', function () {
        console.log('click');
        socket.emit('register', $('#username').val(), $('#password').val());
    });

    $('#login').on('click', function () {
        console.log('click');
        socket.emit('login', $('#username').val(), $('#password').val());
    });
});