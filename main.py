from config import TICKER, START_DATE, END_DATE, FAST_SMA, SLOW_SMA, COMMISSION, FAST_RANGE, SLOW_RANGE, RUN_OPTIMISER
from data_loader import download_data
from strategy import generate_signals
from backtest import run_backtest
from metrics import calculate_performance_metrics
from plotting import plot_results
from optimiser import optimise_sma



def print_metrics(metrics: dict):

    print('\n========== Performance Metrics ==========')

    for key, value in metrics.items():
        if isinstance(value, float):
            if "Return" in key or "Drawdown" in key or "Win Rate" in key:
                print(f"{key:<20}: {value:.2%}")
            else:
                print(f"{key:<20}: {value:.2f}")
        else:
            print(f"{key:<20}: {value}")

def main():
    data = download_data(
        TICKER,
        START_DATE,
        END_DATE
    )

    strategy_data = generate_signals(
        data,
        FAST_SMA,
        SLOW_SMA
    )

    strategy_data = run_backtest(
        strategy_data,
        COMMISSION
    )

    metrics = calculate_performance_metrics(strategy_data)

    print_metrics(metrics)

    plot_results(
        strategy_data, 
        TICKER, 
        FAST_SMA, 
        SLOW_SMA)
    
    if RUN_OPTIMISER:
        optimise_sma(
            data=data,
            fast_range=FAST_RANGE,
            slow_range=SLOW_RANGE,
            commission=COMMISSION,
            metric='Sharpe Ratio'
        )


if __name__ == "__main__":
    main()