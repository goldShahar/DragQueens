from redili_manager import my_redis


def get_message_by_id(id: str):
    result = my_redis.read(id)
    if result:
        return result
    else:
        return "This id does not exits or this reqest was handaled a while back and no longer in our system"
