import pandas as pd
import yfinance as yf

def download_data(
        ticker: str,
        start_date: str,
        end_date: str
):
    """
    Downloads historical stock data for the specified ticker and date range using yfinance.
    """
    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False
    )
    if data.empty:
        raise ValueError(f"No data found for ticker {ticker} between {start_date} and {end_date}.")
    return data