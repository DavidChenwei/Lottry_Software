from PyQt5.QtWidgets import QMainWindow
import utils.globalvar as gl
from UI_and_Operation.Third_window import Ui_Modifiy_gift_price


class Third_Window(QMainWindow, Ui_Modifiy_gift_price):

    def __init__(self):
        super(Third_Window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.transport_info)
        self.pushButton.clicked.connect(self.close_w2)

        # gl._init()

    def close_w2(self):  # 点击按钮将窗体1关掉
        self.close()

    def transport_info(self):  # 点击按键，将房间号，返点率和时间戳传给全局变量

        Mdx_price = self.lineEdit_2.text()
        if Mdx_price == '':
            Mdx_price = '100'
        gl.set_value('Mdx_price', Mdx_price)

        Mdx_price_small = self.lineEdit_10.text()
        if Mdx_price_small == '':
            Mdx_price_small = Mdx_price
        gl.set_value('Mdx_price_small', Mdx_price_small)

        Mtl_price = self.lineEdit_3.text()
        if Mtl_price == '':
            Mtl_price = '1000'
        gl.set_value('Mtl_price', Mtl_price)

        Mtl_price_small = self.lineEdit_11.text()
        if Mtl_price_small == '':
            Mtl_price_small = Mtl_price
        gl.set_value('Mtl_price_small', Mtl_price_small)

        double_mdx_price = self.lineEdit.text()
        if double_mdx_price == '':
            double_mdx_price = '200'
        gl.set_value('double_mdx_price', double_mdx_price)

        Three_mdx_price = self.lineEdit_9.text()
        if Three_mdx_price == '':
            Three_mdx_price = '300'
        gl.set_value('Three_mdx_price', Three_mdx_price)

        Pdk_price = self.lineEdit_4.text()
        if Pdk_price == '':
            Pdk_price = '10'
        gl.set_value('Pdk_price', Pdk_price)

        Three_mtl_price = self.lineEdit_5.text()
        if Three_mtl_price == '':
            Three_mtl_price = '3000'
        gl.set_value('Three_mtl_price', Three_mtl_price)

        Double_mtl_price = self.lineEdit_6.text()
        if Double_mtl_price == '':
            Double_mtl_price = '2000'
        gl.set_value('Double_mtl_price', Double_mtl_price)

        Rqq_price = self.lineEdit_7.text()
        if Rqq_price == '':
            Rqq_price = '1000'
        gl.set_value('Rqq_price', Rqq_price)

        Xjzj_price = self.lineEdit_8.text()
        if Xjzj_price == '':
            Xjzj_price = '5000'
        gl.set_value('Xjzj_price', Xjzj_price)

        print('金额修改成功，当前礼物金额：迷迭香: ', Mdx_price, ', 小迷迭香: ', Mtl_price_small, ', 两倍香: ', double_mdx_price,
              ', 三倍迷迭香: ', Three_mdx_price, ', 摩天轮, :', Mtl_price, ', 小摩天轮: ', Mtl_price_small,
              ', 两倍摩天轮: ', Double_mtl_price, ', 三倍摩天轮: ', Three_mtl_price, ', 梦幻热气球价格: ', Rqq_price,
              ', 星际战舰价格: ', Xjzj_price)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
