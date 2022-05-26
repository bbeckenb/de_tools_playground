import datetime
from common.clients import YahooClient

def get_stock_data(tickers):
    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(1)
    data = YahooClient.get_stock_df(tickers=tickers,
                                    start=yesterday,
                                    end=today)
    print(data)

print(get_stock_data('AMZN'))
