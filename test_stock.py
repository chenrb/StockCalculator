# -*- coding:utf-8 -*-

import pytest

from stock_calculator import BuyCalculator, StockRate


def test_buy():
    rate = StockRate(0.00025)
    buy_1 = BuyCalculator(rate, 297.22, 100)
    assert buy_1.cost == 29722.00
    assert buy_1.commission == 7.43
    assert buy_1.transfer_fee == 0.59
    assert buy_1.total == 29730.02
    assert buy_1.break_even_price == 297.30
    buy_2 = BuyCalculator(rate, 10, 100)
    assert buy_2.cost == 1000
    assert buy_2.commission == 5