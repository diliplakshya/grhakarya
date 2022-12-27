import boto3
from boto3.resources.base import ServiceResource
from .create_table import create_table
# import settings for variable access
from .config import settings


def initialize_db() -> ServiceResource:
    print("url {}".format(settings.db_url))
    client =  boto3.resource('dynamodb',
         #endpoint_url=settings.db_url,
         region_name=settings.aws_region,
         aws_access_key_id=settings.aws_access_key_id,
         aws_secret_access_key=settings.aws_secret_access_key)
    
    print("Connected to Dynamo DB")

    if 'Milk' not in [table.name for table in client.tables.all()]:
        table =  create_table(client=client)
    return client


client = initialize_db()
