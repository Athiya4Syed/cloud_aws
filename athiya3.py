import json
import boto3
import base64

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Retrieve data from the event
    bucket_name = event['bucket_name']
    object_key = event['object_key']
    object_data = event['object_data']

    # Convert the base64-encoded data back to binary
    object_data_binary = base64.b64decode(object_data)

    # Upload the object to S3
    s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=object_data_binary)

    return {
        'statusCode': 200,
        'body': json.dumps(f'Object {object_key} uploaded to bucket {bucket_name}')
    }
{
    "bucket_name": "your-bucket-name",
    "object_key": "your-object-key",
    "object_data": "base64-encoded-data"
}
import base64
with open('your-file-path', 'rb') as file:
    encoded_data = base64.b64encode(file.read()).decode('utf-8')




Integrate Lambda with powerfull S3 service
import boto3
import os

s3_client = boto3.client('s3')
ses_client = boto3.client('ses')

def lambda_handler(event, context):
    # Get the bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Retrieve the file from S3
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    content = response['Body'].read().decode('utf-8')

    # Extract email IDs
    email_ids = content.split('\n')

    # Send an email to each email ID
    for email in email_ids:
        if email:
            send_email(email)

    return {
        'statusCode': 200,
        'body': 'Emails sent successfully'
    }

def send_email(recipient_email):
    response = ses_client.send_email(
        Source=os.environ['SES_SOURCE_EMAIL'],
        Destination={'ToAddresses': [recipient_email]},
        Message={
            'Subject': {'Data': 'Hello from Lambda!'},
            'Body': {
                'Text': {'Data': 'This is a test email sent from an AWS Lambda function.'}
            }
        }
    )
    return response
