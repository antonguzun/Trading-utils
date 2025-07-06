"""Payoff diagram utilities."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def payoff_values(
    stock_price: float, strike_price: float, premium: float, prices: np.ndarray
) -> np.ndarray:
    """Compute net P/L for a covered call at given terminal prices."""
    return np.where(
        prices > strike_price,
        strike_price - stock_price + premium,
        prices - stock_price + premium,
    )


def plot_payoff(
    stock_price: float,
    strike_price: float,
    premium: float,
    prices: np.ndarray | None = None,
) -> None:
    """Plot payoff diagram for a covered call."""
    if prices is None:
        prices = np.linspace(stock_price * 0.5, stock_price * 1.5, 100)
    pl = payoff_values(stock_price, strike_price, premium, prices)
    break_even = stock_price - premium
    max_gain = strike_price - stock_price + premium

    fig, ax = plt.subplots()
    ax.plot(prices, pl, label="Covered Call")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(break_even, color="gray", linestyle="--", linewidth=0.8)
    ax.axhline(max_gain, color="gray", linestyle=":", linewidth=0.8)
    ax.annotate(
        "Max Gain", xy=(prices[-1], max_gain), xytext=(0, 5), textcoords="offset points"
    )
    ax.annotate(
        "Break-even", xy=(break_even, 0), xytext=(0, -15), textcoords="offset points"
    )
    ax.set_xlabel("Stock Price at Expiration")
    ax.set_ylabel("Net P/L")
    ax.legend()
    plt.show()
