# -*- coding:utf-8 -*-


class StockRate:
    def __init__(
        self, commission_rate, stamp_duty_rate=0.001, transfer_rate=0.00002
    ) -> None:
        self.commission_rate = commission_rate
        self.stamp_duty_rate = stamp_duty_rate
        self.transfer_rate = transfer_rate


def custom_format(data):
    """小数点后2位取整"""
    return float(format(data, ".2f"))


class BuyCalculator:
    def __init__(self, rate, price, num) -> None:
        self.rate = rate
        self.price = price
        self.num = num
        (
            self.transaction_amount,
            self.commission,
            self.transfer_fee,
            self.amount_incurred,
            self.break_even_price,
        ) = self.calculate(self.rate, self.price, self.num)

    @staticmethod
    def calculate(rate, price, num):
        """
        price: 成交均价
        num: 成交数量
        transaction_amount: 成交金额
        amount_incurred: 发生金额
        commission: 手续费
        transfer_fee: 过户费
        """
        transaction_amount = custom_format(price * num)
        commission = custom_format(transaction_amount * rate.commission_rate)
        if commission < 5:
            commission = 5
        transfer_fee = custom_format(transaction_amount * rate.transfer_rate)
        amount_incurred = custom_format(transaction_amount + commission + transfer_fee)
        break_even_price = custom_format(amount_incurred / num)
        return transaction_amount, commission, transfer_fee, amount_incurred, break_even_price


class SaleCalculator:
    def __init__(self, rate, price, num) -> None:
        self.rate = rate
        self.price = price
        self.num = num
        (
            self.transaction_amount,
            self.commission,
            self.stamp_duty,
            self.transfer_fee,
            self.amount_incurred,
        ) = self.calculate(self.rate, self.price, self.num)

    @staticmethod
    def calculate(rate, price, num):
        """
        price: 成交均价
        num: 成交数量
        transaction_amount: 成交金额
        amount_incurred: 发生金额
        commission: 手续费
        stamp_duty: 印花税
        transfer_fee: 过户费
        """
        transaction_amount = custom_format(price * num)
        commission = custom_format(transaction_amount * rate.commission_rate)
        if commission < 5:
            commission = 5
        stamp_duty = custom_format(transaction_amount * rate.stamp_duty_rate)
        transfer_fee = custom_format(transaction_amount * rate.transfer_rate)
        amount_incurred = custom_format(
            transaction_amount - commission - stamp_duty - transfer_fee
        )
        return transaction_amount, commission, stamp_duty, transfer_fee, amount_incurred
