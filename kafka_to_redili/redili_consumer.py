from kafkush.consumers import consumer
from redili_manager.my_redis import write
from config import TOPIC1, TOPIC2


def write_topic1_to_redili_func():
    status = consumer.read_from_kafka(TOPIC1)
    write(status["id_msg"], "in progress")


def write_topic2_to_redili_func():
    status = consumer.read_from_kafka(TOPIC2)
    write(
        status["id_msg"],
        status["status"],
    )


if __name__ == "__main__":
    while True:
        try:
            write_topic1_to_redili_func()
            write_topic2_to_redili_func()
        except:
            continue
