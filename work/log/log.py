import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog

from Dao.dao import cursor


class Ui_Frame(QDialog):
    def setupUi(self, Frame):
        Frame.setObjectName("1")
        Frame.resize(400, 302)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabWidget = QtWidgets.QTabWidget(Frame)
        self.tabWidget.setGeometry(QtCore.QRect(70, 30, 281, 231))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 100, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab)
        self.commandLinkButton.setGeometry(QtCore.QRect(100, 140, 71, 31))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(60, 40, 51, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 51, 61))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 50, 113, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 100, 113, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.tab_2)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(100, 140, 81, 31))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(60, 40, 51, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(60, 80, 61, 61))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Frame)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        global username, password
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.commandLinkButton.setText(_translate("Frame", "登录"))
        self.label.setText(_translate("Frame", "账号："))

        username = self.label.text()

        self.label_2.setText(_translate("Frame", "密码："))
        password = self.label_2.text()
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Frame", "Tab 1"))
        self.commandLinkButton_2.setText(_translate("Frame", "注册"))
        self.label_3.setText(_translate("Frame", "账号："))
        self.label_4.setText(_translate("Frame", "密码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Frame", "Tab 2"))
        # 按钮绑定事件
        self.commandLinkButton.clicked.connect(self.upload)
        self.commandLinkButton_2.clicked.connect(self.newuser)

    def upload(self):

        sql = "select * from user where username=%s and password=%s"
        # print(sql)
        # 判断是否存在  excute 可以解决sql注入问题
        res = cursor.execute(sql, (self.lineEdit.text(), self.lineEdit_2.text()))
        res1 = cursor.fetchall()
        if res1:  # res 或者res1 都可以 返回值
            print("登陆成功")
            os.system('python mainframewindow.py')
        else:
            QtWidgets.QMessageBox.question(self, '警告', '账号密码错误，请重新输入', QtWidgets.QMessageBox.Yes)
            print('账号或者密码错误')

    def newuser(self):
        print('2')
