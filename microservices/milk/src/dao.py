from botocore.exceptions import ClientError


class Dao:
    def __init__(self, client = None) -> None:
        self.client = client

    def create(self, item):
        table_name = 'MilkProduct'
        table = self.client.Table(table_name)
        # Insert Data
        table.put_item(Item=item)

        # Scan Table
        scan_response = table.scan(TableName='MilkProduct')
        for item in scan_response['Items']:
            print(item)

    def get(self, uid: str):
        try:
            table = self.client.Table('MilkProduct')         # referencing to table MilkProduct
            response = table.get_item(Key={'uid': uid})     # get MilkProduct using uid (partition key)
            return response['Item']                         # return single data
        except ClientError as e:
            raise ValueError(e.response['Error']['Message'])