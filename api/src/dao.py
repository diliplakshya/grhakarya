class Dao:
    def __init__(self, client = None) -> None:
        self.client = client

    def create(self, item):
        print("inserting values {}".format(item))
        table_name = 'Milk'
        table = self.client.Table(table_name)
        # item = Item={
        #         'uid': '9a0',
        #         'quantity': 1.0
        #     }

        # Insert Data
        table.put_item(Item=item)

        # Scan Table
        scan_response = table.scan(TableName='Milk')
        for item in scan_response['Items']:
            print(item)
