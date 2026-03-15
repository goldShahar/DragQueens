import redis
from config import HOST, REDIS_PORT, EXP
from exceptions import KeyNotFound

POOL =  redis.ConnectionPool(host=HOST, port=REDIS_PORT, decode_responses=True)

def read(key: str):
    my_server = redis.Redis(connection_pool=POOL)
    response = my_server.get(key)
    return response

def write(key: str, value: any):
    my_server = redis.Redis(connection_pool=POOL)
    my_server.set(key, value,ex=EXP)

def delete_key(key: str):
    my_server = redis.Redis(connection_pool=POOL)
    if my_server.get(key):
        my_server.delete(key)
    else:
        raise KeyNotFound