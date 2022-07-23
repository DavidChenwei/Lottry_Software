# 此文件用于编写第二个window的相关gui操作
import copy
import operator
import threading
import concurrent.futures
import time

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
import sys

from PyQt5.QtCore import QTimer, Qt
# from Grab_Barrage import grab_info
# from Grab_sys_lottery_info import lottery_related_function
from numpy import around

from utils.Database_operation import update_data_balance_table, insert_gift_info, update_total_around_info, \
    create_every_around, update_every_around_info, create_balance_table, create_gift_table, create_total_around
from Dream_Box_Calculation import Dict_Mdx, Dict_Mtl
from Dream_Box_Calculation import *
from utils.Matplotlib_RMB import plot_method
from UI_and_Operation.Second_Window_UI import Ui_Second_window
import utils.globalvar as gl
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5 import QtCore, QtGui

from simple_Grab_Barrage import grab_info
from Thread_gift_operation import gift_operation, Dict_every_mdx, Dict_every_mtl, Dict_every_pdk, Dict_pdk, \
    Dict_every_rqq, Dict_every_xjzj
# from Tread_grab_info import grab_info
from selected_gift_function import fomart_data, integrated_list, fomart_data_plus
from simple_sys_lottery_info import lottery_related_function
from utils.table_test_1 import pad_len

temp_dict_mtl = {}
temp_dict_mdx = {}
dit_plot = {}  # 存放数据用来画图
temp_info = '礼物信息'
msg_num = 0
Dict_lottery_id = {'红包ID': 1}
temp_list = []
temp_info_list = []
gl.set_value('selected_gift', 'None')
tplt = "{0:<{len1}}\t{1:<{len2}}\t{2:>{len3}}\t{3:>{len4}}\t{4:>{len5}}\t{5:>{len6}}"
lottery_num = 1
num_for_dict = 0


# 重定向console显示的内容到GUI
# class EmittingStr(QtCore.QObject):
#     textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号
#
#     def write(self, text):
#         self.textWritten.emit(str(text))


