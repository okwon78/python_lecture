import os
import json
import logging
import redis
import pymysql

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

SERVICE_NAME = os.environ['SERVICE_NAME']

REDIS_ENDPOINT = os.environ['REDIS_ENDPOINT']
REDIS_PORT = int(os.environ['REDIS_PORT'])
REDIS_DB = os.environ['REDIS_DB']
REDIS_EXPIRE_HOUR = int(os.environ['REDIS_EXPIRE_HOUR'])
REDIS_EXPIRE = 60 * 60 * REDIS_EXPIRE_HOUR
REDIS_PWD = os.environ['REDIS_PWD']

RDS_ENDPOINT = os.environ['RDS_ENDPOINT']
RDS_PORT = int(os.environ['RDS_PORT'])
RDS_USER = os.environ['RDS_USER']
RDS_PWD = os.environ['RDS_PWD']
RDS_DB = os.environ['RDS_DB']


class RedisClient(object):
    def __init__(self):
        self._connect = redis.Redis(host=REDIS_ENDPOINT,
                                    port=REDIS_PORT,
                                    db=REDIS_DB,
                                    password=REDIS_PWD)

    def get_items(self, item_id):
        key = f'{SERVICE_NAME}:{item_id}'
        result = self._connect.get(key)
        logger.info(f"result from redis: {result}")

        if result is None:
            return []
        else:
            result

    def set_items(self, item_id, items):
        key = f'{SERVICE_NAME}:{item_id}'
        self._connect.set(name=key, value=items, ex=REDIS_EXPIRE)


class RDSClient(object):
    def __init__(self):
        self._connection = pymysql.connect(host=RDS_ENDPOINT,
                                           port=RDS_PORT,
                                           user=RDS_USER,
                                           password=RDS_PWD,
                                           database=RDS_DB)

    def get_items(self, item_id):
        with self._connection.cursor() as cursor:
            sql = f"SELECT rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8, rec9, rec10, rec11, rec12, rec13, rec14, " \
                f"rec15, rec16, rec17, rec18, rec19, rec20 FROM apmall.apmall_item2item " \
                f"WHERE target={item_id} AND date_time=(SELECT MAX(date_time) FROM apmall.apmall_item2item)"

            # logger.info(f"RDS sql: {sql}")

            cursor.execute(sql)
            result = cursor.fetchone()
            logger.info(f"result from rds: {result}")

            if result is None:
                return []
            else:
                return list(result)


redis_client = RedisClient()
rds_client = RDSClient()


def lambda_handler(event, context):
    logger.info("Received event: " + json.dumps(event, indent=2))

    params = event['params']
    item_id = params['item_id']
    # item list from redis
    items = redis_client.get_items(item_id)

    # if item doesn't exist in redis, retrieve items from rds
    if len(items) == 0:
        items = rds_client.get_items(item_id)
        logger.info(f"read items form RDS: {items}")
        if len(items) > 0:
            redis_client.set_items(item_id, items)
        else:
            logger.warn(f'Failed to find {item_id} from rds')

    logger.info(f'item list: {items}')

    data = {
        'item_id': item_id,
        'items': items
    }

    if len(items) > 0:
        response = {
            'code': '0000',
            'message': 'SUCCESS',
            'data': data
        }
    else:
        response = {
            'code': '0001',
            'message': 'ITEM LIST IS EMPTY',
            'data': data
        }

    return response
