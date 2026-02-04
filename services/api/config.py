import os

class Settings:
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")
    DATABASE_URL = os.getenv("DATABASE_URL")
    REDIS_HOST = os.getenv("REDIS_HOST", "redis")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    COGNITO_POOL_ID = os.getenv("COGNITO_POOL_ID")

settings = Settings()