class Second_Window(QMainWindow, Ui_Second_window):

    def __init__(self):
        super(Second_Window, self).__init__()
        self.setupUi(self)
        # sys.stdout = EmittingStr(textWritten=self.outputWritten)
        # sys.stderr = EmittingStr(textWritten=self.outputWritten)
        self.pushButton.clicked.connect(self.begin)
        self.pushButton.clicked.connect(self.TGB_start)
        self.pushButton.clicked.connect(self.Timer_emit_lottery)
        self.pushButton.clicked.connect(self.Timer_emit_box)
        self.pushButton.clicked.connect(self.selected_gift_emit)
        self.pushButton.clicked.connect(self.refresh_time_emit)
        self.pushButton_2.clicked.connect(self.showfigur)
        # self.pushButton.clicked.connect(self.Tread_sys_lottery_info)
        # 先建立四个表，红包的收支平衡表, 全部礼物表 和 每轮玩家礼物统计表(第一轮).
        create_balance_table()
        create_gift_table()
        create_total_around()
        create_every_around()

        # 设置表格
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['时间', '昵称', '礼物', '个数', '砖石', '大小盒'])
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setColumnWidth(0, 80)
        self.tableView.setColumnWidth(1, 150)
        self.tableView.setColumnWidth(2, 120)
        self.tableView.setColumnWidth(3, 65)
        self.tableView.setColumnWidth(4, 65)
        # 滚动条自动到底
        self.model.rowsInserted.connect(self.autoScroll)

    def autoScroll(self):
        QtCore.QTimer.singleShot(0, self.tableView.scrollToBottom)

    def begin(self):
        self.pushButton.setDisabled(True)

    def Tread_Grab_Barrage(self):
        try:
            global Dict_lottery_id
            global temp_list
            room_id = gl.get_value('room_id')
            time_stamp = gl.get_value('time_stamp')
            Rmb_back = gl.get_value('Rmb_back')
            lottery_related_function(room_id)
            lottery_id = gl.get_value('lottery_id')
            Dict_lottery_id[lottery_id] = 1
            # print('第一次', Dict_lottery_id)
            gl.set_value('Dict_lottery_id', Dict_lottery_id)
            while True:
                grab_info(room_id, time_stamp, Rmb_back)
            # while True:
            #     # start = time.clock()
            #     list = grab_info(room_id, time_stamp)
            #     # list = ['读着倒得字名个这$$$读着倒得字名个这 赠送 梦幻盒子 变幻出 梦幻迷迭香 x1个 $$$Ko06CnBBAABc5M2KjKsFAMaUFwBh$$$1595994996211', '唯独冰尘$$$唯独冰尘 赠送 梦幻迷你盒 爆出 BUFF 梦幻迷迭香 x1个 $$$tHQzCqhWAAAafTZ_jKsFALuWFwBh$$$1595994801736', ]
            #     # list = ['塔罗世界$$$吃不到葡萄耀說酸赠送魔力包获得海洋之心卡x3，守护主播卡x2，超跑派对卡x1$$$2BmVCUADAAA6pZqxU6oFAEZeMQBh$$$1594651322307']
            #     if len(list) != 0 and operator.eq(list, temp_list) is not True:
            #         temp_list = copy.deepcopy(list)
            #         with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            #             future_to_list = {executor.submit(gift_operation, lt): lt for lt in list}
            #             # print(future_to_list)
            #             for future in concurrent.futures.as_completed(future_to_list):
            #                 lt = future_to_list[future]
            #                 try:
            #                     data = future.result()
            #                 except Exception as e:
            #                     # print(list)
            #                     print('%r generated an exception: %s' % (lt, e))
            #                 else:
            #                     pass
                                # print(data)
                        # end = time.clock()
                        # print('thread running time is ', around((end - start), 10))
        except Exception as e:
            print('无辜报错', e)

    # def Tread_sys_lottery_info(self):
    #     # room_id = gl.get_value('room_id')
    #     # Rmb_back = gl.get_value('Rmb_back')
    #     timer = QTimer(self)
    #     timer.timeout.connect(self.lottery_start)
    #     timer.start(100)
    #
    #     # while True:
    #     #     lottery_related_function(room_id, Rmb_back)
    #
    # def lottery_start(self):
    #     room_id = gl.get_value('room_id')
    #     Rmb_back = gl.get_value('Rmb_back')
    #     # lottery_related_function(room_id, Rmb_back)

    global threads
    threads = [threading.Thread(target=Tread_Grab_Barrage, args=("self",))]

    def TGB_start(self):
        threads[0].start()
        # threads[1].start()

    def Timer_emit_lottery(self):
        timer = QTimer(self)
        timer.timeout.connect(self.Update_lottery)
        timer.start(1000)

    def Update_lottery(self):
        try:
            # room_id = gl.get_value('room_id')
            # Rmb_back = gl.get_value('Rmb_back')
            # lottery_related_function(room_id, Rmb_back)
            gift_total = gl.get_value('gift_total')
            # gift_total_value = gl.get_value('gift_total_value')
            gift_total_value = gl.get_value('total_gift_value_diamond')
            total_rmb_value = gl.get_value('total_rmb_value')
            # Needed_gift_account = gl.get_value('Needed_gift_account')
            RMB_balance = gl.get_value('RMB_balance')
            gift_name = gl.get_value('gift_name')
            total_lottery_value = gl.get_value('total_lottery_value')
            user_total = gl.get_value('user_total')
            this_time_RMB_total = gl.get_value('this_time_RMB_total')
            solo_total_gift_value_diamond = gl.get_value('solo_total_gift_value_diamond')
            solo_total_rmb_value = gl.get_value('solo_total_rmb_value')
            every_local_money_back = gl.get_value('every_local_money_back')
            gift_nick = gl.get_value('gift_nick')

            self.lcdNumber.display(total_lottery_value)
            self.lcdNumber_2.display(user_total)
            self.lcdNumber_3.display(gift_total)
            self.lcdNumber_4.display(gift_total_value)
            self.lcdNumber_5.display(total_rmb_value)
            self.lcdNumber_6.display(RMB_balance)
            self.lcdNumber_7.display(this_time_RMB_total)
            # self.lcdNumber_8.display(this_time_RMB_total)
            self.lcdNumber_9.display(solo_total_rmb_value)
            self.lcdNumber_10.display(solo_total_gift_value_diamond)
            self.lcdNumber_8.display(every_local_money_back)
            self.label_8.setText(gift_name)
            self.label_11.setText(gift_nick)
            app.processEvents()  # 关键的一句话
            # 将上述显示数据更新到数据库中，最后的9999999为主键
            update_data_balance_table(str(total_lottery_value), str(every_local_money_back), str(user_total),
                                      str(gift_total), str(gift_total_value), str(total_rmb_value), str(RMB_balance),
                                      str(solo_total_gift_value_diamond), str(solo_total_rmb_value),
                                      str(this_time_RMB_total), 9999999)
        except Exception as e:
            print(e)

    # 该方法是以表格形式显示玩家中的礼物
    def Timer_emit_box(self):
        timer = QTimer(self)
        timer.timeout.connect(self.Update_box)
        timer.start(1000)

    def Update_box(self):
        global msg_num
        global temp_info
        gift_info = gl.get_value(msg_num)

        if gift_info != temp_info and gift_info is not None:

            try:
                msg = gift_info.split(",")
            except Exception as e:
                print(e)
            print(msg)
            insert_gift_info(msg_num, msg[0], msg[1], msg[2], msg[3], msg[4], msg[6])
            for i in range(0, len(msg) - 2):
                item = QStandardItem(msg[i])
                try:
                    self.model.setItem(msg_num, i, item)
                    if "梦幻花环" in msg[2]:
                        self.model.item(msg_num, i).setBackground(QtGui.QBrush(QtGui.QColor("mistyrose")))
                    if "梦幻情书" in msg[2]:
                        self.model.item(msg_num, i).setBackground(QtGui.QBrush(QtGui.QColor("cyan")))
                    if "永恒魔法棒" in msg[2]:
                        self.model.item(msg_num, i).setBackground(QtGui.QBrush(QtGui.QColor("darkturquoise")))
                    if "梦幻迷迭香" in msg[2] and 'normal' == msg[5] and msg[6] == 'False':
                        self.model.item(msg_num, i).setBackground(QtGui.QBrush(QtGui.QColor("lightpink")))
                    if "梦幻迷迭香" in msg[2] and 'mini' == msg[5] and msg[6] == 'False':
                        self.model.item(msg_num, i).setBackground(QtGui.QBrush(QtGui.QColor("deeppink")))
                    if "梦幻迷迭香" in msg[2] and msg[6] == 'True':
                        self.model.item(msg_num, i).setBackground(QtGui.QBrush(QtGui.QColor("hotpink")))
                    if "梦幻摩天轮" in msg[2] and 'normal' == msg[5] and msg[6] == 'False':
                        self.model.item(msg_num, i).setBackground(QtGui.QBrush(QtGui.QColor("gold")))
                    if "梦幻摩天轮" in msg[2] and 'mini' == msg[5] and msg[6] == 'False':
                        self.model.item(msg_num, i).setBackground(QtGui.QBrush(QtGui.QColor("yellow")))
                    if "梦幻摩天轮" in msg[2] and msg[6] == 'True':
                        self.model.item(msg_num, i).setBackground(QtGui.QBrush(QtGui.QColor("goldenrod")))
                    if "梦幻水晶鞋" in msg[2]:
                        self.model.item(msg_num, i).setBackground(QtGui.QBrush(QtGui.QColor("silver")))
                    if '梦幻热气球' in msg[2]:
                        self.model.item(msg_num, i).setBackground(QtGui.QBrush(QtGui.QColor("peachpuff")))
                    if '星际战舰' in msg[2]:
                        self.model.item(msg_num, i).setBackground(QtGui.QBrush(QtGui.QColor("orangered")))
                    if '超跑派对卡' in msg[2]:
                        self.model.item(msg_num, i).setBackground(QtGui.QBrush(QtGui.QColor("slategray")))
                    self.model.item(msg_num, i).setTextAlignment(Qt.AlignCenter)
                except Exception as e:
                    print(e)
            temp_info = gift_info
            msg_num += 1
            app.processEvents()

    # 该方法为老版的显示玩家的礼物，需要多个框体，新版中该方法为启用
    def Timer_emit_mtl(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update_mtl)
        timer.start(500)

    def update_mtl(self):
        global temp_dict_mdx, temp_dict_mtl
        try:
            dict_Mtl = gl.get_value('dict_Mtl')
            if temp_dict_mtl == dict_Mtl:
                i = 1
            else:
                self.textEdit_2.clear()
                for key in dict_Mtl.keys():
                    str_info = key + ' , ' + str(dict_Mtl[key]) + '个'
                    self.textEdit_2.append(str_info)
                temp_dict_mtl = copy.copy(dict_Mtl)
            # print(dict_Mtl)

        except Exception as e:
            print(e)
            app.processEvents()

        try:
            dict_Mdx = gl.get_value('dict_Mdx')
            if temp_dict_mdx == dict_Mdx:
                i = 1
            else:
                self.textEdit.clear()
                for key in dict_Mdx.keys():
                    str_info = key + ' , ' + str(dict_Mdx[key]) + '个'
                    self.textEdit.append(str_info)
                temp_dict_mdx = copy.copy(dict_Mdx)

        except Exception as e:
            print(e)
        app.processEvents()

    # def outputWritten(self, text):
    #     cursor = self.textBrowser.textCursor()
    #     cursor.movePosition(QtGui.QTextCursor.End)
    #     cursor.insertText(text)
    #     self.textBrowser.setTextCursor(cursor)
    #     self.textBrowser.ensureCursorVisible()

    # 该方法是没五分钟记一次收益，进行画图
    def refresh_time_emit(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update_refresh)
        timer.start(300000)

    def update_refresh(self):
        global num_for_dict
        gl.set_value('refresh_time', 0)
        gl.set_value('refresh_time_sys', 0)
        time_str = time.strftime('%H:%M:%S', time.localtime(time.time()))
        this_time_RMB_total = gl.get_value('this_time_RMB_total')
        dit_plot[num_for_dict] = time_str + ' ' + str(around(this_time_RMB_total, 2))
        sorted(dit_plot)
        num_for_dict += 1

    def showfigur(self):
        plot_method(dit_plot)

    def clearbrowser(self):
        self.textBrowser.clear()

    # 该方法是用来统计玩家在砸盒子中获得的礼物
    def selected_gift_emit(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update_selected_gift)
        timer.start(500)

    def update_selected_gift(self):
        # Dict_Mdx = gl.get_value("dict_Mdx")
        # Dict_Mtl = gl.get_value("dict_Mtl")
        # Dict_pdk = gl.get_value("dict_pdk")
        Dict_every_Mdx = gl.get_value("dict_every_mdx")
        Dict_every_Mtl = gl.get_value("dict_every_mtl")
        Dict_every_Pdk = gl.get_value("dict_every_pdk")
        try:
            global tplt, temp_info_list, tplt_1, lottery_num
            info_list, sum_dict_mdx, sum_dict_mtl, sum_dict_pdk = fomart_data(Dict_Mdx, Dict_Mtl, Dict_pdk)
            info_list_plus, sum_dict_rqq, sum_dict_xjzj = fomart_data_plus(Dict_Rqq, Dict_Xjzj)
            info_list_final = integrated_list(info_list, info_list_plus)
            # print(info_list_final)
            new_lottery_left = gl.get_value('new_lottery_left')
            lottery_gift_name = gl.get_value('gift_name')
            if len(info_list_final) != 0 and operator.eq(info_list_final, temp_info_list) is not True:
                temp_info_list = copy.deepcopy(info_list_final)
                # print(info_list)
                self.textBrowser.clear()
                title_arr = ["玩家ID", "梦幻迷迭香", "梦幻摩天轮", "超跑派对卡", '梦幻热气球', '星际战舰']
                self.textBrowser.append(tplt.format(*title_arr, len1=pad_len(title_arr[0], 25),
                                                    len2=pad_len(title_arr[1], 5), len3=pad_len(title_arr[2], 5),
                                                    len4=pad_len(title_arr[3], 5), len5=pad_len(title_arr[4], 5),
                                                    len6=pad_len(title_arr[5], 5)))
                for i in range(0, len(info_list_final)):
                    temp_arr = info_list_final[i].split(' ')
                    self.textBrowser.append(tplt.format(*temp_arr, len1=pad_len(temp_arr[0], 25),
                                                        len2=pad_len(temp_arr[1], 5), len3=pad_len(temp_arr[2], 5),
                                                        len4=pad_len(temp_arr[3], 5), len5=pad_len(temp_arr[4], 5),
                                                        len6=pad_len(temp_arr[5], 5)))
                    update_total_around_info(temp_arr[0], temp_arr[1], temp_arr[2], temp_arr[4], temp_arr[5],
                    temp_arr[3])
                self.textBrowser.append(
                    "<font color=\"#3366CC\">" + '------------------------------------------------------------------------' + "</font>")
                res_array = ["全局总计", str(sum_dict_mdx), str(sum_dict_mtl), str(sum_dict_pdk), str(sum_dict_rqq),
                             str(sum_dict_xjzj)]
                self.textBrowser.append(tplt.format(*res_array, len1=pad_len(res_array[0], 25),
                                                    len2=pad_len(res_array[1], 5), len3=pad_len(res_array[2], 5),
                                                    len4=pad_len(res_array[3], 5), len5=pad_len(res_array[4], 5),
                                                    len6=pad_len(res_array[5], 5)))
            if new_lottery_left:
                time_stamp = gl.get_value('start_time')
                time_stamp_int = int(time_stamp)
                timeArray = time.localtime(time_stamp_int / 1000)
                otherStyleTime = time.strftime("%H:%M:%S", timeArray)
                info_list, sum_dict_mdx, sum_dict_mtl, sum_dict_pdk = fomart_data(Dict_every_Mdx, Dict_every_Mtl,
                                                                                  Dict_every_Pdk)
                sum_dict_mdx = sum(Dict_every_Mdx.values())
                print(Dict_every_Mdx)
                print(sum_dict_mdx)
                sum_dict_mtl = sum(Dict_every_Mtl.values())
                sum_dict_pdk = sum(Dict_every_Pdk.values())
                info_list_plus, sum_dict_rqq, sum_dict_xjzj = fomart_data_plus(Dict_every_rqq, Dict_every_xjzj)
                info_list_final = integrated_list(info_list, info_list_plus)
                temp_str_2 = '=====第' + str(lottery_num) + ' 轮抽奖 Start Time : ' + str(otherStyleTime) + '====='
                self.textBrowser_2.append("<font color=\"#FF6633\">" + temp_str_2 + "</font>")
                lottery_value = gl.get_value('total_lottery_value')
                temp_str_1 = '抽奖礼物: ' + lottery_gift_name + '红包金额: ' + str(lottery_value)
                self.textBrowser_2.append("<font color=\"#FF6633\">" + temp_str_1 + "</font>")
                title_arr = ["玩家ID", "迷迭香", "摩天轮", "派对卡", '热气球', '战舰']
                self.textBrowser_2.append(
                    tplt.format(*title_arr, len1=pad_len(title_arr[0], 20), len2=pad_len(title_arr[1], 3),
                                len3=pad_len(title_arr[2], 3), len4=pad_len(title_arr[3], 3),
                                len5=pad_len(title_arr[4], 3), len6=pad_len(title_arr[5], 3)))

                for i in range(0, len(info_list_final)):
                    temp_arr = info_list_final[i].split(' ')
                    print(temp_arr)
                    self.textBrowser_2.append(
                        tplt.format(*temp_arr, len1=pad_len(temp_arr[0], 20), len2=pad_len(temp_arr[1], 3),
                                    len3=pad_len(temp_arr[2], 3), len4=pad_len(temp_arr[3], 3),
                                    len5=pad_len(temp_arr[4], 3), len6=pad_len(temp_arr[5], 3)))
                    update_every_around_info(temp_arr[0], temp_arr[1], temp_arr[2], temp_arr[4], temp_arr[5],
                                             temp_arr[3])
                self.textBrowser_2.append(
                    "<font color=\"#3366CC\">" + '-------------------------------------------------------------------------' + "</font>")
                res_array = ["每轮小计", str(sum_dict_mdx), str(sum_dict_mtl), str(sum_dict_pdk), str(sum_dict_rqq),
                             str(sum_dict_xjzj)]
                self.textBrowser_2.append(tplt.format(*res_array, len1=pad_len(res_array[0], 20),
                                                      len2=pad_len(res_array[1], 3), len3=pad_len(res_array[2], 3),
                                                      len4=pad_len(res_array[3], 3), len5=pad_len(res_array[4], 3),
                                                      len6=pad_len(res_array[5], 3)))
                self.textBrowser_2.append(
                    "<font color=\"#3366CC\">" + '-------------------------------------------------------------------------' + "</font>")
                gl.set_value('new_lottery_left', False)
                lottery_num += 1
                Dict_every_Mdx.clear()
                Dict_every_Mtl.clear()
                Dict_every_Pdk.clear()
                Dict_every_rqq.clear()
                Dict_every_xjzj.clear()
        except Exception as e:
            print(e)


app = QtWidgets.QApplication(sys.argv)
