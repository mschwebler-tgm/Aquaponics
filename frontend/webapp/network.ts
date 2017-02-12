import * as types from './types';

/* RELAY AND NETSOCKETSERVER */
import * as net from 'net'

/* AUTHENTICATION */
import * as jwt from 'jsonwebtoken'
import * as bcrypt from 'bcrypt-nodejs'
import * as Database from './models/database'
import * as express from "express"


declare namespace Relay {
    interface IOSocket extends SocketIO.Client {
        _id: number;
    }

    interface NETSocket extends net.Socket {
        _id: number;
    }
}


export class Relay {
    
    private IOCLIENTS: Object;
    private NETCLIENTS: Object;
    
    constructor() {
        this.IOCLIENTS = {};
        this.NETCLIENTS = {};
    }

    public addIOClient(id: string, client: Relay.IOSocket) {
        this.IOCLIENTS[id] = client;
    }

    public removeIOClient(id: string) {
        delete this.IOCLIENTS[id];
    }

    public publishIOClient(id: string, json: Object) {
        this.IOCLIENTS[id].emit('updateJSON', json);
    }

    public addNETClient(id: string, client: Relay.NETSocket) {
        this.NETCLIENTS[id] = client;
    }

    public removeNETClient(id: string) {
        delete this.NETCLIENTS[id];
    }

    public publishNETClient(id: string, json: Object) {
        this.NETCLIENTS[id].emit('updateJSON', json);
    }

}


export class Authentication {

    private io: SocketIO.Server;
    private app: express.Express;
    private relay: Relay;

    //TODO: change the following secretKey to a secure one
    private static secretKey: string = 'secretKey';

    constructor(io: SocketIO.Server, app: express.Application, relay: Relay) {
        this.io = io;
        this.app = app;
        this.relay = relay;
 
        this.initIO();
        this.initApplication();
    }

    /**
     * Initializes the Express middleware for authentication from the aquaponic-system.
     */
    private initApplication () {
        /**
         * Will be used from aquaponic-system to get authentication token (JWT).
         */
        this.app.post('/authenticate', (req, res) => {
            var username = req.body.username;
            var password = req.body.password;
            console.log("SYSTEM FOUND");
            console.log(username);
            console.log(password);
            // trying to find account with provided username in database
            Database.Account.findOne({'username': username}, (err, account) => {
                    // catch errors of database
                    if (err) {
                        //DATABASE ERROR
                        res.send('ERROR: Database error.');
                        return;
                    }
                    // wrong username or password => account doesn't exists or password was wrong
                    else if (!account || !Authentication.checkPassword(account, password)) {
                        res.send('ERROR: Username or Password wrong.')
                        return;
                    }
                    //success
                    jwt.sign({id: account._id, username: account.username}, 'secretKey', {algorithm: 'HS256'}, function(err, token) {
                        res.send(token);
                    });
                }
            );
        });
    }

