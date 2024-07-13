import json
import boto3
import os

s3_client = boto3.client('s3')
transcribe_client = boto3.client('transcribe')

def lambda_handler(event, context):
    # Get the bucket name and object key from the S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Define the transcription job name and file URI
    job_name = object_key.split('.')[0] + '_transcription'
    job_uri = f's3://{bucket_name}/{object_key}'

    # Start the transcription job
    response = transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat=object_key.split('.')[-1],
        LanguageCode='en-US',
        OutputBucketName=bucket_name,
        OutputKey=object_key.split('.')[0] + '.json'
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Transcription job started successfully')
    }
