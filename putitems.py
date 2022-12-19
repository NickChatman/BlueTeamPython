import boto3

dynamodb =boto3.resource('dynamodb')

table=dynamodb.Table('Classes')

response=table.put_item(
        Item={
            'ClassID': 'ASCG',
            'Class_Number': 450,
            'ClassName':"Digital Forensics",
            'Credit Value':'3'
         },
         )
table.put_item(
        Item={
            'ClassID': 'ASCG',
            'Class_Number': 545,
            'ClassName':"Software Engineering",
            'Credit Value':'3'
            },
            )
table.put_item(
            Item={
            'ClassID': 'ASCG',
            'Class_Number': 555,
            'ClassName':"Data Mining",
            'Credit Value':'3'
            },
            )
table.put_item(
             Item={
            'ClassID': 'ASCG',
            'Class_Number': 556,
            'ClassName':"Data Visualization",
            'Credit Value':'3'
            },
            )
table.put_item(
             Item={
            'ClassID': 'ASCG',
            'Class_Number': 561,
            'ClassName':"System Analysis",
            'Credit Value':'3'
            },
            )
table.put_item(
             Item={
            'ClassID': 'ASCG',
            'Class_Number': 585,
            'ClassName':"Network Administration",
            'Credit Value':'3'
            },
            )
table.put_item(
             Item={
            'ClassID': 'ASCG',
            'Class_Number': 572,
            'ClassName':"Modern OS Security",
            'Credit Value':'3'
            },
            )
table.put_item(
             Item={
            'ClassID': 'ASCG',
            'Class_Number': 570,
            'ClassName':"Computer System Security",
            'Credit Value':'3'
            },
            )
table.put_item(
             Item={
            'ClassID': 'ASCG',
            'Class_Number': 578,
            'ClassName':"Network Security",
            'Credit Value':'3'
            },
            )
table.put_item(
             Item={
            'ClassID': 'ASCG',
            'Class_Number': 360,
            'ClassName':"Cybersecurity",
            'Credit Value':'3'
            
            }
            )
   
