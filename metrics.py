import pandas as pd

def calculate_performance_metrics(data: pd.DataFrame):

    if data.empty:
        raise ValueError('Cannot calculate metrics: empty DataFrame')
    
    total_market_return = data['Cumulative_Market'].iloc[-1] - 1

    total_strategy_return = data['Cumulative_Strategy'].iloc[-1] - 1

    sharpe_ratio = (
        data['Strategy_Return'].mean() 
        / data['Strategy_Return'].std()
        ) * (252**0.5)
    
    running_max = data['Cumulative_Strategy'].cummax()
    drawdown = (
        data['Cumulative_Strategy'] - running_max
        ) / running_max
    max_drawdown = drawdown.min()

    number_of_trades = int(data['Trade'].sum())

    winning_days = (
        data['Strategy_Return'] > 0
    ).sum()

    losing_days = (
        data['Strategy_Return'] < 0
    ).sum()

    if (winning_days + losing_days) > 0:
        win_rate = winning_days / (winning_days + losing_days)
    else:
        win_rate = float('nan')

    metrics = {
        'Market Return (Buy and Hold)': total_market_return,
        'Strategy Total Return': total_strategy_return,
        'Sharpe Ratio': sharpe_ratio,
        'Maximum Drawdown': max_drawdown,
        'Number of Trades': number_of_trades,
        'Win Rate': win_rate
    }
    
    return metrics