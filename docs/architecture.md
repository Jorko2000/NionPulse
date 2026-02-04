NionPulse uses event-driven microservices.

API → SNS → SQS → Workers

Workers scale horizontally and process events using:
- ThreadPoolExecutor for IO
- multiprocessing Pool for CPU

Data:
- RDS Postgres (transactions)
- DynamoDB (state)
- S3 (archives)

Kubernetes orchestrates containers.
Terraform provisions AWS infra.
