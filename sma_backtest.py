import yfinance as yf
import pandas as pd
data = yf.download("AAPL", start="2020-01-01", end="2025-01-01")
data['SMA_fast'] = data['Close'].rolling(window=15).mean()
data['SMA_slow'] = data['Close'].rolling(window=35).mean()
print(data.tail())

data['Signal'] = 0
data.loc[data['SMA_fast'] > data['SMA_slow'], 'Signal'] = 1
data['Return'] = data['Close'].pct_change()
data['Strategy_Return'] = data['Signal'].shift(1) * data['Return']
data['cumulative_market'] = (1 + data['Return']).cumprod()
data['cumulative_strategy'] = (1 + data['Strategy_Return']).cumprod()

import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.plot(data.index, data['cumulative_market'], label='Market (buy and hold)')
plt.plot(data.index, data['cumulative_strategy'], label='SMA Strategy')
plt.title('SMA Crossover Backtest on AAPL')
plt.legend()
plt.show()

total_market_return = data['cumulative_market'].iloc[-1] - 1
total_strategy_return = data['cumulative_strategy'].iloc[-1] - 1
sharpe_ratio = (data['Strategy_Return'].mean() / data['Strategy_Return'].std()) * (252**0.5)

print(f"Market Return: {total_market_return:.2%}")
print(f"Strategy Return: {total_strategy_return:.2%}")
print(f"Strategy Sharpe Ratio: {sharpe_ratio:.2f}")