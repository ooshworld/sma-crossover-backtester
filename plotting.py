import os
import matplotlib.pyplot as plt
import pandas as pd


def plot_results(
        data: pd.DataFrame,
        ticker: str,
        fast_sma: int,
        slow_sma: int,
        save_images: bool = True
):
    
    plt.figure(figsize=(12,6))

    plt.plot(
        data.index,
        data['Cumulative_Market'],
        linewidth=2,
        label='Market (buy and hold)'
    )

    plt.plot(
        data.index,
        data['Cumulative_Strategy'],
        linewidth=2,
        label='SMA Strategy'
    )

    plt.title(f'{ticker} - Strategy Performance')
    plt.xlabel('Date')
    plt.ylabel('Growth of $1 Investment')
    plt.grid(True, alpha=0.3)
    plt.legend()

    if save_images:
        plt.savefig(
            f'images/sma_crossover_{ticker}_{fast_sma}_{slow_sma}.png',
            dpi=300,
            bbox_inches='tight'
        )
    
    plt.show()


    plt.figure(figsize=(14,7))

    plt.plot(
        data.index,
        data['Close'],
        linewidth=2,
        label='Close Price'
    )

    plt.plot(
        data.index,
        data['SMA_fast'],
        linewidth=2,
        label=f'{fast_sma}-day SMA'
    )

    plt.plot(
        data.index,
        data['SMA_slow'],
        linewidth=2,
        label=f'{slow_sma}-day SMA'
    )

    plt.scatter(
        data.loc[data['Buy']].index,
        data.loc[data['Buy'], 'Close'],
        marker="^",
        color="green",
        label='Buy',
        zorder=5
    )

    plt.scatter(
        data.loc[data['Sell']].index,
        data.loc[data['Sell'], 'Close'],
        marker="v",
        color="red",
        label='Sell',
        zorder=5
    )

    plt.title(
        f'{ticker} Stock Price with {fast_sma}/{slow_sma} SMA Crossover Signals'
    )

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True, alpha=0.3)
    plt.legend()

    if save_images:
        plt.savefig(
            f'images/sma_crossover_signals_{ticker}_{fast_sma}_{slow_sma}.png',
            dpi=300,
            bbox_inches='tight'
        )

    plt.show()
