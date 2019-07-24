import logging
import boto3
import time

# day * minutes * seconds * hours
EXPIRE_DAY = 30 * 60 * 60 * 24


class DynamoDB(object):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb',
                                       region_name='ap-northeast-2',
                                       aws_access_key_id='AKIAXRJ2HI73PLFWN43E',
                                       aws_secret_access_key='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')

        self.table = self.dynamodb.Table('recsys-inverted-index')
        # print(self.table.creation_date_time)

    @staticmethod
    def get_ttl():
        ttl = EXPIRE_DAY + int(time.time())
        return ttl

    def __put_item(self, user_id, items):
        ttl = self.get_ttl()

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

        if 'Item' in response:
            items = response['Item']['items']
            return items

        if response['ResponseMetadata']['HTTPStatusCode'] is not 200:
            logging.error(f"Invalid HTTPStatusCode [{response['ResponseMetadata']['HTTPStatusCode']}]")
            return None
        else:
            return None


dynamodb = DynamoDB()

# dynamodb.get_items("2222")

dynamodb.add_item("2222", "33333")
