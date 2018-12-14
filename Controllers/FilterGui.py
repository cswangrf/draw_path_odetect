import sys

from settings import df_by_obj,bg
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt

import resources
from Models.Filters import *


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 644)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 50, 131, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 80, 91, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 110, 111, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 61, 16))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(150, 50, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(160, 20, 71, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_2.setGeometry(QtCore.QRect(320, 20, 71, 22))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 21, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 80, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 80, 21, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 80, 21, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 80, 21, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 80, 21, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 80, 21, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 80, 21, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 150, 661, 391))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 580, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(lambda: self.get_filters())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Time Filter"))
        self.checkBox_2.setText(_translate("MainWindow", "Date And Time Filter"))
        self.checkBox_3.setText(_translate("MainWindow", "Location Filter"))
        self.checkBox_4.setText(_translate("MainWindow", "Choose Boxs Filter"))
        self.label.setText(_translate("MainWindow", "Start Time"))
        self.label_2.setText(_translate("MainWindow", "End Time"))
        self.label_3.setText(_translate("MainWindow", "X1"))
        self.label_4.setText(_translate("MainWindow", "Y1"))
        self.label_5.setText(_translate("MainWindow", "X2"))
        self.label_6.setText(_translate("MainWindow", "Y2"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/paths0.png\" /></p></body></html>"))

    def get_filters(self):
        fil = {"f1": self.checkBox.checkState(), "f2": self.checkBox_2.checkState(),
               "f3": self.checkBox_3.checkState(), "f4": self.checkBox_4.checkState()}
        dr = {}
        s = {}
        for filter_name, status in fil.items():
            if status == 2:
                if filter_name == "f1":
                    s1 = str(self.timeEdit.text()) + ":00"
                    s["start_time"] = s1
                    s1 = str(self.timeEdit_2.text()) + ":00"
                    s["end_time"] = s1
                    dr["time_filter"] = s
                elif filter_name == "f2":
                    s["date"] = str(self.dateEdit.text())
                    s1 = str(self.timeEdit.text()) + ":00"
                    s["start_time"] = s1
                    s1 = str(self.timeEdit_2.text()) + ":00"
                    s["end_time"] = s1
                    dr["date_filter"] = s
                elif filter_name == "f3":
                    s["x1"] = int(self.lineEdit.text())
                    s["y1"] = int(self.lineEdit_2.text())
                    s["x2"] = int(self.lineEdit_3.text())
                    s["y2"] = int(self.lineEdit_4.text())
                    dr["location_filter"] = s

        print("Hiiiiiii!")
        plots(arguments_receiver_and_filter(dr))
        print("Byeeeeee!")


def show_image(objs, df_by_obj):
    imshow(bg, alpha=0.5)
    for t, n in objs.iteritems():
        o = df_by_obj.loc[t]
        plt.plot(o.x, o.y)
    plt.show()


def plots(dataframe):
    objs = dataframe.groupby(['filename', 'objectNum']).size()
    show_image(objs, df_by_obj)


def start():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
