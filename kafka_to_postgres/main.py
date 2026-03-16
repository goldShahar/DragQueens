from postgres_manager.welcome_func import welcome_func
from kafkush.consumers import consumer
from kafkush.producers import producer
from config import TOPIC1


def write_topic1_to_postgress_func():
    status = consumer.read_from_kafka(TOPIC1)
    answer = welcome_func(status["ACTION"], status["TABLE"], status["VALUSES"])
    write_postgress_to_topic1_func(answer)


def write_postgress_to_topic1_func(answer):
    producer.send_to_kafka(answer, TOPIC1)


while True:
    try:
        write_postgress_to_topic1_func()
    except:
        continue
