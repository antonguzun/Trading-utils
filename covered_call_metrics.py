"""Core metrics for covered call analysis."""

from __future__ import annotations


def break_even(
    stock_price: float,
    option_premium: float,
    dividends: float = 0.0,
    commissions: float = 0.0,
) -> float:
    """Return the break-even stock price per share."""
    return stock_price - option_premium - dividends + commissions


def roi(total_profit: float, capital: float, years: float = 1.0) -> tuple[float, float]:
    """Return total and annualized return on investment (ROI)."""
    total = total_profit / capital
    annualized = (1 + total) ** (1 / years) - 1 if years else total
    return total, annualized


def return_on_risk(profit: float, margin_at_risk: float) -> float:
    """Return profit divided by margin capital at risk."""
    return profit / margin_at_risk
