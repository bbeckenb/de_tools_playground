import boto3

class AwsManager:
    '''Class to set up session with AWS and manage resources'''
    def __init__(self) -> None:
        self.aws_sess = self.create_aws_client()
        self.s3_res = self.create_s3_resource()

    def create_aws_client(self):
        aws_session = boto3.Session(profile_name='hobby_dev')
        return aws_session

    def create_s3_resource(self):
        s3 = self.aws_sess.resource('s3')
        return s3