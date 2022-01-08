# -*- coding:utf-8 -*-


class StockRate:
    def __init__(self, commission_rate) -> None:
        self.commission_rate = commission_rate
        self.stamp_duty_rate = 0.001
        self.transfer_rate = 0.00002


def custom_format(data):
    """小数点后2位取整"""
    # return int(data * f) / f
    return float(format(data, '.2f'))


class BuyCalculator:
    def __init__(self, rate, price, num) -> None:
        self.rate = rate
        self.price = price
        self.num = num
        (
            self.cost,
            self.commission,
            self.transfer_fee,
            self.total,
            self.break_even_price,
        ) = self.calculate(self.rate, self.price, self.num)

    @staticmethod
    def calculate(rate, price, num):
        """
        根据费率、买入单价、数量计算：买入金额，佣金，过户费，总费用，保本单价
        """
        cost = price * num
        commission = cost * rate.commission_rate
        if commission < 5:
            commission = 5
        transfer_fee = cost * rate.transfer_rate
        total = cost + commission + transfer_fee
        break_even_price = total / num
        return (
            custom_format(cost),
            custom_format(commission),
            custom_format(transfer_fee),
            custom_format(total),
            custom_format(break_even_price),
        )


class SaleCalculator:
    def __init__(self, rate, price, num) -> None:
        self.rate = rate
        self.price = price
        self.num = num
        (
            self.sales_amount,
            self.commission,
            self.stamp_duty,
            self.transfer_fee,
            self.net_sales_amount,
        ) = self.calculate(self.rate, self.price, self.num)

    @staticmethod
    def calculate(rate, price, num):
        """
        根据费率、卖出单价、数量计算：卖出金额，佣金，印花税，过户费，卖出净金额
        """
        sales_amount = price * num
        commission = sales_amount * rate.commission_rate
        if commission < 5:
            commission = 5
        stamp_duty = sales_amount * rate.stamp_duty_rate
        transfer_fee = sales_amount * rate.transfer_rate
        net_sales_amount = sales_amount - commission - stamp_duty - transfer_fee
        return (
            custom_format(sales_amount),
            custom_format(commission),
            custom_format(stamp_duty),
            custom_format(transfer_fee),
            custom_format(net_sales_amount),
        )
