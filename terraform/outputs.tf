output "sns_topic_arn" {
  value = aws_sns_topic.events.arn
}

output "sqs_queue_url" {
  value = aws_sqs_queue.queue.id
}

output "db_endpoint" {
  value = aws_db_instance.postgres.endpoint
}
