import boto3, json
from config import settings

sns = boto3.client("sns", region_name=settings.AWS_REGION)

def publish_event(payload: dict):
    sns.publish(TopicArn=settings.SNS_TOPIC_ARN, Message=json.dumps(payload))
