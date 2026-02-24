def label_session(df):
    df = df.copy()
    df["hour"] = df.index.hour
    
    def get_session(hour):
        if 0 <= hour < 8:
            return "Asia"
        elif 8 <= hour < 16:
            return "London"
        else:
            return "NewYork"
    
    df["session"] = df["hour"].apply(get_session)
    
    return df

def session_volatility(df):
    # std of hourly returns is better than std of price levels
    df = df.copy()
    df["ret"] = df["Close"].pct_change()
    return df.groupby("session")["ret"].std()