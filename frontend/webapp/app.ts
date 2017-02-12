import * as bodyParser from 'body-parser';
import * as express from 'express';
import * as logger from 'morgan';
import * as path from 'path';
import * as net from 'net';
import * as http from 'http';
import * as socketio from 'socket.io';
import * as mongoose from 'mongoose';

import * as network from './network';


export class Server {
	public static PORT = 8080;

	private app: express.Application;
	private httpServer: http.Server;
	private io: SocketIO.Server;

	// The relay will be used to connect the NETSocketServer with the S
	private relay: network.Relay;
	private authentication: network.Authentication;
	private socketServer: network.NETSocketServer;

	constructor() {
		this.app = express();
		this.httpServer = http.createServer(this.app);
		this.io = socketio.listen(this.server);

		this.initApplication();
		this.initRoutes();
		this.initMongoDB();

		this.relay = new network.Relay();
		this.authentication = new network.Authentication(this.io, this.app, this.relay);
		this.socketServer = new network.NETSocketServer(this.relay);

		this.app.listen(Server.PORT, () => {
			console.log('Example app listening on port ' + Server.PORT + '!');
		});
	}

	private initApplication() {
		//add public folder
		this.app.use(express.static(path.join(__dirname, 'public')));

		//template engine
		this.app.set('views', path.join(__dirname, 'views'));
		this.app.set('view engine', 'pug');
				
		// initializing SASS-preprocessor
		this.app.use(require('node-sass-middleware')({
			src: path.join(__dirname, 'public'),
			dest: path.join(__dirname, 'public'),
			indentedSyntax: true,
			sourceMap: true
		}));

		//mount logger
		this.app.use(logger("dev"));

		// catch 404 and forward to error handler
		this.app.use(function(err: any, req: express.Request, res: express.Response, next: express.NextFunction) {
			err.status = 404;
			next(err);
		});

		// uncomment after placing your favicon in /public
		//this.express.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
		this.app.use(bodyParser.json());
		this.app.use(bodyParser.urlencoded({extended: false}));
	}

	private initRoutes() {
		this.app.get('/', (req, res) => {
			res.render('index', {title: 'Express'});
		});
	}

	private initMongoDB() {
		// connect to database
		var dbConfig = require('./models/conf.js');
		mongoose.connect(dbConfig.url);
	}

	public getHTTPServer(): http.Server {
		return this.httpServer;
	}
}
