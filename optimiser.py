import os
import pandas as pd

from strategy import generate_signals
from backtest import run_backtest
from metrics import calculate_performance_metrics

def optimise_sma(
        data: pd.DataFrame,
        fast_range: range,
        slow_range: range,
        commission: float = 0.001,
        metric: str = 'Sharpe Ratio'
):
    results = []

    for fast in fast_range:
        for slow in slow_range:
            if fast >= slow:
                continue

            strategy_data = generate_signals(
                data.copy(),
                fast,
                slow
            )

            strategy_data = run_backtest(
                strategy_data,
                commission
            )

            metrics = calculate_performance_metrics(
                strategy_data
            )

            metrics['Fast SMA'] = fast
            metrics['Slow SMA'] = slow

            results.append(metrics)

    results = pd.DataFrame(results)

    results = results.sort_values(
        by=metric,
        ascending=False
    )

    os.makedirs('optimisation_results', exist_ok=True)

    results.to_csv(
        'optimisation_results/sma_optimisation.csv',
        index=False
    )

    print('\n========== TOP 10 STRATEGIES ==========\n')

    print(
        results[
            [
                'Fast SMA',
                'Slow SMA',
                metric,
                'Strategy Total Return',
                'Maximum Drawdown'
            ]
        ].head(10)
    )

    return results