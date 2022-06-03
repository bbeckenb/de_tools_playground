import datetime
import pandas as pd
import re
from common.clients import AwsClient

def query_stockdb_get_s3_filename():
    query = 'SELECT * FROM amznamzn LIMIT 5'
    filename = AwsClient.query_athena_get_s3_file(query)
    return filename

# print(query_stockdb_get_s3_filename())
AwsClient.clean_up_query_folder()