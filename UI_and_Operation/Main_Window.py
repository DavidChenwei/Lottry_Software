import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
import sys

from utils.Database_operation import create_balance_table, create_gift_table
from UI_and_Operation.First_Window_Operation import First_Window
from UI_and_Operation.Monitor_player_operation import Monitor_Window
from UI_and_Operation.Second_Window_Operation import Second_Window
# from Simple_Second_Window_Operation import Simple_Second_Window
from Combox_test import ComboCheckBox
from UI_and_Operation.Thrid_window_operation import Third_Window

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        main_window = First_Window()
        lottery_window = Second_Window()
        # lottery_window = Simple_Second_Window()
        modify_price = Third_Window()
        monitor_player = Monitor_Window()
        # 通过toolButton将两个窗体关联
        btn = main_window.NextStep_pushButton
        btn.clicked.connect(lottery_window.show)
        btn.clicked.connect(main_window.close_w1)

        btn_m_p = lottery_window.modify_price_pushButton
        btn_m_p.clicked.connect(modify_price.show)
        comboBox1 = ComboCheckBox(lottery_window)
        comboBox1.setGeometry(QtCore.QRect(110, 10, 200, 30))
        comboBox1.setMinimumSize(QtCore.QSize(100, 20))
        comboBox1.loaditem()
        btn_m_p = lottery_window.pushButton_monitor_player
        btn_m_p.clicked.connect(monitor_player.show)
        # 显示
        main_window.show()
        os._exit(app.exec_())
        # sys.exit(app.exec_())
    except Exception as e:
        print(e)
