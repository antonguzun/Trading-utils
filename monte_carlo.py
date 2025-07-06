"""Monte-Carlo simulator for covered calls."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from payoff_plot import payoff_values


def simulate(
    S0: float,
    mu: float,
    sigma: float,
    strike: float,
    premium: float,
    years: float,
    paths: int,
) -> np.ndarray:
    """Simulate terminal P/L paths."""
    steps = int(252 * years)
    dt = years / steps
    prices = np.full(paths, S0)
    for _ in range(steps):
        z = np.random.normal(size=paths)
        prices *= np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
    pl = payoff_values(S0, strike, premium, prices)
    return pl


def stats(data: np.ndarray) -> dict[str, float]:
    """Return summary statistics for simulated P/L."""
    mean = float(np.mean(data))
    median = float(np.median(data))
    var = float(np.percentile(data, 5))
    es = float(data[data <= var].mean())
    return {"mean": mean, "median": median, "VaR95": var, "ES95": es}


def plot_hist(data: np.ndarray, bins: int = 50) -> None:
    plt.hist(data, bins=bins, color="steelblue", edgecolor="black")
    plt.xlabel("P/L")
    plt.ylabel("Frequency")
    plt.show()
