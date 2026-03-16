from kafka_to_redili.main import write_topic2_to_redili_func, consumer_cache

while KeyboardInterrupt:
    print("----------t2-----------")
    write_topic2_to_redili_func(consumer_cache)
