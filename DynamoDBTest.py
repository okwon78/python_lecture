import logging
import boto3
import time

# day * minutes * seconds * hours
EXPIRE_DAY_OFFSET = 60 * 60 * 24  # minutes * seconds * hour
EXPIRE_DAY = 30
#EXPIRE = EXPIRE_DAY * EXPIRE_DAY_OFFSET
EXPIRE = 60

MAX_SEQ_LEN = 5


class DynamoDB(object):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb',
                                       region_name='ap-northeast-2',
                                       aws_access_key_id='',
                                       aws_secret_access_key='')

        self.table = self.dynamodb.Table('recsys-appmall-user-history')
        # print(self.table.creation_date_time)

    @staticmethod
    def get_ttl():
        ttl = EXPIRE + int(time.time())
        return ttl

    def __put_item(self, user_id, items):
        ttl = self.get_ttl()

        if len(items) > MAX_SEQ_LEN:
            items = items[0:MAX_SEQ_LEN]

        self.table.put_item(
            Item={
                'ttl': ttl,
                'user_id': user_id,
                'items': items
            }
        )

    def add_item(self, user_id, item):
        origin_items = self.get_items(user_id)

        if origin_items is None:
            self.add_new_item(user_id, item)
        else:
            self.update_item(user_id, origin_items, item)

    def update_item(self, user_id, origin_items, item):
        if origin_items[0] == item:
            return
        else:
            new_lst = [item, *origin_items]
            self.__put_item(user_id, new_lst)

    def add_new_item(self, user_id, item):
        ttl = self.get_ttl()

        self.table.put_item(
            Item={
                'user_id': user_id,
                'items': [item],
                'ttl': ttl
            }
        )

    def get_items(self, user_id):
        response = self.table.get_item(
            Key={
                'user_id': user_id
            }
        )

        if response['ResponseMetadata']['HTTPStatusCode'] is not 200:
            logging.error(f"Invalid HTTPStatusCode [{response['ResponseMetadata']['HTTPStatusCode']}]")
            return None

        if 'Item' in response:
            items = response['Item']['items']
            return items
        else

        else:
            return None


dynamodb = DynamoDB()

# dynamodb.get_items("2222")

dynamodb.add_item("2", "1")
dynamodb.add_item("2", "2")
dynamodb.add_item("2", "3")
dynamodb.add_item("2", "4")
dynamodb.add_item("2", "5")
dynamodb.add_item("2", "6")
dynamodb.add_item("2", "7")
dynamodb.add_item("2", "8")
dynamodb.add_item("2", "9")
dynamodb.add_item("2", "10")


