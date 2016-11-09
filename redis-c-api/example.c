#include "redis_api.c"

void callback_example(const char key[], const char value[]) {
	printf("%s ==== %s\n", key, value);
}

int main (int argc, char **argv) {
	//############################
	//SYNC (SET AND GET EXAMPLE)
	//############################
	redisContext *c = create_connection("localhost", 6379);
	//SETS THE TEMPERATURE TO 23
	set(c, "temperature 23 humidity 20");
	//GETS THE VALUE OF TEMPERATURE
	const char *temp = get(c, SENSOR_TEMPERATURE);
	printf("TEMPERATURE IS %s \n", temp);
	//DISCONNECTS FROM SERVER
	disconnect_connection(c);

	//############################
	//ASYNC EXAMPLE
	//############################
	redisAsyncContext *ac = subscribe_to_topic("localhost", 6379, TOPIC_ACTUATORS, callback_example);
	return 0;
}
