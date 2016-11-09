var mongoose = require('mongoose'),
	Schema = mongoose.Schema

var Account = new Schema({
	username: String,
	password: String,
	email: String,
	firstName: String,
	lastName: String
});

module.exports = mongoose.model('Account',Account);