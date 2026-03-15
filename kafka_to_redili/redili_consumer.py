from kafkush.consumers import consumer
from redili_manager.my_redis import write
from config import TOPIC1, TOPIC2, message_id


def write_topic1_to_redili_func():
    status = consumer.read_from_kafka(TOPIC1)
    write(
        status[message_id],
        {k: status[k] for k in set(list(status.keys())) - set([message_id])},
    )


def write_topic2_to_redili_func():
    status = consumer.read_from_kafka(TOPIC2)
    write(
        status[message_id],
        {k: status[k] for k in set(list(status.keys())) - set([message_id])},
    )
