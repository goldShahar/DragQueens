import json
from confluent_kafka import Producer

producer_config = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(producer_config)

def send_to_kafka(msg, topic):
    value = json.dumps(msg).encode("utf-8")
    producer.produce(
    topic=topic,
    value=value,
    callback=msg_report
    )
    producer.flush()


def msg_report(err, msg):
    if err:
        print(f"Message failed: {err}")
    else:
        print(f"Message {msg.value().decode("utf-8")}")
        print(f"Message sent to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")