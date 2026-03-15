
from confluent_kafka import Consumer

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "kafka-consumer",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)

def read_from_kafka(topic: str):
    consumer.subscribe([topic])
    print(f"Consumer is running and subscribed to {topic} topic")
    
    msg = consumer.poll()
    if msg.error():
        consumer.close()
        return msg.error

    value = msg.value().decode("utf-8")
    print(value)
    consumer.close()
    return value