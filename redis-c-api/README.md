# REDIS C API
Include this API in your src-file, so you can access the functions and global variables.

```c
#include "redis_api.c"
```

## Requirements
The hiredis API of redis uses libevent. Install the library with:

    * apt-get install libevent-dev

After that run the following command in the redis-c-api folder:

    * make install


## Synchronous connection
To send HMSET and HGET commands to the REDIS-server, you have to use synchronous connections.

### Create a connection
The `create_connection` function creates a connection to the server and returns a `redisContext`, which stores the connection. The context is used to send HSET and HGET commands, which you can see in the following sections.

```c
//Creates a connection to localhost at port 6379
redisContext *context = create_connection("localhost", 6379);
```

### Send a HMSET command
The HMSET command stores multiple keys with values in the redis database to a hash key, which is internally set to 'system'.
To send a HMSET command you have to use the `set` function. The first parameter takes the context, which has to be created through `create_function`. The other one is taking the keys and values.

```c
// create a connection to redis
redisContext *context = create_function();
// use the context to send the set command
set(context, "key1 value1 key2 value2 key3 value3");
```

### Send a HGET command
The HGET command asks the database the value of the given key in hash key, which is internally set to 'system'.
To send a HGET command you have to use the `get` function.
The first parameter takes the context, which has to be created through `created_function`. The second parameter takes the key.
The function returns the value of the key as `char*`.

```c
// create a connection to redis
redisContext *context = create_function();
// use the context to send the get command
const char* temp = get(context, "key1");
```

### Disconnect
With the function `disconnect_connection` you can disconnect the given context from the redis server.

```c
// create a connection to redis
redisContext *context = create_function();
// disconnects from server
disconnect_connection(context);
```

## Asynchronous connection
The asynchronous connection is used to listen to changes of a topic.
E.g. if someone changes the color of the light (with the command `PUBLISH actuators lightcolor:red`) and you want to be notified, you have to subscribe to the topic `actuators`.

You can achieve this by using the function `subscribe_to_topic`, which takes two parameters. The first one takes the topic name, the second one takes a callback function, which will be called after a change was received.

The callback function should look like this:
```c
/**
 * The return type must be void!
 * The signature must be the same!
**/
void callback_example(const char key[], const char value[]) {
    printf("The %s was changed to %s", key, value);
}
```

To listen now to changes call the function `subscribe_to_topic` like this:
```c
// connects to redis and subscribes to TOPIC_ACTUATORS ("actuators")
// if a change was received, your callback function will be executed with the received parameters (key and value)
redisAsyncContext *ac = subscribe_to_topic(TOPIC_ACTUATORS, callback_example);
```
As you can see the function `subscribe_to_topic` creates, like the synchronous connection, a context. You can disconnect the connection at anytime you want by 'disconnect_async_connection', which takes the context as parameter.

```c
// disconnects the connection from redis
disconnect_async_connection(ac);
```

## Try the example
To try the example run 'make' in the redis-c-api folder and start the example by

    * ./example.out
