import datetime
import pandas as pd
import re
from common.clients import AwsClient

def query_stockdb_get_s3_filename():
    query = 'SELECT * FROM amznamzn LIMIT 5'
    filename = AwsClient.query_athena_get_s3_file(query)
    return filename

file_name = query_stockdb_get_s3_filename()
print(file_name)

new_file = AwsClient.get_csv_from_s3(file_name)
print(new_file)
# AwsClient.clean_up_query_folder()