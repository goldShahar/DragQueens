from kafkush.consumers import consumer
from config import TOPIC1


def welcome_func(action: str, table: str, valuses: dict[str, any]):
    pass


def write_topic1_to_postgress_func():
    status = consumer.read_from_kafka(TOPIC1)
    welcome_func(status["ACTION"], status["TABLE"], status["VALUSES"])
