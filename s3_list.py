import boto3
import json

s3 = boto3.client(
    's3',
    aws_access_key_id='AKIAWC26C2VWM2MHGPMB',
    aws_secret_access_key='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'
)

response = s3.list_buckets()

print(response)