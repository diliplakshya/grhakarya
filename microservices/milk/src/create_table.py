def create_table(client=None):
    """
    Creates a DynamoDB table.

    :param client: Either a Boto3 or DAX resource.
    :return: The newly created table.
    """
    if client is None:
        raise Exception("Invalid client object.")

    table_name = 'MilkProduct'

    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': 'uid', 'KeyType': 'HASH'}
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'uid', 'AttributeType': 'S'}
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    }
    table = client.create_table(**params)
    print(f"Creating {table_name}...")
    table.wait_until_exists()
    return table

