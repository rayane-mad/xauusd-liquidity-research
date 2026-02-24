import os
import matplotlib.pyplot as plt

from data_loader import load_data
from session_analysis import label_session, session_volatility
from strategy import breakout_strategy
from backtester import backtest
from metrics import performance_metrics, buy_hold_metrics


def main():
    df = load_data()
    df = label_session(df)

    print("Session Volatility:")
    print(session_volatility(df))
    #--------tested: windows=50,100,20
    df = breakout_strategy(df, window=100, session_only=None)
    #--------
    df = backtest(df, cost_per_trade=0.0001)  # test with small cost

    freq_per_year = 252 * 24  # hourly bars

    strategy_metrics = performance_metrics(
        df["strategy_returns"], freq_per_year=freq_per_year
    )
    benchmark_metrics = buy_hold_metrics(
        df["Close"], freq_per_year=freq_per_year
    )

    print("\nStrategy Metrics:")
    for k, v in strategy_metrics.items():
        print(f"{k}: {v:.4f}")

    print("\nBuy & Hold Metrics:")
    for k, v in benchmark_metrics.items():
        print(f"{k}: {v:.4f}")

    # Plot equity
    equity_curve = df["equity_curve"].dropna()

    os.makedirs("outputs", exist_ok=True)
    plt.figure(figsize=(10, 5))
    equity_curve.plot(title="Strategy Equity Curve")
    plt.tight_layout()
    plt.savefig("outputs/equity_curve.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    main()