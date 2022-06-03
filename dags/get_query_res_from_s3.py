import datetime
import pandas as pd
import re
from common.clients import AwsClient

def query_stock_data():
    query = 'SELECT * FROM amznamzn LIMIT 5'
    AwsClient.query_athena(query)

query_stock_data()