# REDIS C API
Include this API in your src-file, so you can access the functions and global variables.

```c
#include "redis_api.c"
```

## Requirements
The hiredis API of redis uses libevent. Install the library with:

    * apt-get install libevent-dev

## Synchronous connection
To send SET and GET commands to the REDIS-server, you have to use synchronous connections.

### Create a connection
The `create_connection` function creates a connection to the server and returns a `redisContext`, which stores the connection. The context is used to send SET and GET commands, which you can see in the following sections.

```c
redisContext *context = create_connection();
```

### Send a SET command
The SET command stores a key with a value in the redis database.
To send a SET command you have to use the `set` function. The first parameter takes the context, which has to be created through `create_function`. The other two parameters are taking the key and value.

```c
// create a connection to redis
redisContext *context = create_function();
// use the context to send the set command
set(context, "key", "value");
```

### Send a GET command
The GET command asks the database the value of the given key.
To send a GET command you have to use the `get` function.
The first parameter takes the context, which has to be created through `created_function`. The second parameter takes the key.
The function returns the value of the key as `char*`.

```c
// create a connection to redis
redisContext *context = create_function();
// use the context to send the get command
const char* temp = get(context, "key");
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
Ask Ramin Bahadoorifar in the school anytime you want, no bock this zu schreiben :D
