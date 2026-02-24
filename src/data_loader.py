import yfinance as yf
import pandas as pd

def load_data():
    ticker = "GC=F"

    # 1h data is limited to ~730 days on Yahoo
    data = yf.download(ticker, period="730d", interval="1h", auto_adjust=False)

    # If yfinance returns MultiIndex columns, flatten them
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns]  # keep 'Open','High','Low','Close','Volume'

    data.dropna(inplace=True)

    print("Downloaded rows:", len(data))
    return data