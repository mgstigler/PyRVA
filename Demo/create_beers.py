import json
import boto3
dynamodb = boto3.resource('dynamodb')

def create(event, context):
    table = dynamodb.Table('PyBrew')
    print(event)
    data = json.loads(event["body"])
    # fetch items from the database
    result = table.put_item(
        TableName='PyBrew',
        Item={
            "beer_type": data['beer_type'],
            "beer_name": data['beer_name']
        },
    )

    # create and return response
    response = {
        "statusCode": 200,
        "body": "Beer has been created!"
    }

    return response