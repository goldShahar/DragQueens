from confluent_kafka import Consumer
import json

consumer_config_main = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "consumer-main",
    "auto.offset.reset": "earliest",
}
consumer_config_cache = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "consumer-cache",
    "auto.offset.reset": "earliest",
}


def create_consumer(consumer):
    return Consumer(consumer)


def read_from_kafka(consumer: Consumer, topic: str):
    consumer.subscribe([topic])
    print(f"Consumer is running and subscribed to {topic} topic")

    msg = consumer.poll()
    if msg.error():
        print(msg.error())
        return msg.error()
    value = msg.value().decode("utf-8")
    print("val", value)
    consumer.close()
    return json.loads(value)
