from postgres_manager.welcome_func import welcome_func
from kafkush.consumers import consumer
from kafkush.producers import producer
from config import TOPIC1, TOPIC2


def write_topic1_to_postgress_func(consumer_main):
    status = consumer.read_from_kafka(consumer_main, TOPIC1)
    print("status", status)
    answer = welcome_func(
        status["ACTION"],
        status["TABLE"],
        {
            k: status[k]
            for k in set(list(status.keys())) - set(["ACTION", "TABLE", "id_msg"])
        },
    )
    print("answer", answer)
    write_postgress_to_topic1_func(answer, status["id_msg"])


def write_postgress_to_topic1_func(answer: str, id_msg: str):
    print("topic1_func", {"status": answer, "id_msg": id_msg})
    producer.send_to_kafka({"status": answer, "id_msg": id_msg}, TOPIC2)


while KeyboardInterrupt:
    consumer_main = consumer.create_consumer(consumer.consumer_config_main)
    try:
        write_topic1_to_postgress_func(consumer_main)
    except:
        continue
