from kafka_to_redili.main import write_topic1_to_redili_func, consumer_cache

while KeyboardInterrupt:
    print("----------t1-----------")
    write_topic1_to_redili_func(consumer_cache)
