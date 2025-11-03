import json
import boto3
import os

sns = boto3.client("sns")

def lambda_handler(event, context):
    # Log full event for debugging / audit
    print("Received Event:", json.dumps(event, indent=2))

    # Extract relevant fields
    try:
        detail = event.get("detail", {})
        user_identity = detail.get("userIdentity", {})
        event_name = detail.get("eventName", "UnknownEvent")
        source = event.get("source", "UnknownSource")

        # For your email subject and body
        subject = f"[ALERT] Root activity detected in {source}"
        message = (
            f"A root user performed an action in {source}.\n\n"
            f"Event Name: {event_name}\n"
            f"Principal ID: {user_identity.get('principalId', 'N/A')}\n"
            f"Account: {user_identity.get('accountId', 'N/A')}\n\n"
            f"Full event details:\n{json.dumps(event, indent=2)}"
        )

        # Post to SNS topic
        sns.publish(
            TopicArn="SNS_TOPIC_ARN",
            Subject=subject,
            Message=message
        )

        print("SNS notification sent successfully.")

    except Exception as e:
        print(f"Failed to process event: {str(e)}")

    return {"statusCode": 200}
