import numpy as np
import pandas as pd

def performance_metrics(returns: pd.Series, freq_per_year: int) -> dict:
    """
    Metrics computed from periodic returns (not prices).
    returns: strategy returns per bar (e.g., hourly)
    """
    returns = returns.dropna()

    # Equity from returns
    equity = (1 + returns).cumprod()

    total_return = equity.iloc[-1] / equity.iloc[0] - 1

    ann_vol = returns.std() * np.sqrt(freq_per_year)

    sharpe = np.nan
    if returns.std() != 0:
        sharpe = (returns.mean() / returns.std()) * np.sqrt(freq_per_year)

    peak = equity.cummax()
    drawdown = equity / peak - 1
    max_dd = drawdown.min()

    return {
        "Total Return": total_return,
        "Annualized Vol": ann_vol,
        "Sharpe": sharpe,
        "Max Drawdown": max_dd,
    }


def buy_hold_metrics(close: pd.Series, freq_per_year: int) -> dict:
    close = close.dropna()
    rets = close.pct_change().dropna()
    return performance_metrics(rets, freq_per_year=freq_per_year)