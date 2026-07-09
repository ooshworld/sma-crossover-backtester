# sma-crossover-backtester
# Overview
Python backtester for a simple moving average crossover strategy using historical data.

# Features
- Downloads historical price data
- Calculates SMA indicators
- Generates buy/sell signals
- Plots and calculates cumulative strategy vs. cumulative market returns
- Plots stock price along with SMA indicator lines and buy/sell signals
- Calculates sharpe ratio
- Calculates maximum drawdown

# Technologies
- Python
- Pandas
- matplotlib
- yfinance

## Strategy Performance
![Performance](images/sma_crossover_GOOGL_15_35.png)

## Buy/Sell Signals
![Signals](images/sma_crossover_signals_GOOGL_15_35.png)

## SMA Parameter Optimisation

The optimiser evaluates every fast/slow SMA combination and ranks them based on Sharpe Ratio.

A heatmap is created:

![Heatmap](optimisation_results/GOOGL_heatmap.png)