def breakout_strategy(df, window: int = 20, session_only: str = "London"):
    df = df.copy()

    # Rolling breakout levels
    df["rolling_high"] = df["High"].rolling(window=window).max()
    df["rolling_low"] = df["Low"].rolling(window=window).min()

    # Long-only signal: enter on breakout, otherwise flat
    df["signal"] = 0
    df.loc[df["Close"] > df["rolling_high"].shift(1), "signal"] = 1

    # Optional session filter applied LAST
    if session_only is not None:
        df.loc[df["session"] != session_only, "signal"] = 0

    return df