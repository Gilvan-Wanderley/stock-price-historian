import yfinance as yf
import pandas as pd
from datetime import datetime

class FinanceService:
    def __init__(self, ticker: yf.Ticker) -> None:
        self._ticker = ticker

    def history(self, stock_name: str, start: datetime, end: datetime) -> pd.DataFrame | None:
        ticker = self._ticker(stock_name)
        try:
            df = ticker.history(start=start, end=end, interval="1h")
            return None if df.empty else df
        except:
            raise Exception(f"Invalid request history for {stock_name}.")
        
    def get_data(self, index: datetime.timestamp, row: pd.Series) -> dict:
        return {            
            "open": row["Open"],
            "high": row["High"],
            "low": row["Low"],
            "close": row["Close"],
            "volume": row["Volume"],
            "dividends": row["Dividends"],
            "stock_splits": row["Stock Splits"],
            "datetime": str(index)}