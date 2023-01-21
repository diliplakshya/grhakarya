import boto3
from boto3.resources.base import ServiceResource
from .create_table import create_table
# import settings for variable access
from .config import settings
import json


def initialize_db() -> ServiceResource:
    client = None

    db_url = "http://" + settings.dns + ":8000"

    if json.loads(settings.aws_dynamo_db.lower()):
        client =  boto3.resource('dynamodb',
            region_name=settings.aws_region,
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key)
    else:
        client =  boto3.resource('dynamodb',
            endpoint_url=db_url,
            region_name=settings.aws_region,
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key)

    print("Connected to Dynamo DB")

    if 'MilkProduct' not in [table.name for table in client.tables.all()]:
        table =  create_table(client=client)
    return client


# client = initialize_db()
