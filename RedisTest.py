import os
import json
import logging
import redis

REDIS_ENDPOINT = "13.124.86.19"
REDIS_PORT = 6379
REDIS_DB = 1
REDIS_PWD = 'dlatkdgur1!'
REDIS_EXPIRE = 60
SERVICE_NAME = "aa"


class RedisClient(object):
    def __init__(self):
        self._connect = redis.Redis(host=REDIS_ENDPOINT,
                                    port=REDIS_PORT,
                                    db=REDIS_DB,
                                    password=REDIS_PWD)

    def get_items(self, item_id):
        key = f'{SERVICE_NAME}:{item_id}'
        s = self._connect.get(key).decode('utf8')
        values = s.split(',')
        result = [int(i) for i in values]
        print(f"result from redis: {result}")

        if result is None:
            return []
        else:
            return result

    def set_items(self, item_id, items):
        key = f'{SERVICE_NAME}:{item_id}'
        s = [str(i) for i in items]
        values = ",".join(s)
        self._connect.set(name=key, value=values, ex=REDIS_EXPIRE)


client = RedisClient()

client.set_items("aa", [1,2,3])
a = client.get_items("aa")
print(a)