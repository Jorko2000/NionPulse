import boto3, json
from thread_pool import process_io_tasks
from mp_engine import run_cpu_tasks

sqs = boto3.client("sqs")
QUEUE_URL = "SQS_URL"

def poll():
    while True:
        msgs = sqs.receive_message(QueueUrl=QUEUE_URL, MaxNumberOfMessages=10).get("Messages", [])
        for msg in msgs:
            body = json.loads(msg["Body"])
            process_io_tasks([body])
            run_cpu_tasks([body])
            sqs.delete_message(QueueUrl=QUEUE_URL, ReceiptHandle=msg["ReceiptHandle"])

if __name__ == "__main__":
    poll()
