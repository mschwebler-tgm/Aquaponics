import * as mongoose from 'mongoose'

// ############################

export interface IAccount extends mongoose.Document{
	username: string;
	password: string;
	email: string;
	firstName: string;
	lastName: string;
}

// must be the same

var SAccount = new mongoose.Schema({
	username: String,
	password: String,
	email: String,
	firstName: String,
	lastName: String
});

export var Account = mongoose.model<IAccount>('Account', SAccount);

// ###########################
