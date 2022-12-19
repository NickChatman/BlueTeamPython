#This will scan a dynamodb table with boto3
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YourFile')
response = table.scan()['Items']
print(response)
