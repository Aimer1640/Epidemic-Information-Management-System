import os
import openpyxl
from ExButton import ExButton, Tk, Canvas, Label

import tkinter.messagebox as msgbox
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt



class Main(Tk):
    def __init__(self):
        super().__init__()
        self.top_frame = None
        self.button_frame_1 = None
        self.button_frame_2 = None
        self.main_frame_1 = None
        self.main_frame_2 = None
        self.top_button_arr = []
        self.left_button_arr = []
        self.main_button_arr = []
        self.initialize()
        self.frame_initialize()
        self.interface_initialize()


    def initialize(self):
        self.title("疫情信息管理系统")
        self.geometry("1000x620+%d+%d" % (self.winfo_screenwidth() / 2 - 500,
                                          self.winfo_screenheight() / 2 - 390))
        # self.resizable(False, False)

    def frame_initialize(self):
        self.top_frame = Canvas(self, bg="black", height=60, width=1000, highlightthickness=0)
        self.top_frame.place(x=0, y=0)
        self.button_frame_1 = Canvas(self, bg="White", height=255, width=180, highlightthickness=0)
        self.button_frame_1.place(x=30, y=90)
        self.button_frame_2 = Canvas(self, bg="White", height=215, width=180, highlightthickness=0)
        self.button_frame_2.place(x=30, y=375)
        self.main_frame_1 = Canvas(self, bg="White", height=55, width=730, highlightthickness=0)
        self.main_frame_1.place(x=240, y=90)
        self.main_frame_2 = Canvas(self, bg="White", height=440, width=730, highlightthickness=0)
        self.main_frame_2.place(x=240, y=150)

    def interface_initialize(self):
        # 布置顶层界面
        Label(self.top_frame, text="疫情信息管理系统", bg="black", fg="white", font=("楷体", 18)).place(x=30, y=13)
        top_button_1 = ExButton(self.top_frame, height=60, width=120, text="退出", font=("楷体", 12),
                                command=self.loginout)
        top_button_1.set(font_color=("White", "White"), color=("Black", "Black"))
        top_button_1.place(x=880, y=0)

        # 布置按钮界面
        Label(self.button_frame_1, text="数据库", bg="white", font=("楷体", 16)).place(x=30, y=10)
        left_button = ExButton(self.button_frame_1, height=40, width=180, text="账号信息", font=("楷体", 11),
                               command=self.show)
        left_button.set(button_list=self.left_button_arr, color=("White", "White"),
                        active_color=("DeepSkyBlue", "#F0F0F0"))
        left_button.place(x=0, y=55)
        left_button = ExButton(self.button_frame_1, height=40, width=180, text="需求信息", font=("楷体", 11),
                               command=self.need)
        left_button.set(button_list=self.left_button_arr, color=("White", "White"),
                        active_color=("DeepSkyBlue", "#F0F0F0"))
        left_button.place(x=0, y=95)
        left_button = ExButton(self.button_frame_1, height=40, width=180, text="获取数据", font=("楷体", 11),
                               command=self.get)
        left_button.set(button_list=self.left_button_arr, color=("White", "White"),
                        active_color=("DeepSkyBlue", "#F0F0F0"))
        left_button.place(x=0, y=135)
        left_button = ExButton(self.button_frame_1, height=40, width=180, text="查询城市", font=("楷体", 11),
                               command=self.check)
        left_button.set(button_list=self.left_button_arr, color=("White", "White"),
                        active_color=("DeepSkyBlue", "#F0F0F0"))
        left_button.place(x=0, y=175)
        left_button = ExButton(self.button_frame_1, height=40, width=180, text="获取词云", font=("楷体", 11),
                               command=self.wordcloude)
        left_button.set(button_list=self.left_button_arr, color=("White", "White"),
                        active_color=("DeepSkyBlue", "#F0F0F0"))
        left_button.place(x=0, y=215)

        # 布置第二层按钮界面
        # Label(self.button_frame_2, text="个人中心", bg="white", font=("楷体", 16)).place(x=30, y=10)
        # left_button = ExButton(self.button_frame_2, height=40, width=180, text="账号信息", font=("楷体", 11),
        #                        command=self.pass_command)
        # left_button.set(button_list=self.left_button_arr, color=("White", "White"),
        #                 active_color=("DeepSkyBlue", "#F0F0F0"))
        # left_button.place(x=0, y=55)
        # left_button = ExButton(self.button_frame_2, height=40, width=180, text="发布需求", font=("楷体", 11),
        #                        command=self.pass_command)
        # left_button.set(button_list=self.left_button_arr, color=("White", "White"),
        #                 active_color=("DeepSkyBlue", "#F0F0F0"))
        # left_button.place(x=0, y=95)
        # left_button = ExButton(self.button_frame_2, height=40, width=180, text="我的需求", font=("楷体", 11),
        #                        command=self.pass_command)
        # left_button.set(button_list=self.left_button_arr, color=("White", "White"),
        #                 active_color=("DeepSkyBlue", "#F0F0F0"))
        # left_button.place(x=0, y=135)
        # left_button = ExButton(self.button_frame_2, height=40, width=180, text="注销", font=("楷体", 11),
        #                        command=self.pass_command)
        # left_button.set(button_list=self.left_button_arr, color=("White", "White"),
        #                 active_color=("DeepSkyBlue", "#F0F0F0"))
        # left_button.place(x=0, y=175)
        #
        # # 页眉
        # Label(self.main_frame_1, text="主要功能", bg="White", font=("楷体", 15)).place(x=30, y=13)
        #
        # # 主界面内容
        # main_button = ExButton(self.main_frame_2, text="详情", height=35, width=70, command=self.pass_command,
        #                        font=("楷体", 11), style="vertical_color")
        # main_button.set(button_list=self.main_button_arr, active_color=("#F0F0F0", "#F0F0F0"))
        # main_button.place(x=0, y=0)

        Label(self.main_frame_2, text="Python数据爬取\t（实时爬取疫情数据）", bg="White", font=("楷体", 13)).place(x=25, y=50)
        Label(self.main_frame_2, text="查询实时城市疫情数据", bg="White", font=("楷体", 13)).place(x=25, y=85)
        Label(self.main_frame_2, text="查看账号及需求", bg="White", font=("楷体", 13)).place(x=25, y=120)
        Label(self.main_frame_2, text="查看词云", bg="White", font=("楷体", 13)).place(x=25, y=155)

    def pass_command(self):
        pass

    def loginout(self):
        print('退出成功')
        exit()

    def show(self):
        os.system('python ../user.py')
        # import user
        # self.one = user.tree.selection()()
        # self.one.show()

    def need(self):
        os.system('python ../need.py')

    def get(self):
        os.system('python ../search/searchchinanum.py')
        msgbox.showinfo('提示', '查询成功')
        print('查询成功')


    def check(self):
        # os.system('python ../citydata.py')
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

            xlsx = pd.read_excel('../data.xlsx', sheet_name='国内疫情实时数据')
            xlsx.to_csv('../data.csv', header=None)
            new, total, now, dead, heal = np.loadtxt('../data.csv', delimiter=',', usecols=(2, 3, 4, 5, 6), unpack=True,
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
            labels = '新增人数', '现有确诊', '死亡人数', '治愈人数'
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
            sys.exit(app.exec_(0))

    def wordcloude(self):
        # os.system('python ../search/citywordcloude.py')
        bg = openpyxl.load_workbook('../data.xlsx')
        sheel = bg['国内疫情实时数据']
        frequency = {}
        for row in sheel.values:
            if row[0] == '省份':
                pass
            else:
                frequency[row[0]] = float(row[1])
        from wordcloud import WordCloud
        wordcloud = WordCloud(font_path="C:/Windows/Fonts/SIMLI.TTF", background_color="white", width=1920, height=1080)
        wordcloud.generate_from_frequencies(frequency)
        wordcloud.to_file('../citywordcloude.png')
        msgbox.showinfo('提示', '成功生成词云')
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

        print('成功生成词云')



if __name__ == "__main__":
    run = Main()
    run.mainloop()

