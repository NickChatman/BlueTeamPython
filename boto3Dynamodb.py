#Creates a dynamodb table with boto3
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='Classes',
    KeySchema=[
        {
            'AttributeName': 'ClassID',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Class_Number',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ClassID',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Class_Number',
            'AttributeType': 'N'
        },
        
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# Wait until the table exists.
table.wait_until_exists()
