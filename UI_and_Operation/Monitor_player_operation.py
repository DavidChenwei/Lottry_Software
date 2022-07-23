import time

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow

import utils.globalvar as gl
from UI_and_Operation.Monitor_player import Ui_Monitor_players

temp_array = []
temp_monitor_info = ''
temp_monitor_total_info = ''
tplt = "{0:{3}<15}\t{1:{3}<3}\t{2:{3}<3}"
tplt_1 = "{0:{3}<13}\t{1:{3}<3}\t{2:{3}<3}"
lottery_num = 1


class Monitor_Window(QMainWindow, Ui_Monitor_players):

    def __init__(self):
        super(Monitor_Window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.transport_info)
        self.pushButton.clicked.connect(self.Timer_emit_monitor)

    def transport_info(self):  # 点击按键，将玩家姓名，折扣传给全局变量
        player_1_name = self.lineEdit.text().strip()
        gl.set_value('player_1_name', player_1_name)
        player_1_discount = self.lineEdit_6.text().strip()
        gl.set_value('player_1_discount', player_1_discount)

        player_2_name = self.lineEdit_2.text().strip()
        gl.set_value('player_2_name', player_2_name)
        player_2_discount = self.lineEdit_7.text().strip()
        gl.set_value('player_2_discount', player_2_discount)

        player_3_name = self.lineEdit_3.text().strip()
        gl.set_value('player_3_name', player_3_name)
        player_3_discount = self.lineEdit_8.text().strip()
        gl.set_value('player_3_discount', player_3_discount)

        player_4_name = self.lineEdit_4.text().strip()
        gl.set_value('player_4_name', player_4_name)
        player_4_discount = self.lineEdit_9.text().strip()
        gl.set_value('player_4_discount', player_4_discount)

        player_5_name = self.lineEdit_5.text().strip()
        gl.set_value('player_5_name', player_5_name)
        player_5_discount = self.lineEdit_10.text().strip()
        gl.set_value('player_5_discount', player_5_discount)

        all_names = [player_1_name, player_2_name, player_3_name, player_4_name, player_5_name]
        gl.set_value('all_name', all_names)

    def Timer_emit_monitor(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update_monitor)
        timer.start(500)

    def update_monitor(self):
        global temp_monitor_info, lottery_num, tplt, tplt_1, temp_monitor_total_info, temp_array
        lottery_gift_name = gl.get_value('gift_name')
        try:
            monitor_info = gl.get_value('monitor_info')
            monitor_total_info = gl.get_value('monitor_total_info')
            new_lottery = gl.get_value('new_lottery')

            # 这里是显示全程的玩家监控信息
            if temp_monitor_total_info == monitor_total_info:
                pass
            else:
                temp_monitor_total_info = monitor_total_info
                self.textBrowser_3.clear()
                self.textBrowser_3.append(tplt_1.format("玩家ID", "钻石数", "金额", chr(12288)))
                temp_array_2 = monitor_total_info.split(' || ')
                for i in range(0, len(temp_array_2) - 1):
                    temp_arr = temp_array_2[i].split(' ')
                    self.textBrowser_3.append(tplt_1.format(temp_arr[0], temp_arr[1], temp_arr[2], chr(12288)))

            # 这里显示每轮的记录
            if temp_monitor_info == monitor_info:
                pass
            else:
                temp_monitor_info = monitor_info
                self.textBrowser_2.clear()
                self.textBrowser_2.append(tplt_1.format("玩家ID", "钻石数", "金额", chr(12288)))
                temp_array = monitor_info.split(' || ')
                # print(temp_array)
                for i in range(0, len(temp_array) - 1):
                    temp_arr = temp_array[i].split(' ')
                    self.textBrowser_2.append(tplt_1.format(temp_arr[0], temp_arr[1], temp_arr[2], chr(12288)))
            # 这里显示历史记录
            if new_lottery:
                time_stamp = gl.get_value('start_time')
                time_stamp_int = int(time_stamp)
                timeArray = time.localtime(time_stamp_int / 1000)
                otherStyleTime = time.strftime("%H:%M:%S", timeArray)
                temp_str_2 = '=====第' + str(lottery_num) + ' 轮抽奖 Start Time : ' + str(otherStyleTime) + '====='
                self.textBrowser.append("<font color=\"#FF6633\">" + temp_str_2 + "</font>")
                temp_str_1 = '抽奖礼物: ' + lottery_gift_name
                self.textBrowser.append("<font color=\"#FF6633\">" + temp_str_1 + "</font>")
                self.textBrowser.insertPlainText("\r\n")
                self.textBrowser.insertPlainText(tplt.format("玩家ID", "钻石数", "金额", chr(12288)))
                self.textBrowser.insertPlainText("\r\n")

                for i in range(0, len(temp_array) - 1):
                    temp_arr = temp_array[i].split(' ')
                    self.textBrowser.append(tplt.format(temp_arr[0], temp_arr[1], temp_arr[2], chr(12288)))
                self.textBrowser.append("<font color=\"#3366CC\">"
                                        + "---------------------------------------------------------------------------------------" + "</font>")
                self.textBrowser.append(
                    "<font color=\"#3366CC\">"
                    + "---------------------------------------------------------------------------------------" + "</font>")
                gl.set_value('new_lottery', False)
                lottery_num += 1

        except Exception as e:
            print('监控错误:', e)
