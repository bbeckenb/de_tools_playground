import boto3
import time
import re
import pandas as pd

class AwsManager:
    '''Class to set up session with AWS and manage resources'''
    def __init__(self) -> None:
        self.aws_sess = self.create_aws_client()
        self.s3_res = self.create_s3_resource()
        self.athena_client = self.create_athena_client()

    def create_aws_client(self):
        aws_session = boto3.Session(profile_name='hobby_dev')
        return aws_session

    def create_s3_resource(self):
        s3 = self.aws_sess.resource('s3')
        return s3

    def create_athena_client(self):
        athena = self.aws_sess.client('athena')
        return athena

    def query_athena(self, query_str):
        res = self.athena_client.start_query_execution(
            QueryString=query_str,
            QueryExecutionContext={
                'Database': 'stockdb',
                'Catalog': 'AwsDataCatalog'
            },
            ResultConfiguration={
                'OutputLocation': 's3://brycepracticequeryresbucket/temp/athena/output'
            }
        )
        return res

    def query_athena_get_s3_file(self, query_str, max_execution=5):
        exec = self.query_athena(query_str)
        exec_id = exec['QueryExecutionId']
        state = 'RUNNING'

        while (max_execution > 0 and state in ['RUNNING', 'QUEUED']):
            max_execution -= 1
            res = self.athena_client.get_query_execution(QueryExecutionId = exec_id)

            if 'QueryExecution' in res and \
                    'Status' in res['QueryExecution'] and \
                    'State' in res['QueryExecution']['Status']:
                state = res['QueryExecution']['Status']['State']
                if state == 'FAILED':
                    return False
                elif state == 'SUCCEEDED':
                    s3_path = res['QueryExecution']['ResultConfiguration']['OutputLocation']
                    filename = re.findall('.*\/(.*)', s3_path)[0]
                    return filename
            time.sleep(1)
        
        return False

    def get_csv_from_s3(self, file_name):
        obj = self.s3_res.Object('brycepracticequeryresbucket',
                                f'temp/athena/output/{file_name}')
        
        read_file = obj.get()['Body'].read()
        # read_file = obj.get()['Body'].read().decode('utf-8')
        # file_to_df = pd.read_csv(read_file)
        return read_file

    def clean_up_query_folder(self):
        bucket = self.s3_res.Bucket('brycepracticequeryresbucket')
        for item in bucket.objects.filter(Prefix='temp/athena/output'):
            item.delete()
