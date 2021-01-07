import json

def handler(event, context):
    body = {
        "message": "Hello World! This is a message from a container",
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response