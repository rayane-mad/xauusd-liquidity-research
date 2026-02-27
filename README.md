Gold Futures Session Breakout Research
======================================

### Structural Robustness Analysis of Intraday Breakout Dynamics in GC=F (2020–2024)

Research Objective
------------------

This project investigates whether intraday breakout strategies exhibit structural robustness across global trading sessions (Asia, London, New York) using 1-hour gold futures data.

The goal is not strategy optimization, but structural evaluation:

*   Do breakout signals represent persistent structural alpha?
    
*   Or are they primarily driven by microstructure noise and volatility clustering?
    

Dataset
-------

*   Instrument: Gold Futures (GC=F)
    
*   Frequency: 1-hour bars
    
*   Period: 2020–2024
    
*   Source: Yahoo Finance (yfinance)
    
*   Session Segmentation:
    
    *   Asia
        
    *   London
        
    *   New York
        

All backtests are fully vectorized using pandas.

Strategy Framework
------------------

### Long-Only Breakout Logic

For each bar:

1.  Compute rolling high over N periods
    
2.  Enter long when:Close > rolling\_high.shift(1)
    
3.  Exit when condition no longer holds
    

Transaction costs are applied per trade.

Structural Windows Tested
-------------------------

To evaluate noise sensitivity and structural persistence:

*   20-bar window → Short-term breakout (noise-sensitive)
    
*   50-bar window → Medium-term breakout
    
*   100-bar window → Long-term structural breakout
    

Benchmark comparison:

*   Passive Buy & Hold over identical period
    

Results Summary
---------------

### All Sessions Combined (Long Only)

WindowTotal ReturnSharpeMax Drawdown202.95%0.25-9.03%503.27%0.31-6.71%1006.24%0.60-4.30%Buy & Hold180%2.39-16.36%

### Interpretation of Window Scaling

*   Sharpe improves as breakout window increases.
    
*   Drawdown decreases as short-term noise is filtered.
    
*   Even at 100 bars, breakout underperforms passive drift.
    

This suggests:Breakout effectiveness improves as microstructure noise is removed, but gold’s long-term upward drift dominates active breakout logic.

Session Volatility Analysis
---------------------------

Observed session volatility:

SessionVolatilityAsia0.002247London0.002809New York0.002557

London session exhibits the highest volatility.

However:Higher volatility did not translate into improved breakout performance.

Conclusion:Volatility expansion alone does not imply structural edge.

Session-Based Breakout Testing
------------------------------

Breakout performance was evaluated under:

*   All sessions combined
    
*   London-only filtering
    
*   Cross-session comparison
    

Findings:

*   London session shows highest volatility but not superior Sharpe.
    
*   Session filtering does not convert breakout logic into structural alpha.
    
*   Short windows are heavily influenced by intraday noise across all sessions.
    

Performance Metrics Calculated
------------------------------

*   Total Return
    
*   Annualized Volatility
    
*   Sharpe Ratio (rough)
    
*   Maximum Drawdown
    
*   Equity Curve
    

Project Structure
-----------------

xauusd-liquidity-research/

*   src/
    
    *   data\_loader.py
        
    *   session\_analysis.py
        
    *   strategy.py
        
    *   backtester.py
        
    *   metrics.py
        
    *   main.py
        
*   data/
    
*   notebooks/
    
*   outputs/
    
    *   equity\_curve.png
        
*   requirements.txt
    
*   README.md
    

Running the Project
-------------------

Activate environment:

source venv/bin/activate

Run:

python src/main.py

Limitations
-----------

*   No slippage modeling
    
*   No execution modeling
    
*   No walk-forward validation
    
*   No out-of-sample testing
    
*   No regime-switching model
    
*   Static position sizing
    

Key Structural Insights
-----------------------

1.  Short-horizon breakout is noise-dominated20-bar structures show weak risk-adjusted performance.
    
2.  Window scaling improves stabilityMoving from 20 → 50 → 100 bars consistently improves Sharpe and reduces drawdown.
    
3.  Gold’s structural drift dominatesPassive exposure significantly outperforms breakout logic.
    
4.  Volatility ≠ alphaHigher session volatility does not imply stronger breakout signals.
    

Conclusion
----------

Hourly breakout strategies in gold futures demonstrate improved statistical stability as structural windows increase, indicating partial noise-filtering behavior.

However, breakout logic fails to generate persistent structural alpha relative to passive exposure.

The evidence supports the view that intraday breakout behavior in GC=F is influenced more by volatility clustering and drift than by exploitable structural inefficiencies.
