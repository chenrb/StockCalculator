# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog

from ui.app_ui import Ui_MainWindow
from stock_calculator import StockRate, Deal

COST_TEXT = """
保本价：{break_even_price}
总费用：{cost}
印花税：{stamp_duty}，佣金：{commission}，过户费：{transfer_fee}
"""
RISE_TEXT = "涨幅：{} %"
PROFIT_TEXT = "利润：{}"
RED = "<font color=red>{}</font>"
GREEN = "<font color=green>{}</font>"


class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        rate = self.get_stock_rate()
        buy = self.BuyBox.value()
        sale = self.SaleBox.value()
        num = self.NumBox.value()
        if num <= 0:
            self.textBrowser.setText('请输入正确的股数')
            return

        deal = Deal(rate, buy, sale, num)
        if deal.profit > 0:
            rise_text = RISE_TEXT.format(RED.format(deal.rise))
            profit_text = PROFIT_TEXT.format(RED.format(deal.profit))
        else:
            rise_text = RISE_TEXT.format(GREEN.format(deal.rise))
            profit_text = PROFIT_TEXT.format(GREEN.format(deal.profit))
        self.textBrowser.append(rise_text)
        self.textBrowser.append(profit_text)
        cost_text = COST_TEXT.format(break_even_price=deal.break_even_price,
                                     cost=deal.cost,
                                     stamp_duty=deal.stamp_duty,
                                     commission=deal.commission,
                                     transfer_fee=deal.transfer_fee)
        self.textBrowser.append(cost_text)

    def get_stock_rate(self):
        commission_rate = self.CommissionBox.value()
        stamp_duty_rate = self.StampDutyBox.value()
        transfer_rate = self.TransferBox.value()
        rate = StockRate(commission_rate, stamp_duty_rate, transfer_rate)
        return rate


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())
