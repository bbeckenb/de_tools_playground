import csv
import datetime
from io import StringIO
import pandas as pd
from common.clients import YahooClient, AwsClient

def get_stock_data(tickers) -> pd.DataFrame:
    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(1)
    data = YahooClient.get_stock_df(tickers=tickers,
                                    start=yesterday,
                                    end=today)
    return data

def write_to_s3(data: pd.DataFrame) -> None:
    csv_buffer = StringIO()
    data.to_csv(csv_buffer)
    bucket_name = 'brycepracticebucket'
    s3_obj_name = 'test.csv'
    AwsClient.s3_res.Object(bucket_name, s3_obj_name).put(Body=csv_buffer.getvalue())
    print('success!')

data = get_stock_data('AMZN')
print(write_to_s3(data))
