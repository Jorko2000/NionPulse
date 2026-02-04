variable "region" {
  default = "us-east-1"
}

variable "db_user" {}
variable "db_pass" {}


outputs.tf


output "sns_topic_arn" {
  value = aws_sns_topic.events.arn
}

output "sqs_queue_url" {
  value = aws_sqs_queue.queue.id
}

output "db_endpoint" {
  value = aws_db_instance.postgres.endpoint
}
