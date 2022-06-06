import datetime
import pandas as pd
import re
from common.clients import AwsClient

def query_stockdb_get_s3_filename():
    query = 'SELECT * FROM amznamzn LIMIT 5'
    filename = AwsClient.query_athena_get_s3_file(query)
    return filename

def get_file_send_email():
    file_name = query_stockdb_get_s3_filename()

    new_file = AwsClient.get_csv_from_s3(file_name)

    AwsClient.clean_up_query_folder()

    AwsClient.ses_send_email(new_file)

