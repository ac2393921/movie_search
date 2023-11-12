import redis


class RedisHandler:
    def __init__(self, host="localhost", port=6379, db=0):
        self.redis_client = redis.StrictRedis(
            host=host,
            port=port,
            db=db,
            decode_responses=True,
        )

    def set_value(self, key, value, ex=None):
        self.redis_client.set(key, value, ex)

    def get_value(self, key):
        return self.redis_client.get(key)

    def delete_key(self, key):
        self.redis_client.delete(key)
