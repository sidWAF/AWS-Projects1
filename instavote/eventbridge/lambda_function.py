import json
import requests  # Corrected import
import boto3

# Initialize AWS EventBridge client
eventbridge = boto3.client('events')

def lambda_handler(event, context):
    # Custom event payload
    custom_event = {
        'source': 'my.api.gateway',
        'detail-type': 'CustomEventType',
        'detail': {
            'key': 'value'
        }
    }
    url = "https://google5261.zendesk.com/api/v2/tickets"
    payload = {
        "ticket": {
            "comment": {
                "body": "Customer experience was unsatisfactory."
            },
            "priority": "urgent",
            "subject": "Customer experience was unsatisfactory."
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.request(  # Corrected request method
        "POST",
        url,
        auth=('username', 'password'),  # Replace with your Zendesk credentials
        headers=headers,
        json=payload
    )
    
    print(response.text)

    # Publish the event to EventBridge
    response = eventbridge.put_events(
        Entries=[
            {
                'Source': custom_event['source'],
                'DetailType': custom_event['detail-type'],
                'Detail': json.dumps(custom_event['detail'])
            }
        ]
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Event published to EventBridge successfully')
    }
