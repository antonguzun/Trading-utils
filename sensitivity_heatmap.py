"""Heatmap utilities for price/time sensitivity."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from payoff_plot import payoff_values


def heatmap(
    stock_price: float,
    strike_price: float,
    premium: float,
    weeks: int,
    price_range: tuple[float, float] | None = None,
) -> None:
    """Plot heatmap of expected P/L over price and time."""
    if price_range is None:
        price_range = (stock_price * 0.5, stock_price * 1.5)
    prices = np.linspace(price_range[0], price_range[1], 50)
    weeks_arr = np.arange(weeks + 1)
    pl_matrix = np.zeros((len(weeks_arr), len(prices)))
    for i, wk in enumerate(weeks_arr):
        decay = (weeks - wk) / weeks
        pl_matrix[i] = payoff_values(stock_price, strike_price, premium * decay, prices)

    fig, ax = plt.subplots()
    im = ax.imshow(
        pl_matrix,
        extent=[prices[0], prices[-1], 0, weeks],
        origin="lower",
        aspect="auto",
        cmap="coolwarm",
    )
    ax.set_xlabel("Price")
    ax.set_ylabel("Weeks to Expiration")
    fig.colorbar(im, ax=ax, label="P/L")
    plt.show()
