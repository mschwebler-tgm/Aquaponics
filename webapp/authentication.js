var jwt = require('jsonwebtoken');
var bCrypt = require('bcrypt-nodejs');
var Account = require('./models/account');

module.exports = function(io, app){

    io.use(function(socket, next) {
        console.log(socket.handshake.query.token);
        jwt.verify(socket.handshake.query.token, 'secretKey', function(err, decoded) {
            console.log(decoded);
            if (err || decoded == null) {
                socket.emit('failure', {message: 'Unauthorized.'});
                return next();
            }
            return next();
        });
    });

    io.sockets.on('connection', function(socket) {
        console.log(socket.handshake.query.token);
        socket.on('register', function(username, password, email, firstName, lastName) {
            // trying to find account with provided username in database
            Account.findOne({ 'username' :  username }, function(err, user) {
                // catches errors of database
                if (err) {
                    socket.emit('failure', {message: 'Database error.'});
                    return;
                }
                // checks if user already exists
                if (user) {
                    socket.emit('failure', {message: 'Account already exists.'});
                } else {
                    // if there is no user with that email
                    // create the user
                    var newAccount = new Account();

                    // sets account's data
                    newAccount.username = username;
                    newAccount.password = generateHash(password);
                    newAccount.email = email;
                    newAccount.firstName = firstName;
                    newAccount.lastName = lastName;

                    // saves the account in the database
                    newAccount.save(function(err) {
                        if (err){
                            socket.emit('failure', {message: 'Couldn\'t save account in the database'});
                            return;
                        }
                        socket.emit('success');
                        return;
                    });
                }
            });
        });

        socket.on('login', function(username, password) {
            // trying to find account with provided username in database
            Account.findOne(
                {'username': username},
                function (err, account) {
                    // catch errors of database
                    if (err) {
                        socket.emit('failure', {message: 'Database error.'});
                        return;
                    }
                    // wrong username or password => account doesn't exists or password was wrong
                    else if (!account || !checkPassword(account, password)) {
                        socket.emit('failure', {message: 'Username or Password wrong.'});
                        return;
                    }
                    io.emit('success');
                    jwt.sign({id: account._id, username: account.username}, 'secretKey', {algorithm: 'HS256'}, function(err, token) {
                        socket.emit('jwt', {token: token});
                    });
                }
            );
        });

        app.post('/authenticate', function(req, res) {
            var username = req.body.username;
            var password = req.body.password;

            // trying to find account with provided username in database
            Account.findOne(
                {'username': username},
                function (err, account) {
                    // catch errors of database
                    if (err) {
                        res.send('Database error.');
                        return;
                    }
                    // wrong username or password => account doesn't exists or password was wrong
                    else if (!account || !checkPassword(account, password)) {
                        socket.emit('failure', {message: 'Username or Password wrong.'});
                        return;
                    }
                    io.emit('success');
                    jwt.sign({id: account._id, username: account.username}, 'secretKey', {algorithm: 'HS256'}, function(err, token) {
                        res.send(token);
                    });
                }
            );
        });
    });

    // compares the provided password with the encrypted password
    var checkPassword = function(account, password){
        return bCrypt.compareSync(password, account.password);
    }

    // generates hash using bCrypt
    var generateHash = function(password){
        return bCrypt.hashSync(password, bCrypt.genSaltSync(10), null);
    }

}