"""Scenario table generation."""

from __future__ import annotations

from typing import Sequence

import numpy as np
import pandas as pd

from payoff_plot import payoff_values


def make_scenarios(
    terminal_prices: Sequence[float],
    stock_price: float,
    strike_price: float,
    premium: float,
) -> pd.DataFrame:
    """Return DataFrame comparing covered call and buy-and-hold."""
    prices = np.array(terminal_prices, dtype=float)
    cc = payoff_values(stock_price, strike_price, premium, prices)
    bh = prices - stock_price
    df = pd.DataFrame({"Terminal Price": prices, "Covered Call": cc, "Buy & Hold": bh})
    return df
