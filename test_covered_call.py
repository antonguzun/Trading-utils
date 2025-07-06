from covered_call import calc_cash_returns, calc_margin_returns


def test_calc_cash_returns():
    res = calc_cash_returns(
        shares=500,
        stock_price=43.0,
        strike_price=45.0,
        option_price=3.0,
        dividends=500.0,
        comm_stock_buy=320.0,
        comm_stock_sell=330.0,
        comm_option_sell=60.0,
    )
    assert round(res.net_investment, 2) == 20380.0
    assert round(res.return_if_exercised, 2) == 11.24
    assert round(res.return_if_unchanged, 2) == 7.95
    assert round(res.break_even, 2) == 39.76
    assert round(res.downside_protection, 2) == 7.53


def test_calc_margin_returns():
    res = calc_margin_returns(
        shares=500,
        stock_price=43.0,
        strike_price=45.0,
        option_price=3.0,
        dividends=500.0,
        comm_stock_buy=320.0,
        comm_stock_sell=330.0,
        comm_option_sell=60.0,
        margin_rate=0.50,
        interest_rate=0.10,
        months=6,
    )
    assert round(res.net_investment, 2) == 9470.0
    assert round(res.return_if_exercised, 2) == 18.42
    assert round(res.return_if_unchanged, 2) == 11.35
    assert round(res.break_even, 3) == 40.851
    assert round(res.downside_protection, 2) == 5.0
