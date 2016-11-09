var jwt = require('jsonwebtoken');
var bCrypt = require('bcrypt-nodejs');
var Account = require('./models/account');

module.exports = function(io){


	io.use(function(socket, next) {
		console.log(socket.handshake.query.token);
		jwt.verify(socket.handshake.query.token, 'secretKey', function(err, decoded) {
			console.log(decoded);
			if (err || decoded == null) {
				io.emit('error', 'Unauthorized.');
				return next();
			}
			return next();
		});
	});

	io.sockets.on('connection', function(socket) {
		socket.on('register', function(username, password, email, firstName, lastName) {
			// trying to find account with provided username in database
			Account.findOne({ 'username' :  username }, function(err, user) {
				// catches errors of database
				if (err) {
					socket.emit('error', 'Database error.');
					return;
				}
				// checks if user already exists
				if (user) {
					socket.emit('error', 'Account already exists.');
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
							socket.emit('error', 'Couldn\'t save account in the database');
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
						socket.emit('error', 'Database error.');
						return;
					}
					// wrong username or password => account doesn't exists or password was wrong
					else if (!user || !checkPassword(account, password)) {
						socket.emit('error', 'Username or Password wrong.');
						return;
					}
					io.emit('success');
					jwt.sign({id: account._id, username: account.username}, 'secretKey', function(err, token) {
						socket.emit('jwt', token);
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