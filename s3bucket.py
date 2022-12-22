#Bucket to create a s3 bucket using boto3
import boto3

s3_client = boto3.client("s3")

response =s3_client.create_bucket(Bucket="nicholaschatmanbuckett")

print(response)

