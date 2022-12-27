import boto3
from boto3.resources.base import ServiceResource
from .create_table import create_table


def initialize_db() -> ServiceResource:
    client =  boto3.resource('dynamodb',
         endpoint_url='http://db:8000',
         region_name='example',
         aws_access_key_id='example',
         aws_secret_access_key='example')

    create_table(client=client)
    return client

client = initialize_db()