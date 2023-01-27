import boto3
from boto3.resources.base import ServiceResource
from .create_table import create_table
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import settings for variable access
from .config import settings
import json


SQL_ALCHEMY_MYSQL_CONNECTION_URL = url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
        settings.mysql_user, settings.mysql_root_password, 
        settings.mysql_host, settings.mysql_port, settings.mysql_database
    )

engine = create_engine(url=SQL_ALCHEMY_MYSQL_CONNECTION_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_connection():

    return create_engine(url=SQL_ALCHEMY_MYSQL_CONNECTION_URL)

def initialize_db() -> ServiceResource:
    client = None

    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = get_connection()

        print(
            f"Connection to the {settings.mysql_host} for user {settings.mysql_user} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

    # if json.loads(settings.aws_dynamo_db.lower()):
    #     client =  boto3.resource('dynamodb',
    #         region_name=settings.aws_region,
    #         aws_access_key_id=settings.aws_access_key_id,
    #         aws_secret_access_key=settings.aws_secret_access_key)
    # else:
    #     client =  boto3.resource('dynamodb',
    #         endpoint_url=db_url,
    #         region_name=settings.aws_region,
    #         aws_access_key_id=settings.aws_access_key_id,
    #         aws_secret_access_key=settings.aws_secret_access_key)

    # print("Connected to Dynamo DB")

    # if 'MilkProduct' not in [table.name for table in client.tables.all()]:
    #     table =  create_table(client=client)
    return client


client = initialize_db()
