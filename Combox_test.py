import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QComboBox, QLineEdit, QListWidgetItem, QListWidget, QCheckBox, \
    QApplication, QVBoxLayout, QWidget
import utils.globalvar as gl

class ComboCheckBox(QComboBox):
    def loaditem(self):
        items = ['梦幻水晶鞋', '梦幻迷迭香', '梦幻摩天轮', '超跑派对卡', '超级跑车', '梦幻花环', '梦幻情书', '梦幻千纸鹤', '爱你一万年']
        self.items = ["全选"] + items  # items list
        self.box_list = []  # selected items
        self.text = QLineEdit()  # use to selected items
        self.state = 0  # use to record state

        q = QListWidget()
        for i in range(len(self.items)):
            self.box_list.append(QCheckBox())
            self.box_list[i].setText(self.items[i])
            item = QListWidgetItem(q)
            q.setItemWidget(item, self.box_list[i])
            if i == 0:
                self.box_list[i].stateChanged.connect(self.all_selected)
            else:
                self.box_list[i].stateChanged.connect(self.show_selected)

        q.setStyleSheet("font-size: 15px; font-weight: bold; height: 50px; margin-left: 5px")
        self.setStyleSheet("width: 300px; height: 100px; font-size: 12px; font-weight: bold")
        self.text.setReadOnly(True)
        self.setLineEdit(self.text)
        self.setModel(q.model())
        self.setView(q)

    # def __init__(self):
    #     items = ["Python", "Java", "Go", "C++", "JavaScript", "PHP"]
    #     super(ComboCheckBox, self).__init__()
    #     self.items = ["全选"] + items  # items list
    #     self.box_list = []  # selected items
    #     self.text = QLineEdit()  # use to selected items
    #     self.state = 0  # use to record state
    #
    #     q = QListWidget()
    #     for i in range(len(self.items)):
    #         self.box_list.append(QCheckBox())
    #         self.box_list[i].setText(self.items[i])
    #         item = QListWidgetItem(q)
    #         q.setItemWidget(item, self.box_list[i])
    #         if i == 0:
    #             self.box_list[i].stateChanged.connect(self.all_selected)
    #         else:
    #             self.box_list[i].stateChanged.connect(self.show_selected)
    #
    #     q.setStyleSheet("font-size: 15px; font-weight: bold; height: 40px; margin-left: 5px")
    #     self.setStyleSheet("width: 300px; height: 50px; font-size: 21px; font-weight: bold")
    #     self.text.setReadOnly(True)
    #     self.setLineEdit(self.text)
    #     self.setModel(q.model())
    #     self.setView(q)

    def all_selected(self):
        """
        decide whether to check all
        :return:
        """
        # change state
        if self.state == 0:
            self.state = 1
            for i in range(1, len(self.items)):
                self.box_list[i].setChecked(True)
        else:
            self.state = 0
            for i in range(1, len(self.items)):
                self.box_list[i].setChecked(False)
        self.show_selected()

    def get_selected(self) -> list:
        """
        get selected items
        :return:
        """
        ret = []
        for i in range(1, len(self.items)):
            if self.box_list[i].isChecked():
                ret.append(self.box_list[i].text())

        return ret

    def show_selected(self):
        """
        show selected items
        :return:
        """
        self.text.clear()
        ret = '; '.join(self.get_selected())
        # print(ret)
        gl.set_value('selected_gift', ret)
        self.text.setText(ret)


class UiMainWindow(QWidget):
    def __init__(self):
        super(UiMainWindow, self).__init__()
        self.setWindowTitle('Test')
        self.resize(600, 200)
        combo = ComboCheckBox()
        layout = QVBoxLayout()
        layout.addWidget(combo)
        layout.setGeometry(QtCore.QRect(50, 10, 1000, 500))
        self.setLayout(layout)


# if __name__ == "__main__":
#     # app = QApplication(sys.argv)
#     # ui = UiMainWindow()
#     # ui.show()
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     comboBox1 = ComboCheckBox(Form)
#     comboBox1.setGeometry(QtCore.QRect(50, 10, 100, 20))
#     comboBox1.setMinimumSize(QtCore.QSize(500, 50))
#     comboBox1.loaditem()
#     Form.show()
#     sys.exit(app.exec_())
