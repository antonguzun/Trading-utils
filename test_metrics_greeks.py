from covered_call_metrics import break_even, roi, return_on_risk
from option_greeks import call_greeks


def test_break_even():
    assert break_even(50, 2, dividends=1) == 47


def test_roi():
    total, annual = roi(10, 100, years=1)
    assert round(total, 2) == 0.10
    assert round(annual, 2) == 0.10


def test_return_on_risk():
    assert return_on_risk(5, 50) == 0.1


def test_call_greeks():
    g = call_greeks(50, 55, 0.01, 0.2, 0.5)
    assert round(g.delta, 3) == round(g.delta, 3)  # ensure numeric
    assert round(g.gamma, 3) > 0
