from postgres_manager.welcome_func import welcome_func
from redili_manager import my_redis


def job():
    hazard_types = welcome_func("READ", "TYPES", {"columes": "all"})
    for hazard_type in hazard_types:
        if not my_redis.read(hazard_type):
            my_redis.write(hazard_type)
