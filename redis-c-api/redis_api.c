#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include "hiredis/hiredis.h"
#include "hiredis/async.h"
#include "hiredis/adapters/libevent.h"

/** REDIS CONFIGURATION **/
extern const char REDIS_HOSTNAME[] = "localhost";
extern const int REDIS_PORT = 6379;

/** TOPICS **/
extern const char TOPIC_ACTUATORS[] = "actuators";

/** AVAILABLE KEYS **/
extern const char SENSOR_TEMPERATURE[] = "temperature";
extern const char SENSOR_HUMIDITY[] = "humidity";
extern const char SENSOR_WATERLEVEL[] = "waterlevel";
//TODO: ADD SENSOR KEYS
extern const char ACTUATOR_LIGHTINTENSITY[] = "lightintensity";
extern const char ACTUATOR_LIGHTCOLOR[] = "lightcolor";
//TODO: ADD ACTUATOR KEYS

//################
//#     SYNC     #
//################

/**
 * Creates a connection to redis, which can send SET- or GET-commands.
 * Returns the context, which then may be passed as parameter to the commands.
**/
redisContext * create_connection() {
	//TODO: ERROR HANDLING
	return redisConnect(REDIS_HOSTNAME, REDIS_PORT);
}

/**
 * Disconnects, the given connection, from redis-server
**/
void disconnect_connection(redisContext *c) {
	//TODO: ERROR HANDLING
	redisFree(c);
}

/**
 * Sends a SET-Command through the given connection and stores the given data (key:value).
**/
void set (redisContext *c, const char key[], const char value[]) {
	//TODO: ERROR HANDLING
	redisCommand(c, "SET %s %s", key, value);
}

/**
 * Sends a GET-Command through the given connection and asks the value of the given key.
**/
const char * get (redisContext *c, const char key[]) {
	//TODO: ERROR HANDLING
	redisReply *reply = redisCommand(c, "GET %s", key);
	return reply->str;
}

//################
//#     ASYNC    #
//################

/**
 * Is executed after a message was received. Parses the message and returns the results as parameters to callback(key, value).
**/
void __on_message(redisAsyncContext *c, void *reply, void *privdata) {
    redisReply *r = reply;
    if (reply == NULL)
		return;

	if(r->element[2]->str == NULL) {
		void (*callback)(char*, char*) = privdata;
		char *key = strtok(r->element[2]->str, ":");;
		char *value = strtok(NULL, ":");
		callback(key, value);
	}
}

/**
 * Creates a connection to redis-server and subscribes to the given topic[param 1].
 * Executes the given callback[param 2] after a message was received.
 *
 * Callback[param 2]: callback (char key[], char value[]){...}
**/
redisAsyncContext * subscribe_to_topic (const char topic[], void* callback) {
	//signal(SIGPIPE, SIG_IGN);
	struct event_base *base = event_base_new();
	//establish connection to redis-server
	redisAsyncContext *ac = redisAsyncConnect(REDIS_HOSTNAME, REDIS_PORT);
	//error handler
	if (ac->err) {
		printf("error: %s\n", ac->errstr);
		return NULL;
	}
	redisLibeventAttach(ac, base);

	// Sends SUBSCRIBE-command with the given topic to redis
	redisAsyncCommand(ac, __on_message, callback, "SUBSCRIBE %s", topic);
	event_base_dispatch(base);
	return ac;
}

/**
 * Disconnects the given connection from redis-server.
**/
void disconnect_async_connection (redisAsyncContext *ac) {
	redisAsyncDisconnect(ac);
}


