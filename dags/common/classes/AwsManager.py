import boto3

class AwsManager:
    '''Class to set up connection with AWS S3 Data Lake'''
    def __init__(self) -> None:
        self.aws_session = self.create_aws_client()
        self.s3_resource = self.create_s3_resource()

    def create_aws_client(self):
        aws_session = boto3.Session(profile_name='hobby_dev')
        return aws_session

    def create_s3_resource(self):
        s3 = self.aws_session.resource('s3')
        return s3