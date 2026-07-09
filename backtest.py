import pandas as pd

def run_backtest(
        data: pd.DataFrame,
        commission: float = 0.001
):
    data = data.copy()

    data['Return'] = data['Close'].pct_change()

    data = data.dropna()

    if data.empty:
        return data

    data['Trading_Cost'] = data['Trade'] * commission

    data['Strategy_Return'] = (
        data['Signal'].shift(1) * data['Return']
        ) - data['Trading_Cost']
    
    data['Strategy_Return'] = data['Strategy_Return'].fillna(0)

    data['Cumulative_Market'] = (
        1 + data['Return']
        ).cumprod()

    data['Cumulative_Strategy'] = (
        1 + data['Strategy_Return']
        ).cumprod()

    return data