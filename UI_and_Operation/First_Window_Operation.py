# 此文件用于编写第一个window的相关gui操作

from PyQt5.QtWidgets import QMainWindow

from UI_and_Operation.First_Window_UI import Ui_First_window
import utils.globalvar as gl
from utils.GetTimestamp import get_TimeStamp


class First_Window(QMainWindow, Ui_First_window):

    def __init__(self):
        super(First_Window, self).__init__()
        self.setupUi(self)
        self.NextStep_pushButton.clicked.connect(self.transport_info)
        # gl._init()

    def close_w1(self):  # 点击按钮将窗体1关掉
        self.close()

    def transport_info(self):  # 点击按键，将房间号，返点率和时间戳传给全局变量
        room_id = self.RoomID_lineEdit.text()
        gl.set_value('room_id', room_id)

        Rmb_back = self.RmbReturn_lineEdit.text()
        if Rmb_back == '':
            Rmb_back = '60.25'
        gl.set_value('Rmb_back', Rmb_back)

        Mdx_price = self.Mdx_Price_lineEdit.text()
        if Mdx_price == '':
            Mdx_price = '100'
        gl.set_value('Mdx_price', Mdx_price)

        Mdx_price_small = self.Mdx_Price_lineEdit_2.text()
        if Mdx_price_small == '':
            Mdx_price_small = Mdx_price
        gl.set_value('Mdx_price_small', Mdx_price_small)

        Mtl_price = self.Mtl_price_lineEdit.text()
        if Mtl_price == '':
            Mtl_price = '1000'
        gl.set_value('Mtl_price', Mtl_price)

        Mtl_price_small = self.Mtl_price_lineEdit_2.text()
        if Mtl_price_small == '':
            Mtl_price_small = Mtl_price
        gl.set_value('Mtl_price_small', Mtl_price_small)

        double_mdx_price = self.double_mdx_price_lineEdit.text()
        if double_mdx_price == '':
            double_mdx_price = '200'
        gl.set_value('double_mdx_price', double_mdx_price)

        Three_mdx_price = self.lineEdit_5.text()
        if Three_mdx_price == '':
            Three_mdx_price = '300'
        gl.set_value('Three_mdx_price', Three_mdx_price)

        time_stamp = get_TimeStamp(room_id)
        gl.set_value('time_stamp', time_stamp)

        gl.set_value('Pdk_price', 66)

        Three_mtl_price = self.lineEdit_2.text()
        if Three_mtl_price == '':
            Three_mtl_price = '2400'
        gl.set_value('Three_mtl_price',Three_mtl_price)

        Double_mtl_price = self.lineEdit.text()
        if Double_mtl_price == '':
            Double_mtl_price = '2000'
        gl.set_value('Double_mtl_price', Double_mtl_price)

        Rqq_price = self.lineEdit_3.text()
        if Rqq_price == '':
            Rqq_price = '1000'
        gl.set_value('Rqq_price', Rqq_price)

        Xjzj_price = self.lineEdit_4.text()
        if Xjzj_price == '':
            Xjzj_price = '5000'
        gl.set_value('Xjzj_price', Xjzj_price)