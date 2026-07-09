import pandas as pd

def generate_signals(
        data: pd.DataFrame,
        fast_sma: int,
        slow_sma: int
):
    data = data.copy()

    data['SMA_fast'] = data['Close'].rolling(window=fast_sma).mean()

    data['SMA_slow'] = data['Close'].rolling(window=slow_sma).mean()

    data['Signal'] = (data['SMA_fast'] > data['SMA_slow']).astype(int)

    data['Position'] = data['Signal'].diff()

    data['Trade'] = data['Position'].abs()

    data['Buy'] = data['Position'] == 1

    data['Sell'] = data['Position'] == -1

    return data