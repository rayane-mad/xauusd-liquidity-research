import numpy as np

def backtest(df, cost_per_trade: float = 0.0):
    """
    Simple backtest:
    - signal is assumed to be {0,1} (flat/long). If you later add -1 for short, it still works.
    - cost_per_trade is a fraction (e.g., 0.0001 = 1 bp, 0.001 = 10 bps)
    """
    df = df.copy()

    df["returns"] = df["Close"].pct_change()

    # Position held during bar t is signal from t-1
    df["position"] = df["signal"].shift(1).fillna(0)

    # Raw strategy returns
    df["strategy_returns_gross"] = df["position"] * df["returns"]

    # Trades happen when position changes
    df["trade"] = df["position"].diff().abs().fillna(0)

    # Apply trading costs when trade occurs
    df["cost"] = df["trade"] * cost_per_trade
    df["strategy_returns"] = df["strategy_returns_gross"] - df["cost"]

    # Equity curve
    df["equity_curve"] = (1 + df["strategy_returns"]).cumprod()

    return df