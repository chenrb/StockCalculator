# -*- coding:utf-8 -*-


class StockRate:
    def __init__(self, commission_rate, stamp_duty_rate=0.001, transfer_rate=0.00002) -> None:
        self.commission_rate = commission_rate
        self.stamp_duty_rate = stamp_duty_rate
        self.transfer_rate = transfer_rate


def custom_format(data):
    """小数点后2位取整"""
    return float(format(data, ".2f"))


class BaseModel:
    def __init__(self, rate, price, num) -> None:
        self.rate = rate
        self.price = price
        self.num = num


class BuyCalculator(BaseModel):
    def __init__(self, rate, price, num) -> None:
        super().__init__(rate, price, num)
        (
            self.transaction_amount,
            self.commission,
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
        transfer_fee: 过户费
        """
        transaction_amount = custom_format(price * num)
        commission = custom_format(transaction_amount * rate.commission_rate)
        if commission < 5:
            commission = 5
        transfer_fee = custom_format(transaction_amount * rate.transfer_rate)
        amount_incurred = custom_format(transaction_amount + commission + transfer_fee)
        return transaction_amount, commission, transfer_fee, amount_incurred


class SaleCalculator(BaseModel):
    def __init__(self, rate, price, num) -> None:
        super().__init__(rate, price, num)
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


class Deal:
    """
    暂定做T买入卖出数量相同
    """

    def __init__(self, rate, buy_price, sale_price, num) -> None:
        self.rate = rate
        self.buy_price = buy_price
        self.sale_price = sale_price
        self.num = num
        (
            self.profit,
            self.rise,
            self.commission,
            self.stamp_duty,
            self.transfer_fee,
            self.cost,
            self.break_even_price,
        ) = self.calculate(self.rate, self.buy_price, self.sale_price, self.num)

    @staticmethod
    def calculate(rate, buy_price, sale_price, num):
        """
        profit: 利润
        rise: 涨幅
        commission: 手续费
        stamp_duty: 印花税
        transfer_fee: 过户费
        cost: commission + stamp_duty + transfer_fee
        break_even_price: 保本单价
        """
        buy = BuyCalculator(rate, buy_price, num)
        sale = SaleCalculator(rate, sale_price, num)
        rise = custom_format((sale_price - buy_price) / buy_price * 100)
        profit = custom_format(sale.amount_incurred - buy.amount_incurred)
        commission = sale.commission + buy.commission
        stamp_duty = sale.stamp_duty
        transfer_fee = sale.transfer_fee + buy.transfer_fee
        cost = custom_format(commission + stamp_duty + transfer_fee)
        break_even_price = custom_format(cost / num) + buy_price
        return profit, rise, commission, stamp_duty, transfer_fee, cost, break_even_price
