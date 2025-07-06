"""Compute Black-Scholes Greeks for a European call."""

from __future__ import annotations

import math
from dataclasses import dataclass

from scipy.stats import norm


@dataclass
class Greeks:
    delta: float
    theta: float
    gamma: float
    net_delta: float


def _d1(S: float, K: float, r: float, sigma: float, t: float) -> float:
    return (math.log(S / K) + (r + 0.5 * sigma**2) * t) / (sigma * math.sqrt(t))


def _d2(d1: float, sigma: float, t: float) -> float:
    return d1 - sigma * math.sqrt(t)


def call_greeks(
    S: float, K: float, r: float, sigma: float, t: float, shares: int = 100
) -> Greeks:
    """Return option delta, theta, gamma, and net position delta."""
    d1 = _d1(S, K, r, sigma, t)
    d2 = _d2(d1, sigma, t)
    delta = norm.cdf(d1)
    theta = (
        -(
            S * norm.pdf(d1) * sigma / (2 * math.sqrt(t))
            + r * K * math.exp(-r * t) * norm.cdf(d2)
        )
        / 365
    )
    gamma = norm.pdf(d1) / (S * sigma * math.sqrt(t))
    net_delta = shares - delta * shares / 100
    return Greeks(delta, theta, gamma, net_delta)
