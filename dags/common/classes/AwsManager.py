import boto3
import os

class AwsManager:
    '''Class to set up connection with AWS S3 Data Lake'''
    def __init__(self) -> None:
        self.aws_key_id = os.getenv('AWS_KEY_ID')
        self.aws_secret_key = os.getenv('AWS_SECRET_KEY')
        self.aws_region = os.getenv('AWS_REGION')
        self.aws_session = self.create_aws_client()
        self.s3_resource = self.create_s3_resource()

    def create_aws_client(self):
        aws_session = boto3.Session(profile_name='hobby_dev')
        # ,
        #                         aws_access_key=self.aws_key_id,
        #                         aws_secret_access_key=self.aws_secret_key,
        #                         region=self.aws_region
        return aws_session

    def create_s3_resource(self):
        s3 = self.aws_session.resource('s3')
        return s3