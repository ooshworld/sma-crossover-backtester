from config import TICKER, START_DATE, END_DATE, FAST_SMA, SLOW_SMA, COMMISSION
from data_loader import download_data
from strategy import generate_signals
from backtest import run_backtest
from metrics import calculate_performance_metrics
from plotting import plot_results



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

    data = generate_signals(
        data,
        FAST_SMA,
        SLOW_SMA
    )

    data = run_backtest(
        data,
        COMMISSION
    )

    metrics = calculate_performance_metrics(data)
    print_metrics(metrics)

    plot_results(data, TICKER, FAST_SMA, SLOW_SMA)


if __name__ == "__main__":
    main()