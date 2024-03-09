# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'citydata.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

global cityname


class Ui_Form(object):

    def __init__(self, parent=None):
        super(Ui_Form, self).__init__()
        # self.setWindowTitle("排列组合")
        # self.resize(400, 100)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(463, 362)

        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(140, 110, 200, 137))
        self.calendarWidget.setObjectName("calendarWidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(320, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(172, 70, 141, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 40, 111, 21))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 300, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 300, 56, 17))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.exit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "请输入要查询的城市:"))

        self.pushButton.setText(_translate("Form", "ok"))
        self.pushButton_2.setText(_translate("Form", "exit"))

    def search(self):
        global cityname
        cityname = self.lineEdit.text()
        print(cityname)
        show()

    def exit(self):
        print('退出成功')
        exit()


def show():
    a = cityname
    # print(a)

    xlsx = pd.read_excel('data.xlsx', sheet_name='国内疫情实时数据')
    xlsx.to_csv('data.csv', header=None)
    new, total, now, dead, heal = np.loadtxt('data.csv', delimiter=',', usecols=(2, 3, 4, 5, 6), unpack=True,
                                             encoding='utf_8')
    # print(new)
    # print(total[1])
    matplotlib.rcParams['font.family'] = 'Kaiti'
    matplotlib.rcParams['font.style'] = 'normal'
    matplotlib.rcParams['font.size'] = 12

    try:
        if a == '台湾':
            n = 0
        elif a == '香港':
            n = 1
        elif a == '上海':
            n = 2
        elif a == '北京':
            n = 3
        elif a == '四川':
            n = 4
        elif a == '吉林':
            n = 5
        elif a == '天津':
            n = 6
        elif a == '河南':
            n = 7
        elif a == '福建':
            n = 8
        elif a == '广东':
            n = 9
        elif a == '浙江':
            n = 10
        elif a == '云南':
            n = 11
        elif a == '江苏':
            n = 12
        elif a == '广西':
            n = 13
        elif a == '陕西':
            n = 14
        elif a == '重庆':
            n = 15
        elif a == '辽宁':
            n = 16
        elif a == '青海':
            n = 17
        elif a == '湖南':
            n = 18
        elif a == '山东':
            n = 19
        elif a == '澳门':
            n = 20
        elif a == '河北':
            n = 21
        elif a == '山西':
            n = 22
        elif a == '内蒙古':
            n = 23
        elif a == '安徽':
            n = 24
        elif a == '贵州':
            n = 25
        elif a == '新疆':
            n = 26
        elif a == '黑龙江':
            n = 27
        elif a == '海南':
            n = 28
        elif a == '宁夏':
            n = 29
        elif a == '湖北':
            n = 30
        elif a == '江西':
            n = 31
        elif a == '西藏':
            n = 32
        elif a == '甘肃':
            n = 33
        else:
            print('请输入正确的省市名称！')
    except:
        print('请输入正确的省市名称！')
    print(n)
    plt.subplot(2, 1, 1)
    data = [new[n], now[n], total[n], dead[n], heal[n]]
    labels = ['新增人数', '现有确诊', '累计确诊', '死亡人数', '治愈人数']

    # plt.bar(range(len(data)), data, tick_label=labels)
    plt.bar(labels, data, 0.4, color="steelblue")
    why = zip(labels, data)

    for a, b in why:  # 柱子上的数字显示
        plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=7)

    plt.title('国内疫情实时数据统计')
    plt.xlabel('人数分布（x）')
    plt.ylabel('人数（y）')
    plt.subplot(2, 1, 2)
    labels = '新增人数', '现有确诊',  '死亡人数', '治愈人数'
    sizes = [new[n], now[n], dead[n], heal[n]]
    explode = (0, 0, 0, 0)
    plt.pie(sizes, explode=explode, labels=labels, shadow=False, autopct="%1.1f%%")
    plt.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())