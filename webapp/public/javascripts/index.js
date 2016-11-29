var socket;

function statusError() {
    var status = $('#status');
    status.addClass('error').css('opacity','1').delay(500).queue(function() {
        status.css('opacity', '0').delay(500).queue(function() {
            status.removeClass('error');
            $(this).dequeue();
        });
        $(this).dequeue();
    });
}

function statusSuccess() {
    var status = $('#status');
    status.addClass('success').css('opacity','1').delay(500).queue(function() {
        status.css('opacity', '0').delay(500).queue(function() {
            status.removeClass('success');
            $(this).dequeue();
        });
        $(this).dequeue();
    });
}

$(document).ready(function () {

    $('#login-panel').addClass('open');

    socket = io.connect('http://127.0.0.1:8080', {
        query: 'token=' + localStorage.getItem('jwt')
    });

    socket.on('login-failure', function (data) {

        if($('#login-panel').hasClass('error')) {
            $('#login-panel').removeClass('error');
        }
        $('#login-panel').delay(100).queue(function() {
            $('#login-panel').addClass('error');
            $('#login-panel').dequeue();
        });
        console.log(data.message);
        statusError();
        console.log('login failure');
    });

    socket.on('login-success', function () {
        statusSuccess();
        console.log('login success!!');
    });

    socket.on('register-failure', function (data) {
        if($('#register-panel').hasClass('error')) {
            $('#register-panel').removeClass('error');
        }
        $('#register-panel').addClass('error');
        console.log(data.message);
        statusError();
        console.log('register failure');
    });

    socket.on('register-success', function () {
        statusSuccess();
        console.log('register success!!');
    });

    socket.on('jwt', function (data) {
        localStorage.setItem('jwt', data.token);
    });

    socket.on('updateJSON', function (json) {
        console.log('json updated');
v    });

    socket.on('authorization-failure', function (data) {
        console.log('authorization-failure');
    });

    $('#open-register-screen').on('click', function() {
        $('#register-panel').addClass('open');
        $('#register-screen').css({
            'z-index': '10',
            'opacity': '1',
            'transform': 'scale(1)'
        });
    });

    $('#close-register-screen').on('click', function() {
        $('#register-screen').css({
            'opacity': '0',
            'transform': 'scale(1.03)'
        }).delay(1000).queue(function() {
            $('#register-screen').css('z-index','-10');
            $('#register-panel').removeClass('open');
            $(this).dequeue();
        });
    });

    $('#register').on('click', function () {
        console.log('click');
        socket.emit('register', $('#register-email').val(), $('#register-password').val());
    });

    $('#login').on('click', function () {
        console.log('click');
        socket.emit('login', $('#login-email').val(), $('#login-password').val());
    });
});