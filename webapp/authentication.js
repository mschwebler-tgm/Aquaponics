var jwt = require('jsonwebtoken');
var bCrypt = require('bcrypt-nodejs');
var Account = require('./models/account');

module.exports = function(io, app){

	// compares the provided password with the encrypted password
	this.checkPassword = function(account, password){
		return bCrypt.compareSync(password, account.password);
	}

	function checkPassword(account, password){
		return bCrypt.compareSync(password, account.password);
	}

	// generates hash using bCrypt
	this.generateHash = function(password){
		return bCrypt.hashSync(password, bCrypt.genSaltSync(10), null);
	}

	function generateHash(password){
		return bCrypt.hashSync(password, bCrypt.genSaltSync(10), null);
	}

	this.verifyToken = function(token, callback) {
		jwt.verify(token, 'secretKey', function(err, decoded) {
			console.log(decoded);
			if (err || decoded == null) {
				return;
			}
			callback(decoded);
		});
	}

	function verifyToken(token, callback) {
		jwt.verify(socket.handshake.query.token, 'secretKey', function(err, decoded) {
			console.log(decoded);
			if (err || decoded == null) {
				return;
			}
			callback(decoded);
		});
	}

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
					});
				}
			});
		});

		socket.on('login', function(username, password) {
			//TODO: DELETE THIS CODELINE AFTER YOU SHOWED TO MR. ALAVARO

			// trying to find account with provided username in database
			Account.findOne({'username': username}, function (err, account) {
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

		/**
		 * Will be used from aquaponic-system to get token.
		 */
		app.post('/authenticate', function(req, res) {
			var username = req.body.username;
			var password = req.body.password;
			console.log("SYSTEM FOUND");
			console.log(username);
			console.log(password);
			// trying to find account with provided username in database
			Account.findOne(
				{'username': username},
				function (err, account) {
					// catch errors of database
					if (err) {
						//DATABASE ERROR
						res.send('ERROR: Database error.');
						return;
					}
					// wrong username or password => account doesn't exists or password was wrong
					else if (!account || !checkPassword(account, password)) {
						res.send('ERROR: Username or Password wrong.')
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


}