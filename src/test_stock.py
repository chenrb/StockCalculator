# -*- coding:utf-8 -*-

from stock_calculator import BuyCalculator, StockRate, SaleCalculator, Deal


def test_buy():
    rate = StockRate(0.00025)
    buy_1 = BuyCalculator(rate, 297.22, 100)
    assert buy_1.transaction_amount == 29722.00
    assert buy_1.commission == 7.43
    assert buy_1.transfer_fee == 0.59
    assert buy_1.amount_incurred == 29730.02
    buy_2 = BuyCalculator(rate, 10, 100)
    assert buy_2.transaction_amount == 1000
    assert buy_2.commission == 5


def test_sale():
    rate = StockRate(0.00025)
    sale_1 = SaleCalculator(rate, 3.29, 7100)
    assert sale_1.transaction_amount == 23359.00
    assert sale_1.commission == 5.84
    assert sale_1.stamp_duty == 23.36
    assert sale_1.transfer_fee == 0.47
    assert sale_1.amount_incurred == 23329.33


def test_deal():
    rate = StockRate(0.00025)
    deal = Deal(rate, 37.18, 37.69, 600)
    buy_1 = BuyCalculator(rate, 37.18, 600)
    assert buy_1.transaction_amount == 22308
    sale_1 = SaleCalculator(rate, 37.69, 600)
    assert sale_1.transaction_amount == 22614
    assert deal.commission == 5.58 + 5.65
    assert deal.stamp_duty == 22.61
    assert deal.transfer_fee == 0.45 + 0.45
    assert deal.profit == 22585.29 - 22314.03
