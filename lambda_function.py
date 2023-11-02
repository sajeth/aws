
import json
import urllib.request

def lambda_handler(event, context):

    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps({"Hello": "World"})
    }
