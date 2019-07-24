import os
import pymysql
import redis

RDS_ENDPOINT = 'recsys-eames-cluster.cluster-ro-cdzwezzqswyj.ap-northeast-2.rds.amazonaws.com'
RDS_PORT = 3306
RDS_USER = 'eames'
RDS_PWD = 'dlatkdgur1!'
RDS_DB = 'apmall'

REDIS_ENDPOINT = '13.124.86.19'
REDIS_PORT = 6379
REDIS_DB = 1
REDIS_PASSWORD = "dlatkdgur1!"
SERVICE_NAME = 'apmall'


class RedisClient(object):
    def __init__(self):
        self._connect = redis.Redis(host=REDIS_ENDPOINT,
                                    port=REDIS_PORT,
                                    db=REDIS_DB,
                                    password=REDIS_PASSWORD)

    def get_items(self, item_id):
        key = f'{SERVICE_NAME}:{item_id}'
        return self._connect.get(key)

    def set_items(self, item_id, items, expires):
        key = f'{SERVICE_NAME}:{item_id}'
        self._connect.set(key=key, value=items, expires=expires)


class RDSClient(object):
    def __init__(self):
        self._connection = pymysql.connect(host=RDS_ENDPOINT,
                                           port=RDS_PORT,
                                           user=RDS_USER,
                                           password=RDS_PWD,
                                           database=RDS_DB)

    def get_item_list(self, item_id):
        with self._connection.cursor() as cursor:
            sql = f"SELECT rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8, rec9, rec10, rec11, rec12, rec13, rec14, " \
                f"rec15, rec16, rec17, rec18, rec19, rec20 FROM apmall.apmall_item2item " \
                f"WHERE target={item_id} AND date_time=(SELECT MAX(date_time) FROM apmall.apmall_item2item)"
            cursor.execute(sql)
            result = cursor.fetchone()

            if result is None:
                return []

            if len(result) == 1:
                return list(result)

            return []


rds_client = RDSClient()
print(rds_client.get_item_list(1111))
# print(rds_client.get_item_list(111130000427))
