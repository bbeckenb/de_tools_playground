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
    today_date = datetime.datetime.today().strftime('%Y-%m-%d')
    s3_obj_name = f'amzn/{today_date}.csv'
    AwsClient.s3_res.Object(bucket_name, s3_obj_name).put(Body=csv_buffer.getvalue())
    print('success')

def send_stock_data_to_S3():
    data = get_stock_data('AMZN')
    write_to_s3(data)



