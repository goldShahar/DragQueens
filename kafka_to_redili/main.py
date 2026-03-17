from kafkush.consumers import consumer
from redili_manager.my_redis import write, delete_key
from config import TOPIC1, TOPIC2


def write_topic1_to_redili_func(consumer_cache):
    status = consumer.read_from_kafka(consumer_cache, TOPIC1)
    write(status["id_msg"], "in progress")


def write_topic2_to_redili_func(consumer_cache):
    status = consumer.read_from_kafka(consumer_cache, TOPIC2)
    print("status", status)
    delete_key(status["id_msg"])
    write(
        status["id_msg"],
        status["status"],
    )


consumer_cache = consumer.create_consumer(consumer.consumer_config_cache)


def read_kafka():
    try:
        print("topic1")
        write_topic1_to_redili_func(consumer_cache)
        print("topic2")
        write_topic2_to_redili_func(consumer_cache)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("--------------------")
    while KeyboardInterrupt:
        read_kafka()
