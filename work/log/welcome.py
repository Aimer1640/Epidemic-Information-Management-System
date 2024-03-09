import sys
from PyQt5.QtWidgets import QApplication, QFrame
# 继承UI文件中的主窗口类
from log import Ui_Frame


class MyMainWindow(QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
