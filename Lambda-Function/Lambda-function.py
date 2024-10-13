import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

def lambda_handler(event, context):
   
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        file_content = response['Body'].read().decode('utf-8')
        
        logger.info(f'Contents of the file {key}: {file_content}')
        
    except Exception as e:
        logger.error(f'Error processing object {key} from bucket {bucket}. Error: {str(e)}')
