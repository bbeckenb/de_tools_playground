import boto3
import os

class S3Manager:
    '''Class to set up connection with AWS S3 Data Lake'''
    def __init__(self) -> None:
        self.aws_key_id = os.getenv('AWS_KEY_ID')
        self.aws_secret_key = os.getenv('AWS_SECRET_KEY')
        self.aws_region = os.getenv('AWS_REGION')
        self.S3Client = self.create_S3_client()

    def create_S3_client(self):
        s3_client = boto3.client('s3',
                                aws_access_key=self.aws_key_id,
                                aws_secret_access_key=self.aws_secret_key,
                                region=self.aws_region)
        return s3_client