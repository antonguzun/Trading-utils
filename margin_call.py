"""Margin call calculator."""

from __future__ import annotations


def margin_call_price(
    stock_price: float, margin_rate: float, maintenance: float
) -> tuple[float, float]:
    """Return critical price and drawdown percentage triggering margin call."""
    debit = stock_price * (1 - margin_rate)
    critical = debit / (1 - maintenance)
    drawdown = (stock_price - critical) / stock_price * 100
    return critical, drawdown
