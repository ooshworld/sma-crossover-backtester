import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

TICKER = "AAPL"
START_DATE = "2020-01-01"
END_DATE = "2026-01-01"

FAST_SMA = 15
SLOW_SMA = 35

COMMISSION = 0.001

def download_data():
    """
    Downloads historical stock data for the specified ticker and date range using yfinance.
    """
    data = yf.download(TICKER, start=START_DATE, end=END_DATE)
    return data

def calculate_signals(data):
    """
    Calculates fast and slow simple moving averages and SMA crossover signals for the given data.

    Returns:
        DataFrame with SMA indicators and buy/sell signals.

    """
    data['SMA_fast'] = data['Close'].rolling(window=FAST_SMA).mean()
    data['SMA_slow'] = data['Close'].rolling(window=SLOW_SMA).mean()
    data['Signal'] = (
        data['SMA_fast'] > data['SMA_slow']
    ).astype(int)
    data['Position'] = data['Signal'].diff()
    data['Buy'] = data['Position'] == 1
    data['Sell'] = data['Position'] == -1
    data['Trade'] = data['Position'].abs()
    return data

def run_backtest(data):
    """
    Runs a backtest on the given data using the SMA crossover strategy.
    
    Returns:
        DataFrame with cumulative returns for both the market and the strategy.
    """
    data['TRADING_COST'] = data['Trade'] * COMMISSION
    data['Return'] = data['Close'].pct_change()
    data['Strategy_Return'] = (data['Signal'].shift(1) * data['Return']) - data['TRADING_COST']
    data['cumulative_market'] = (1 + data['Return']).cumprod()
    data['cumulative_strategy'] = (1 + data['Strategy_Return']).cumprod()
    return data


def plot_results(data):
    """"
    Plots cumulative returns of the market and the strategy.

    Plots stock price of ticker along with SMA indicator lines and buy/sell signals.
    """
    plt.figure(figsize=(12,6))
    plt.plot(
        data.index,
        data['cumulative_market'],
        label='Market (buy and hold)'
    )

    plt.plot(
        data.index,
        data['cumulative_strategy'],
        label='SMA Strategy'
    )

    plt.title(f'SMA Crossover Backtest on {TICKER}')
    plt.ylabel('Growth of $1 Investment')
    plt.xlabel('Date')
    plt.legend()
    plt.show()

    plt.figure(figsize=(12,6))
    plt.plot(
        data.index,
        data['Close'],
        label='Close Price'
    )

    plt.plot(
        data.index,
        data['SMA_fast'],
        label=f'SMA {FAST_SMA}'
    )

    plt.plot(
        data.index,
        data['SMA_slow'],
        label=f'SMA {SLOW_SMA}'
    )

    plt.scatter(
        data.loc[data['Buy']].index,
        data.loc[data['Buy'], 'Close'],
        marker="^",
        color="green",
        s=70,
        label="Buy"
    )

    plt.scatter(
        data.loc[data['Sell']].index,
        data.loc[data['Sell'], 'Close'],
        marker="v",
        color="red",
        s=70,
        label="Sell"
    )

    plt.title('Stock Price with SMA lines and Buy/Sell Signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.savefig(
        f'images/sma_crossover_{TICKER}_{START_DATE}_to_{END_DATE}.png',
        dpi=300,
        bbox_inches='tight'
    )
    plt.show()

def calculate_performance_metrics(data):
    """
    Calculates performance metrics for the strategy.

    Returns:
        Market Return (Buy & Hold)
        Strategy Return
        Sharpe Ratio
        Number of Trades
        Maximum Drawdown
    """
    total_market_return = data['cumulative_market'].iloc[-1] - 1
    total_strategy_return = data['cumulative_strategy'].iloc[-1] - 1
    sharpe_ratio = (data['Strategy_Return'].mean() / data['Strategy_Return'].std()) * (252**0.5)
    running_max = data['cumulative_strategy'].cummax()
    drawdown = (data['cumulative_strategy'] - running_max) / running_max
    max_drawdown = drawdown.min()
    number_of_trades = int(data['Trade'].sum())
    print(f"Market Return: {total_market_return:.2%}")
    print(f"Strategy Return: {total_strategy_return:.2%}")
    print(f"Strategy Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Number of Trades: {number_of_trades}")
    print(f"Maximum Drawdown: {max_drawdown:.2%}")

def main():
    data = download_data()
    data = calculate_signals(data)
    data = run_backtest(data)
    calculate_performance_metrics(data)
    plot_results(data)

if __name__ == "__main__":
    main()