    /**
     * Initializes SocketIO server with the properties of the authentication class.
     */
    private initIO () {
        //before the 'connection'-event this following function will be called if someone connects to the server
        this.io.use((socket: any, next) => {
            //TODO: test if this casting works
            socket = socket as types.IOTypes.Client;
            jwt.verify(socket.handshake.query.token, Authentication.secretKey, (err, decoded) => {
                if(err || decoded == null) {
                    socket.emit('authorization-failure', {message: 'Unauthorized.'});
                    return next();
                }
                //TODO: DELETE THIS CODELINE AFTER YOU SHOWED TO MR. ALAVARO
                socket._id = decoded.id;
                this.relay.addIOClient(decoded.id, socket);
                return next();
            });
        });

        //initialization of socketIO events
        this.io.sockets.on('connection', (socket: any) => {

            //register event
            socket.on('register', (data: types.IOTypes.register) => {
                // trying to find account with provided username in database
                Database.Account.findOne({ 'email' :  data.username }, (err, user) => {
                    // catches errors of database
                    if (err) {
                        socket.emit('register-failure', {message: 'Database error.'});
                        return;
                    }
                    // checks if account already exists
                    if (user) {
                        socket.emit('register-failure', {message: 'Account already exists.'});
                    } else {
                        // if there is no user with that email
                        // create a new account
                        var newAccount = new Database.Account();
                        
                        // sets data of the new account
                        newAccount.username = data.username;
                        newAccount.password = Authentication.generateHash(data.password);
                        newAccount.email = data.email;
                        newAccount.firstName = data.firstName;
                        newAccount.lastName = data.lastName;

                        // saves the account in the database
                        newAccount.save(function(err) {
                            if (err){
                                socket.emit('register-failure', {message: 'Couldn\'t save account in the database'});
                                return;
                            }
                            socket.emit('register-success');
                        });
                    }
                });
            });

            //login event
            socket.on('login', (data) => {
                // trying to find account with provided username in database
                Database.Account.findOne({'email': data.email}, (err, account) => {
                    // catch errors of database
                    if (err) {
                        socket.emit('login-failure', {message: 'Database error.'});
                        return;
                    }
                    // wrong username or password => account doesn't exists or password was wrong
                    else if (!account || !Authentication.checkPassword(account, data.password)) {
                        socket.emit('login-failure', {message: 'Username or Password wrong.'});
                        return;
                    }
                    socket.emit('login-success');
                    jwt.sign({id: account._id, username: account.username}, 'secretKey', {algorithm: 'HS256'}, function(err, token) {
                        socket.emit('jwt', {token: token});
                        socket = socket as types.IOTypes.Client;
                        //TODO: DELETE THE FOLLOWING CODELINE AFTER YOU SHOWED TO MR. ALVARO
                        socket._id = account._id;
                        //add SocketIO client to relay
                        this.relay.addIOClient(account._id, socket);
                    });
                });
            });
        });
    }

    /**
     * Checks if the password (hash) in the given account object is equal to the given password (plain).
     * @returns boolean of the result
     */
    public static checkPassword(account: Database.IAccount, password: string): boolean {
        return bcrypt.compareSync(account.password, password);
    }

    /**
     * Generates a hash from the given password and returns it.
     * @returns generated hash
     */
    public static generateHash(password: string): string {
        return bcrypt.hashSync(password, bcrypt.genSaltSync(10));
    }

    /**
     * Verifies if token is valid, if so the given callback will be executed.
     */
    public static verifyToken(token: string, callback: Function) {
        jwt.verify(token, this.secretKey, (err, decoded) => {
            if(err || decoded == null) {
                return;
            }
            callback(decoded);
        });
    }

}

export class NETSocketServer {

    private server: net.Server;
    private relay: Relay;

    constructor(relay: Relay) {
        this.relay = relay;


        this.initServer();

        this.server.listen(9090, 'localhost');
    }

    /**
     * Initialize server data-event.
     */
    private initServer() {
        this.server = net.createServer((socket: any) => {
            //TODO: set timeout and disable it after successful authentication
            socket.on('data', (rawdata) => {
                console.log('DATA EVENT FIRED');
                var data = rawdata.toString();
                socket = socket as types.NETTypes.Client;
                if (data.indexOf(types.NETTypes.DataType.JSON) != -1) {
                    //TODO: SAVE IN DATABASE (STATISTICS)
                    var json = data.substring(data.indexOf('=')+1);
                    console.log("CLIENT: " + socket._id + "\nSAYS: " + json);
                    if(socket._id != undefined) {
                        this.relay.publishIOClient(socket._id, json);
                    }
                }
                else if (data.indexOf(types.NETTypes.DataType.AUTHENTICATION) != -1) {
                    var token = data.substring(data.indexOf('=')+1);
                    Authentication.verifyToken( token, function(decodedToken) {
                        //TODO: DISABLE TIMEOUT
                        console.log('CLIENT AUTHENTICATED WITH ID: ' + decodedToken._id);
                        socket._id = decodedToken.id;
                        console.log('SOCKET ID SET TO ' + socket._id);
                        this.relay.addNETClient(decodedToken._id, socket);
                    });
                }
            });
        });
    }


}