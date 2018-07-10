import json
import decimal
import boto3
dynamodb = boto3.resource('dynamodb')
from boto3.dynamodb.conditions import Key

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def get(event, context):
    table = dynamodb.Table('PyBrew')
    print(event)
    # fetch items from the database
    result = table.query(
        KeyConditionExpression=Key('beer_type').eq(event['queryStringParameters']['type'])
    )
    items = result['Items']

    # create and return response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=DecimalEncoder)
    }

    return response