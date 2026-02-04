provider "aws" {
  region = var.region
}

resource "aws_sns_topic" "events" {
  name = "nionpulse-events"
}

resource "aws_sqs_queue" "queue" {
  name = "nionpulse-queue"
}

resource "aws_s3_bucket" "analytics" {
  bucket = "nionpulse-analytics-${var.region}"
}

resource "aws_db_instance" "postgres" {
  engine = "postgres"
  instance_class = "db.t3.micro"
  allocated_storage = 20
  username = var.db_user
  password = var.db_pass
  skip_final_snapshot = true
}
