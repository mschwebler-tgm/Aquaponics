import * as net from 'net';

//NETSocket
//######################################################
export namespace NETTypes {
    /**
     * Data types, which will be send over the NETSocket connection (Server <=> Client).
     */
    export enum DataType {
        AUTHENTICATION = 100,
        JSON = 200
    }

    export interface Client extends net.Socket{
        readonly token: string;
    }
}
//#######################################################

//Socket.io
//#######################################################
export namespace IOTypes {

    export interface Client extends SocketIO.Client {
        readonly token: string;
    }

    export interface register {
        firstName: string;
        lastName: string;
        username: string;
        email: string;
        password: string;
    }

    export interface login {
        email: string;
        password: string;
    }

    export interface jsonData {
        data: Object;
    }
}
//#######################################################