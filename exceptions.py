class RedisError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class KeyNotFound(RedisError):
    def __init__(self, message="The provided key doesn't exist in redis."):
        super().__init__(message,status_code=400)