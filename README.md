# sma-crossover-backtester
# Overview

A modular Python backtesting framework that evaluates a simple moving average (SMA) crossover strategy using historical price data from Yahoo Finance.

The project simulates trading performance, calculates key performance metrics, visualises buy/sell signals, and performs parameter optimisation across multiple fast/slow SMA combinations.

# Features
- Downloads historical market data using Yahoo Finance
- Configurable fast/slow SMA periods
- Calculates SMA indicators
- Generates buy/sell signals
- Backtests with trading commission
- Plots cumulative strategy vs. cumulative market equity curves
- Plots stock price chart along with SMA indicator lines and buy/sell signals
- Calculates sharpe ratio, maximum drawdown, number of trades and win rate
- Optimiser ranks fast/slow SMA combinations via Sharpe Ratio
- Optimiser generates heatmap showing strategy performance across SMA combinations
- Modular structure

# Technologies
- Python
- Pandas
- matplotlib
- yfinance

# Strategy Performance
![Performance](images/sma_crossover_GOOGL_15_35.png)

# Buy/Sell Signals
![Signals](images/sma_crossover_signals_GOOGL_15_35.png)

# SMA Parameter Optimisation

The optimiser evaluates every fast/slow SMA combination and ranks them based on Sharpe Ratio.

A heatmap is created:

![Heatmap](optimisation_results/GOOGL_heatmap.png)

# Performance Metrics

- Buy & Hold Return
- Strategy Total Return
- Sharpe Ratio
- Maximum Drawdown
- Win Rate
- Number of Trades

## Future Improvements

- Walk-forward optimisation
- Support for multiple technical indicators
- Position sizing and risk management
- Interactive dashboard