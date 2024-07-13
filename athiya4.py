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
