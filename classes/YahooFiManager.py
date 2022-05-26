from datetime import date
import pandas as pd
import yfinance as yf

class YahooFiManager:
    def get_stock_df(self, tickers:str, start: date, end: date) -> pd.DataFrame:
        '''takes in all caps string of stock tickers separated by spaces, retur'''
        return yf.download(tickers, start=start, end=end)