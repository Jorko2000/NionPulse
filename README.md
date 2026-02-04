# NionPulse

NionPulse is a cloud-native, event-driven analytics platform built to
demonstrate senior-level Python backend engineering.

It ingests events through a REST API, publishes them to AWS SNS/SQS,
processes them asynchronously using threaded and multiprocessing workers,
stores results in Postgres/DynamoDB/S3, and exposes analytics dashboards.

## Core Capabilities

- FastAPI REST service
- AWS SNS → SQS event fan-out
- Threading + multiprocessing workers
- Redis caching
- JWT authentication (Cognito)
- Rate limiting
- Terraform infrastructure
- Kubernetes deployments
- Dockerized services
- Jenkins + CircleCI pipelines
- Observability via OpenTelemetry + Prometheus + Grafana
- React dashboard frontend

## Local Dev

docker compose up --build

API: http://localhost:8000  
Frontend: http://localhost:5173  

## Terraform

cd terraform
terraform init
terraform apply

## Kubernetes

kubectl apply -f k8s/

## Tests

pytest services/
