import redis
import json
from config import HOST, REDIS_PORT, EXP, SUCCESS, FAILURE
from typing import Any

POOL = redis.ConnectionPool(host=HOST, port=REDIS_PORT, decode_responses=True)


def read(key: str):
    my_server = redis.Redis(connection_pool=POOL)
    value = my_server.get(key)
    if value:
        return json.loads(value)
    return value


def write(key: str, value: Any):
    my_server = redis.Redis(connection_pool=POOL)
    my_server.set(key, json.dumps(value), ex=EXP)


def delete_key(key: str):
    my_server = redis.Redis(connection_pool=POOL)
    if my_server.get(key):
        my_server.delete(key)
        return SUCCESS
    else:
        return FAILURE
