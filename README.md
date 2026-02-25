# Gold Futures: Structural Breakout Robustness Study  
### *An empirical analysis of intraday trend persistence in GC=F (2020–2024).*

---

## Research Objective

This study investigates whether intraday breakout strategies exhibit structural robustness across global trading sessions (**Asia, London, New York**).

Rather than optimizing for profitability, the objective is to evaluate whether breakout signals represent **persistent structural alpha** or are primarily driven by **microstructure noise and volatility clustering**.

---

## Dataset & Experimental Scope

- **Instrument:** Gold Futures (GC=F)  
- **Frequency:** 1-hour bars  
- **Period:** 2020–2024  
- **Data Source:** Yahoo Finance (`yfinance`)  
- **Session Segmentation:** Asia / London / New York  

All tests are executed using vectorized pandas operations with transaction costs applied.

---

## Methodology

### Strategy Framework — Long-Only Breakout

For each time step:

- Compute rolling high over window **N**
- Enter long when:
Close_t > RollingHigh_{t-1}

- Exit when condition no longer holds  
- Transaction costs incorporated  
- Fully vectorized backtesting engine  

### Structural Windows Tested

- 20 bars → Short-term structure (noise-sensitive)  
- 50 bars → Medium-term structure  
- 100 bars → Long-term structural regime shifts  

**Benchmark:** Passive Buy & Hold.

---

## Results Summary

### All Sessions (Aggregated)

| Strategy | Total Return | Sharpe Ratio | Max Drawdown |
|----------|--------------|--------------|--------------|
| 20-Bar Breakout | 2.95% | 0.25 | -9.03% |
| 50-Bar Breakout | 3.27% | 0.31 | -6.71% |
| 100-Bar Breakout | 6.24% | 0.60 | -4.30% |
| Buy & Hold | 180% | 2.39 | -16.36% |

---

## Structural Insights

### 1) Noise Dominance in Short Horizons
20-bar breakouts exhibit weak risk-adjusted performance, suggesting heavy exposure to intraday microstructure noise.

### 2) Monotonic Risk Improvement
Sharpe ratio and drawdown improve consistently as the structural window increases (20 → 50 → 100 bars).  
This indicates breakout effectiveness improves as noise is filtered.

### 3) Alpha vs Drift
Despite structural improvement, breakout strategies significantly underperform Buy & Hold, suggesting gold’s drift component dominates breakout alpha.

### 4) Volatility ≠ Edge
The London session displayed the highest volatility but did not yield superior breakout performance, reinforcing that volatility expansion does not guarantee persistent structural opportunity.

---

## Interpretation

Breakout signals appear to:

- Act as risk filters  
- Reduce drawdown  
- Reduce volatility exposure  
- But fail to generate superior long-run returns  

This suggests structural breakouts may be more suitable as:

- Volatility regime filters  
- Risk overlays  
- Capital allocation constraints  

rather than standalone alpha engines.

---

## Project Architecture
xauusd-liquidity-research/
├── src/
│ ├── data_loader.py
│ ├── session_analysis.py
│ ├── strategy.py
│ ├── backtester.py
│ ├── metrics.py
│ └── main.py
├── outputs/
│ └── equity_curve.png
├── requirements.txt
└── README.md

---

## Running the Project

Activate environment:

```bash
source venv/bin/activate
Execute:
python src/main.py
Limitations
No slippage modeling
No walk-forward validation
No out-of-sample testing
No regime-switching models
No volatility-adjusted sizing
Future Research Directions
Out-of-sample robustness checks
Monte Carlo trade reshuffling
Transaction cost sensitivity analysis
Regime classification models
Rolling window Sharpe stability tracking
Volatility-adjusted breakout thresholds
Conclusion
Intraday breakouts in GC=F demonstrate improved risk-adjusted characteristics as structural windows increase, but fail to outperform passive exposure.
The evidence suggests that breakout dynamics at hourly frequencies are partially driven by volatility clustering rather than persistent structural inefficiencies.
