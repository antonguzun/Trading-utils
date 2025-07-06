from dataclasses import dataclass


@dataclass
class CashResult:
    net_investment: float
    return_if_exercised: float
    return_if_unchanged: float
    break_even: float
    downside_protection: float


@dataclass
class MarginResult:
    net_investment: float
    return_if_exercised: float
    return_if_unchanged: float
    break_even: float
    downside_protection: float


def calc_cash_returns(
    shares: int,
    stock_price: float,
    strike_price: float,
    option_price: float,
    dividends: float,
    comm_stock_buy: float,
    comm_stock_sell: float,
    comm_option_sell: float,
) -> CashResult:
    """Compute covered call returns assuming cash account."""
    premium_total = option_price * shares
    net_investment = (
        shares * stock_price + comm_stock_buy - premium_total + comm_option_sell
    )

    profit_exercised = (
        shares * strike_price - comm_stock_sell + dividends - net_investment
    )
    return_if_exercised = profit_exercised / net_investment * 100

    profit_unchanged = shares * stock_price + dividends - net_investment
    return_if_unchanged = profit_unchanged / net_investment * 100

    break_even = (net_investment - dividends) / shares
    downside_protection = (stock_price - break_even) / stock_price * 100

    return CashResult(
        net_investment,
        return_if_exercised,
        return_if_unchanged,
        break_even,
        downside_protection,
    )


def calc_margin_returns(
    shares: int,
    stock_price: float,
    strike_price: float,
    option_price: float,
    dividends: float,
    comm_stock_buy: float,
    comm_stock_sell: float,
    comm_option_sell: float,
    margin_rate: float,
    interest_rate: float,
    months: int,
) -> MarginResult:
    """Compute covered call returns assuming margin account."""
    premium_total = option_price * shares
    net_stock_cost = shares * stock_price + comm_stock_buy

    equity_required = net_stock_cost * margin_rate
    net_investment = equity_required - premium_total + comm_option_sell
    debit_balance = net_stock_cost - equity_required

    interest = debit_balance * interest_rate * months / 12.0

    profit_exercised = (
        shares * strike_price
        - comm_stock_sell
        + dividends
        - interest
        - debit_balance
        - net_investment
    )
    return_if_exercised = profit_exercised / net_investment * 100

    profit_unchanged = (
        shares * stock_price + dividends - interest - debit_balance - net_investment
    )
    return_if_unchanged = profit_unchanged / net_investment * 100

    break_even = (net_investment + debit_balance - dividends + interest) / shares
    downside_protection = (stock_price - break_even) / stock_price * 100

    return MarginResult(
        net_investment,
        return_if_exercised,
        return_if_unchanged,
        break_even,
        downside_protection,
    )
