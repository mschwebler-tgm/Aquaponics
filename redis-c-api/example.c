#include "redis_api.c"

void callback_example(const char key[], const char value[]) {
	printf("%s ==== %s\n\n\n", key, value);
}

int main (int argc, char **argv) {
	//############################
	//SYNC (SET AND GET EXAMPLE)
	//############################
	redisContext *c = create_connection();
	//SETS THE TEMPERATURE TO 23
	set(c,SENSOR_TEMPERATURE, "23");
	//GETS THE VALUE OF TEMPERATURE
	const char *temp = get(c, SENSOR_TEMPERATURE);
	printf("TEMPRATURE IS %s\n", temp);
	//DISCONNECTS FROM SERVER
	disconnect_connection(c);

	//############################
	//ASYNC EXAMPLE
	//############################
	redisAsyncContext *ac = subscribe_to_topic(TOPIC_ACTUATORS, callback_example);
	return 0;
}