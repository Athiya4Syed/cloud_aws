mkdir python
cd python
pip install pymongo -t .
zip -r pymongo-layer.zip .
import json
import os
from pymongo import MongoClient

def lambda_handler(event, context):
    # Get environment variables
    cluster_endpoint = os.environ['CLUSTER_ENDPOINT']
    cluster_port = os.environ['CLUSTER_PORT']
    db_name = os.environ['DB_NAME']
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']

    # Connect to MongoDB
    client = MongoClient(f'mongodb://{username}:{password}@{cluster_endpoint}:{cluster_port}/?ssl=true&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client[db_name]

    # Perform a simple query (example)
    collection = db['your_collection']
    document = collection.find_one()
    
    return {
        'statusCode': 200,
        'body': json.dumps(document, default=str)
    }
