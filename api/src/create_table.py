def create_table(client):
    client.create_table(
        TableName='Milk',                # create table Recipes
        AttributeDefinitions=[
            {
                'AttributeName': 'uid',     # In this case, I only specified uid as partition key (there is no sort key)
                'AttributeType': 'S'        # with type string
            },
            {
                'AttributeName': 'quantity',     # In this case, I only specified uid as partition key (there is no sort key)
                'AttributeType': 'N'        # with type string
            }
        ],
        KeySchema=[
            {
                'AttributeName': 'uid',     # attribute uid serves as partition key
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'quantity',     # attribute uid serves as partition key
                'KeyType': 'RANGE'
            }
        ],
        ProvisionedThroughput={             # specying read and write capacity units
            'ReadCapacityUnits': 10,        # these two values really depend on the app's traffic
            'WriteCapacityUnits': 10
        }
    )
    print("Table created...")
